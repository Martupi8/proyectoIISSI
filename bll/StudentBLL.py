from dal.StudentDAL import StudentDAL
from dal.DALException import DALException
from bll.BLLException import BLLException
from bll.utils import check_not_null
from datetime import datetime
from validate_email import validate_email

class StudentBLL(StudentDAL):

    def get_all(self):
        return super().get_all()

    def get_by_OID(self, oid):
        return super().get_by_OID(oid)

    def insert(self, accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt):
        self.check_attributes_not_empty(accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt)
        self.check_accessMethod(accessMethod)
        self.check_dni_unique(dniSt)
        self.check_email_unique(emailSt)
        self.check_RN017_email(emailSt)
        self.check_RN008_selectividad(accessMethod, birthDateSt)

        try:
            studentId = super().insert(accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt)
        except DALException as exc:
            raise BLLException(exc) from exc

        return studentId
    
    def update(self, oid, accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt):
        self.check_attributes_not_empty(accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt)
        self.check_studentId_exists(oid)
        self.check_accessMethod(accessMethod)
        self.check_dni_unique(dniSt)
        self.check_email_unique(emailSt)
        self.check_RN017_email(emailSt)
        self.check_RN008_selectividad(accessMethod, birthDateSt)

        try:
            modified_id = super().update(oid, accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt)
        except DALException as exc:
            raise BLLException from exc

        return modified_id
    
    def delete(self, oid):
        self.check_studentId_exists(oid)

        try:
            deleted_id = super().delete(oid)
        except DALException as exc:
            raise BLLException(exc) from exc

        return deleted_id
    
####################################################33

    def check_attributes_not_empty(self, accessMethod, dniSt, firstNameSt, surname, birthDateSt, emailSt):
       check_not_null(accessMethod, "The accessMethod cannot be empty")
       check_not_null(dniSt, "The dniSt cannot be empty")
       check_not_null(firstNameSt, "The firstNameSt cannot be empty")
       check_not_null(surname, "The surname cannot be empty")
       check_not_null(birthDateSt, "The birthDateSt cannot be empty")
       check_not_null(emailSt, "The emailSt cannot be empty")

    def check_studentId_exists(self, oid):
        student = self.get_by_OID(oid)
        if student is None:
            raise BLLException(f"There exists no user with ID {oid}")

    def check_accessMethod(self, access):
        lista = ["Selectividad", "Ciclo", "Mayor", "Titulado Extranjero"]
        if access not in lista:
            raise BLLException(f"Cannot add or update student with accessMethod = {access}")
    
    def check_dni_unique(self, dni):
        for student in self.get_all():
            if dni == student["dniSt"]:
                raise BLLException("Two people cannot have the same DNI")
    
    def check_email_unique(self, email):
        for student in self.get_all():
            if email == student["emailSt"]:
                raise BLLException("Two people cannot have the same email")

    #RN-017 Correos bien formados
    #email debe contener @ y .
    
    def check_RN017_email(self, email):
        is_valid = validate_email(email)
        if not is_valid:
            raise BLLException(f"The email {email} is not valid.")

    #RN-008: Selectividad -> mas de 16 años
    def check_RN008_selectividad(self, accessMethod, birthDateSt):
        if accessMethod != "Selectividad":
            return
        
        date_now = datetime.now()
        date_birth_student = datetime.strptime(birthDateSt, "%Y-%m-%d")
        diff = date_now - date_birth_student
        
        if diff.days // 365 < 16:
            raise BLLException("The student is younger than 16 years old")