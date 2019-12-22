from dal.BaseDAL import BaseDAL

class TutorialDAL(BaseDAL):
    
    def get_all(self):
        q = "SELECT * FROM Tutorials"
        tutorials = super().query(q)
        return tutorials
    
    def get_by_OID(self, oid):
        q = "SELECT * FROM Tutorials WHERE tutorialId = %s"
        params = (oid,)
        tutorial = None

        res = super().query(q, params)
        if len(res) > 0:
            tutorial = res[0]

        return tutorial

    def get_by_teacherId(self, teacherId):
        q = "SELECT * FROM Tutorials WHERE teacherId = %s"
        params = (teacherId,)
        tutorials = None

        res = super().query(q, params)
        if len(res) > 0:
            tutorials = res
        
        return tutorials
    
    def insert(self, dayWeek, startTime, endTime, teacherId):
        q = "INSERT INTO Tutorials (dayWeek, startTime, endTime, teacherId) VALUES (%s, %s, %s, %s)"
        params = (dayWeek, startTime, endTime, teacherId)
        res = super().execute(q, params)
        return res
    
    def update(self, oid, dayWeek, startTime, endTime, teacherId):
        q = "UPDATE Tutorials SET dayWeek = %s, startTime = %s, endTime = %s, teacherId = %s WHERE tutorialId = %s"
        params = (dayWeek, startTime, endTime, teacherId, oid)
        res = super().execute(q, params)
        return res

    def delete(self, oid):
        q = "DELETE FROM Tutorials WHERE tutorialId = %s"
        params = (oid,)
        res = super().execute(q, params)
        return res