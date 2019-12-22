from dal.TeacherDAL import TeacherDAL
from dal.DALException import DALException
from bll.BLLException import BLLException
from bll.utils import check_not_null
from validate_email import validate_email

class TeacherBLL(TeacherDAL):

    def get_all(self):
        return super().get_all()

    def get_by_OID(self, oid):
        return super().get_by_OID(oid)

    def insert(self, dni, firstName, surname, birthDate, email, category):
        self.check_attributes_not_empty(dni, firstName, surname, birthDate, email, category)
        self.check_category(category)
        self.check_dni_unique(dni)
        self.check_email_unique(email)
        self.check_RN017_email(email)

        try:
            teacherId = super().insert(dni, firstName, surname, birthDate, email, category)
        except DALException as exc:
            raise BLLException(exc) from exc

        return teacherId
    
    def update(self, oid, dni, firstName, surname, birthDate, email, category):
        self.check_attributes_not_empty(dni, firstName, surname, birthDate, email, category)
        self.check_teacherId_exists(oid)
        self.check_category(category)
        self.check_dni_unique(dni)
        self.check_email_unique(email)
        self.check_RN017_email(email)

        try:
            modified_id = super().update(oid, dni, firstName, surname, birthDate, email, category)
        except DALException as exc:
            raise BLLException from exc

        return modified_id
    
    def delete(self, oid):
        self.check_teacherId_exists(oid)

        try:
            deleted_id = super().delete(oid)
        except DALException as exc:
            raise BLLException(exc) from exc

        return deleted_id

##################################################

    def check_attributes_not_empty(self, dni, firstName, surname, birthDate, email, category):
        check_not_null(dni, "DNI can't be empty")
        check_not_null(category, "The teacher's category can't be empty")
        check_not_null(firstName, "The teacher's firstName can't be empty")
        check_not_null(surname, "The teacher's surname can't be empty")
        check_not_null(birthDate, "The teacher's birthDate can't be empty")
        check_not_null(email, "The teacher's email can't be empty")

    def check_teacherId_exists(self, oid):
        teacher = self.get_by_OID(oid)
        if teacher is None:
            raise BLLException(f"There exists no teacher with ID {oid}")

    def check_category(self, cat):
        lista = ["Catedrático", "Titular de Universidad", "Profesor Contratado Doctor", "Profesor Ayudante Doctor"]
        if cat not in lista:
            raise BLLException(f"Cannot add or update teacher with category = {cat}")

    def check_dni_unique(self, dni):
        for teacher in self.get_all():
            if dni == teacher["dni"]:
                raise BLLException("Two people cannot have the same DNI")

    def check_RN017_email(self, email):
        is_valid = validate_email(email)
        if not is_valid:
            raise BLLException(f"The email {email} is not valid.")
    
    def check_email_unique(self, email):
        for teacher in self.get_all():
            if email == teacher["email"]:
                raise BLLException("Two people cannot have the same email")