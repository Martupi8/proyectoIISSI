from test.utils import Test, success, error
from bll.BLLException import BLLException
from bll.TeacherBLL import TeacherBLL

teacher_bll = TeacherBLL()

class TestsTeacher(Test):

    @success
    def test_insert_positive(self):
        teacherId = teacher_bll.insert(
            dni = "12345678A", 
            firstName = "Pepe",
            surname = "Ruiz",
            birthDate = "1975-05-27",
            email = "profesor@us.es",
            category = "Catedrático"
        )
        inserted = teacher_bll.get_by_OID(teacherId)
        assert inserted is not None

    @error(BLLException)
    def test_insert_email_not_valid_negative(self):
        teacher_bll.insert(
            dni = "12345678A", 
            firstName = "Pepe",
            surname = "Ruiz",
            birthDate = "1975-05-27",
            email = "profesorarrobauspuntoes",
            category = "Catedrático"
        )

    