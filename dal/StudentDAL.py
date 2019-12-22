from dal.BaseDAL import BaseDAL

class StudentDAL(BaseDAL):
    
    def get_all(self):
        q = "SELECT * FROM Students"
        students = super().query(q)
        return students
    
    def get_by_OID(self, oid):
        q = "SELECT * FROM Students WHERE studentId = %s"
        params = (oid,)
        student = None

        res = super().query(q, params)
        if len(res) > 0:
            student = res[0]

        return student
    
    def insert(self, accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt):
        q = "INSERT INTO Students (accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt)
        res = super().execute(q, params)
        return res
    
    def update(self, oid, accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt):
        q = "UPDATE Students SET accessMethod = %s, dniSt = %s, firstNameSt = %s, surnameSt = %s, birthDateSt = %s, emailSt = %s WHERE studentId = %s"
        params = (accessMethod, dniSt, firstNameSt, surnameSt, birthDateSt, emailSt, oid)
        res = super().execute(q, params)
        return res

    def delete(self, oid):
        q = "DELETE FROM Students WHERE studentId = %s"
        params = (oid,)
        res = super().execute(q, params)
        return res