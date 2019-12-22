from dal.BaseDAL import BaseDAL

class AppointmentDAL(BaseDAL):
    
    def get_all(self):
        q = "SELECT * FROM Appointments"
        appointments = super().query(q)
        return appointments
    
    def get_by_OID(self, oid):
        q = "SELECT * FROM Appointments WHERE appointmentId = %s"
        params = (oid,)
        appointment = None

        res = super().query(q, params)
        if len(res) > 0:
            appointment = res[0]

        return appointment

    def get_BY_studentId(self, studentId):
        q = "SELECT * FROM Appointments WHERE studentId = %s"
        params = (studentId,)
        appointments = None

        res = super().query(q, params)
        if len(res) > 0:
            appointments = res
        
        return appointments

    def get_BY_teacherId(self, teacherId):
        q = "SELECT dateAppointment, hourAppointment, tutorialId, studentId FROM Appointments NATURAL JOIN Tutorials WHERE teacherId = %s"
        params = (teacherId,)
        appointments = None

        res = super().query(q, params)
        if len(res) > 0:
            appointments = res
        
        return appointments
    
    def insert(self, dateAppointment, hourAppointment, tutorialId, studentId):
        q = "INSERT INTO Appointments (dateAppointment, hourAppointment, tutorialId, studentId) VALUES (%s, %s, %s, %s)"
        params = (dateAppointment, hourAppointment, tutorialId, studentId)
        res = super().execute(q, params)
        return res
    
    def update(self, oid, dateAppointment, hourAppointment, tutorialId, studentId):
        q = "UPDATE Appointments SET dateAppointment = %s, hourAppointment = %s, tutorialId = %s, studentId = %s WHERE appointmentId = %s"
        params = (dateAppointment, hourAppointment, tutorialId, studentId, oid)
        res = super().execute(q, params)
        return res

    def delete(self, oid):
        q = "DELETE FROM Appointments WHERE appointmentId = %s"
        params = (oid,)
        res = super().execute(q, params)
        return res