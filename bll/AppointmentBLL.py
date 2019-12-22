from dal.AppointmentDAL import AppointmentDAL
from dal.DALException import DALException
from bll.BLLException import BLLException
from bll.utils import check_not_null
from bll.TutorialBLL import TutorialBLL
from datetime import date 
import calendar

tutorial_bll = TutorialBLL()

class AppointmentBLL(AppointmentDAL):

    def get_all(self):
        return super().get_all()

    def get_by_OID(self, oid):
        return super().get_by_OID(oid)
    
    def get_BY_studentId(self, studentId):
        return super().get_BY_studentId(studentId)

    def get_BY_teacherId(self, teacherId):
        return super().get_BY_teacherId(teacherId)

    def insert(self, dateAppointment, hourAppointment, tutorialId, studentId):
        self.check_attributes_not_empty(dateAppointment, hourAppointment, tutorialId, studentId)
        self.check_RN005_date_hour_correct(dateAppointment, hourAppointment, tutorialId)

        try:
            appointmentId = super().insert(dateAppointment, hourAppointment, tutorialId, studentId)
        except DALException as exc:
            raise BLLException(exc) from exc

        return appointmentId
    
    def update(self, oid, dateAppointment, hourAppointment, tutorialId, studentId):
        self.check_attributes_not_empty(dateAppointment, hourAppointment, tutorialId, studentId)
        self.check_appointmentId_exists(oid)
        self.check_RN005_date_hour_correct(dateAppointment, hourAppointment, tutorialId)

        try:
            modified_id = super().update(oid, dateAppointment, hourAppointment, tutorialId, studentId)
        except DALException as exc:
            raise BLLException from exc

        return modified_id

    def delete(self, oid):
        self.check_appointmentId_exists(oid)

        try:
            deleted_id = super().delete(oid)
        except DALException as exc:
            raise BLLException(exc) from exc

        return deleted_id

#####################################################

    def check_attributes_not_empty(self, dateAppointment, hourAppointment, tutorialId, studentId):
        check_not_null(dateAppointment, "dateAppointment can't be empty")
        check_not_null(hourAppointment, "hourAppointment can't be empty")
        check_not_null(tutorialId, "The tutorialId can't be empty")
        check_not_null(studentId, "The studentId can't be empty")

    def check_appointmentId_exists(self, oid):
        appointment = self.get_by_OID(oid)
        if appointment is None:
            raise BLLException(f"There exists no appointment with ID {oid}")

    def check_RN005_date_hour_correct(self, dateAppointment, hourAppointment, tutorialId):
        dayWeek = calendar.day_name[dateAppointment.weekday()]
        tutorial = tutorial_bll.get_by_OID(tutorialId)
        if dayWeek != tutorial["dayWeek"] or hourAppointment < tutorial["startTime"] or hourAppointment >= tutorial["endTime"]:
            raise BLLException("Appointment no valid.")