from dal.BaseDAL import BaseDAL

class TeacherDAL(BaseDAL):
    
    def get_all(self):
        q = "SELECT * FROM Teachers"
        teachers = super().query(q)
        return teachers
    
    def get_by_OID(self, oid):
        q = "SELECT * FROM Teachers WHERE teacherId = %s"
        params = (oid,)
        teacher = None

        res = super().query(q, params)
        if len(res) > 0:
            teacher = res[0]

        return teacher
    
    def insert(self, dni, firstName, surname, birthDate, email, category):
        q = "INSERT INTO Teachers (dni, firstName, surname, birthDate, email, category) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (dni, firstName, surname, birthDate, email, category)
        res = self.execute(q, params)
        return res
    
    def update(self, oid, dni, firstName, surname, birthDate, email, category):
        q = "UPDATE Teachers SET dni = %s, firstName = %s, surname = %s, birthDate = %s, email = %s, category = %s WHERE teacherId = %s"
        params = (dni, firstName, surname, birthDate, email, category, oid)
        res = self.execute(q, params)
        return res

    def delete(self, oid):
        q = "DELETE FROM Teachers WHERE teacherId = %s"
        params = (oid,)
        res = self.execute(q, params)
        return res