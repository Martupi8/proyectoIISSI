from test.utils import Test, success, error
from bll.BLLException import BLLException
from bll.AppointmentBLL import AppointmentBLL
from bll.TutorialBLL import TutorialBLL
from bll.TeacherBLL import TeacherBLL
from datetime import datetime, timedelta

appointment_bll = AppointmentBLL()
tutorial_bll = TutorialBLL()
teacher_bll = TeacherBLL()

class TestsAppointment(Test):

    @success
    def test_get_all_positive(self):
        all_appointments = appointment_bll.get_all()
        assert len(all_appointments) > 0

    @success
    def update_positive(self):
        appointments = appointment_bll.get_all()
        appointment = appointments[0]
        tutorial = tutorial_bll.get_by_OID(appointment["tutorialId"])
        appointment_bll.update(
            oid = appointment["appointmentId"],
            dateAppointment = appointment["dateAppointment"] + timedelta(weeks=1),
            hourAppointment = tutorial["startTime"],
            tutorialId = appointment["tutorialId"],
            studentId = appointment["studentId"]
        )

    @error(BLLException)
    def update_negative(self):
        appointments = appointment_bll.get_all()
        appointment = appointments[0]
        tutorial = tutorial_bll.get_by_OID(appointment["tutorialId"])
        appointment_bll.update(
            oid = appointment["appointmentId"],
            dateAppointment = appointment["dateAppointment"] + timedelta(days=1),
            hourAppointment = tutorial["startTime"],
            tutorialId = appointment["tutorialId"],
            studentId = appointment["studentId"]
        )

    @success
    def test_delete_positive(self):
        appointments = appointment_bll.get_all()
        appointment = appointments[0]
        appointmentId = appointment_bll.insert(
            dateAppointment = appointment["dateAppointment"],
            hourAppointment = appointment["hourAppointment"] + timedelta(minutes=15),
            tutorialId = appointment["tutorialId"],
            studentId = appointment["studentId"])

        appointment = appointment_bll.get_by_OID(appointmentId)
        assert appointment is not None

        appointment_bll.delete(appointmentId)        
        appointment = appointment_bll.get_by_OID(appointmentId)
        assert appointment is None

    