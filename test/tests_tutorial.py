from test.utils import Test, success, error
from bll.BLLException import BLLException
from bll.TutorialBLL import TutorialBLL
from bll.TeacherBLL import TeacherBLL

tutorial_bll = TutorialBLL()
teacher_bll = TeacherBLL()

class TestsTutorial(Test):

    @success
    def test_insert_teacher_pad_2_hours_positive(self):
        teacherId = teacher_bll.insert(
            dni = "12346789Z",
            firstName = "Manolo",
            surname = "García",
            birthDate = "1979-03-21",
            email = "manolo@us.es",
            category = "Profesor Ayudante Doctor"
        )
        tutorial_bll.insert(
            dayWeek = "Tuesday",
            startTime = "10:30:00",
            endTime = "12:30:00",
            teacherId = teacherId
        )

    @error(BLLException)
    def test_insert_teacher_pad_3_hours_negative(self):
        teacherId = teacher_bll.insert(
            dni = "12746719Z",
            firstName = "María",
            surname = "Pérez",
            birthDate = "1978-08-11",
            email = "maria@us.es",
            category = "Profesor Ayudante Doctor"
        )
        tutorial_bll.insert(
            dayWeek = "Tuesday",
            startTime = "10:30:00",
            endTime = "13:30:00",
            teacherId = teacherId
        )