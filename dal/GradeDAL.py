from dal.BaseDAL import BaseDAL

class GradeDAL(BaseDAL):

    def get_all(self):
        '''
        Get grade by OID
        -Input:
            *The OID of the grade that we want to get
        -Output:
            *Only one grade
            *None value if we cannot find the OID
        '''

        q = "SELECT * FROM Grades"
        grades = self.query(q)
        return grades

    def get_by_oid(self, oid):
        '''
        Get grade by OID
        -Input:
            *The OID of the grade that we want to get
        -Output:
            *Only one grade
            *None value if we cannot find the OID
        '''

        grade = None
        q = "SELECT * FROM Grades WHERE gradeId = %s"
        params = (oid,)

        res = self.query(q, params)
        if len(res) > 0:
            grade = res[0]

        return grade

    def get_by_gradeCall_studentId_groupId(self, gradeCall, studentId, groupId):
        '''
        Get grade by gradeCall, studentId and groupId
        -Input:
            *The name of the grade that we want to get
        -Output:
            *Only one grade
            *None value if we cannot find the gradeCall, studentId and groupId
        '''

        grade = None
        q = "SELECT * FROM Grades WHERE gradeCall = %s AND studentId = %s AND groupId = %s"
        params = (gradeCall, studentId, groupId)

        res = self.query(q, params)
        if len(res) > 0:
            grade = res[0]

        return grade

    def insert(self, value, gradeCall, withHonours, studentId, groupId):
        '''
        Insert a new grade
        -Input:
            *All of the properties of the grade
        - Output:
            *The OID assigned to the grade that we have inserted
        '''

        q = "INSERT INTO Grades (value, gradeCall, withHonours, studentId, groupId) VALUES (%s, %s, %s, %s, %s)"
        params = (value, gradeCall, withHonours, studentId, groupId)
        res = self.execute(q, params)
        return res

    def update(self, oid, value, gradeCall, withHonours, studentId, groupId):
        '''
        Update one grade
        -Input:
            *All of the properties of the grade, including the OID that we want to update
        -Output:
            *The OID of the grade that we have updated
        '''

        q = "UPDATE Grades SET value = %s, gradeCall = %s, withHonours = %s, studentId = %s, groupId = %s WHERE gradeId = %s"
        params = (value, gradeCall, withHonours, studentId, groupId, oid)
        res = self.execute(q, params)
        return res

    def delete(self, oid):
        '''
        Delete one grade
        -Input:
            *The OID of the grade that we want to delete
        -Output:
            *The OID of the grade that was deleted
        '''

        q = "DELETE FROM Grades WHERE gradeId = %s"
        params = (oid,)
        res = self.execute(q, params)
        return res