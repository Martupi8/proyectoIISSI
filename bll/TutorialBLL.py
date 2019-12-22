from dal.TutorialDAL import TutorialDAL
from dal.DALException import DALException
from bll.BLLException import BLLException
from bll.TeacherBLL import TeacherBLL
from bll.utils import check_not_null
from datetime import datetime, time, timedelta

teacher_bll = TeacherBLL()

class TutorialBLL(TutorialDAL):

    def get_all(self):
        return super().get_all()

    def get_by_OID(self, oid):
        return super().get_by_OID(oid)
    
    def get_by_teacherId(self, teacherId):
        return super().get_by_teacherId(teacherId)

    def insert(self, dayWeek, startTime, endTime, teacherId):
        self.check_attributes_not_empty(dayWeek, startTime, endTime)
        self.check_weekday(dayWeek)
        self.check_RN018_PAD(teacherId, startTime, endTime)
        
        try:
            tutorialId = super().insert(dayWeek, startTime, endTime, teacherId)
        except DALException as exc:
            raise BLLException(exc) from exc
        
        return tutorialId
    
    def update(self, oid, dayWeek, startTime, endTime, teacherId):
        self.check_attributes_not_empty(dayWeek, startTime, endTime)
        self.check_tutorialId_exists(oid)
        self.check_weekday(dayWeek)
        self.check_RN018_PAD(teacherId, startTime, endTime)

        try:
            modified_id = super().update(oid, dayWeek, startTime, endTime, teacherId)
        except DALException as exc:
            raise BLLException from exc

        return modified_id
    
    def delete(self, oid):
        self.check_tutorialId_exists(oid)

        try:
            deleted_id = super().delete(oid)
        except DALException as exc:
            raise BLLException(exc) from exc

        return deleted_id

#############################################################

    def check_attributes_not_empty(self, dayWeek, startTime, endTime):
        check_not_null(dayWeek, "dayWeek can't be empty")
        check_not_null(startTime, "startTime can't be empty")
        check_not_null(endTime, "endTime can't be empty")

    def check_tutorialId_exists(self, oid):
        tutorial = self.get_by_OID(oid)
        if tutorial is None:
            raise BLLException(f"There exists no tutorial with ID {oid}")
    
    def check_weekday(self, day):
        lista = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        if day not in lista:
            raise BLLException(f"Cannot add or update tutorial on {day}")

    def check_RN018_PAD(self, teacherId, startTime, endTime):
        teacher = teacher_bll.get_by_OID(teacherId)
        if teacher["category"] == "Profesor Ayudante Doctor":
            start = datetime.strptime(startTime, "%H:%M:%S")
            end = datetime.strptime(endTime, "%H:%M:%S")
            total = end - start
            if total.seconds//3600 > 2:
                raise BLLException("A PAD teacher cannot give more than 2 hours of tutorials a week.")
            tutorials_by_teacher = self.get_by_teacherId(teacherId)
            if tutorials_by_teacher is not None:
                for t in tutorials_by_teacher:
                    start = datetime.strptime(str(t["startTime"]), "%H:%M:%S")
                    end = datetime.strptime(str(t["endTime"]), "%H:%M:%S")
                    diff = end - start
                    total = total + diff
                if total.seconds//3600 > 2:
                    raise BLLException("A PAD teacher cannot give more than 2 hours of tutorials a week.")