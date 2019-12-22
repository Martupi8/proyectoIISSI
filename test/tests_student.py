from test.utils import Test, success, error
from bll.BLLException import BLLException
from bll.StudentBLL import StudentBLL

student_bll = StudentBLL()

class TestsStudent(Test):

    @success
    def test_getall_positive(self):
        all_students = student_bll.get_all()
        assert len(all_students) > 0

    @success
    def test_get_one_positive(self):
        all_students = student_bll.get_all()
        first_student = all_students[0]
        studentId = first_student["studentId"]

        student_getone = student_bll.get_by_OID(studentId)
        assert first_student == student_getone

    @success
    def test_insert_positive(self):
        studentId = student_bll.insert(
            accessMethod = "Selectividad",
            dniSt = "88888888Z",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "1990-01-01",
            emailSt = "pepe@us.es"
        )
        inserted = student_bll.get_by_OID(studentId)
        assert inserted is not None

    @error(BLLException)
    def test_insert_accessMethod_empty_negative(self):
        student_bll.insert(
            accessMethod = " ",
            dniSt = "88888888Z",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "1990-01-01",
            emailSt = "pepe@us.es"
        )

    @error(BLLException)
    def test_insert_dniSt_empty_negative(self):
        student_bll.insert(
            accessMethod = "Selectividad",
            dniSt = " ",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "1990-01-01",
            emailSt = "pepe@us.es"
        )
    
    @error(BLLException)
    def test_insert_dni_repeated_negative(self):
        all_students = student_bll.get_all()
        student = all_students[0]
        dni_existing = student["dniSt"]

        student_bll.insert(
            accessMethod = "Selectividad",
            dniSt = dni_existing,
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "1990-01-01",
            emailSt = "pepe@us.es"
        )

    @error(BLLException)
    def test_insert_accessMethod_negative(self):
        student_bll.insert(
            accessMethod = "fhgjh",
            dniSt = "88888888Z",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "1990-01-01",
            emailSt = "pepe@us.es"
        )

    @error(BLLException)
    def test_insert_email_not_valid_negative(self):
        student_bll.insert(
            accessMethod = "Selectividad",
            dniSt = "88888888Z",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "1990-01-01",
            emailSt = "pepeus.es"
        )
    
    @success
    def test_insert_RN008_positive(self):
        student_bll.insert(
            accessMethod = "Ciclo",
            dniSt = "88888888Z",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "2005-01-01",
            emailSt = "pepe@us.es"
        )

    @error(BLLException)
    def test_insert_RN008_negative(self):
        student_bll.insert(
            accessMethod = "Selectividad",
            dniSt = "88888888Z",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "2005-01-01",
            emailSt = "pepe@us.es"
        )

######################################

    @success
    def test_update_positive(self):
        all_students = student_bll.get_all()
        student = all_students[0]
        studentId = student["studentId"]

        student_bll.update(
            oid = studentId,
            accessMethod = "Selectividad",
            dniSt = "88888888Z",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "1990-01-01",
            emailSt = "pepe@us.es"
        )

        student = student_bll.get_by_OID(studentId)
        assert student["dniSt"] == "88888888Z"

    @error(BLLException)
    def test_update_email_empty_negative(self):
        all_students = student_bll.get_all()
        student = all_students[0]
        studentId = student["studentId"]

        student_bll.update(
            oid = studentId,
            accessMethod = "Selectividad",
            dniSt = "88888888Z",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "1990-01-01",
            emailSt = " "
        )

############################################

    @success
    def test_delete_positive(self):
        studentId = student_bll.insert(
            accessMethod = "Selectividad",
            dniSt = "88888888Z",
            firstNameSt = "Pepe",
            surnameSt = "Pérez",
            birthDateSt = "1990-01-01",
            emailSt = "pepe@us.es"
        )

        student = student_bll.get_by_OID(studentId)
        assert student is not None

        student_bll.delete(studentId)        
        student = student_bll.get_by_OID(studentId)
        assert student is None

    @error(BLLException)
    def test_delete_negative(self):
        student_bll.delete(12345678909876543234567876543256788765432)


