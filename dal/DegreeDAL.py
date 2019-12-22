from dal.BaseDAL import BaseDAL

class DegreeDAL(BaseDAL):

    def get_all(self):
        '''
        Get degree by OID
        -Input:
            *The OID of the degree that we want to get
        -Output:
            *Only one degree
            *None value if we cannot find the OID
        '''

        q = "SELECT * FROM Degrees"
        degrees = self.query(q)
        return degrees

    def get_by_oid(self, oid):
        '''
        Get degree by OID
        -Input:
            *The OID of the degree that we want to get
        -Output:
            *Only one degree
            *None value if we cannot find the OID
        '''

        degree = None
        q = "SELECT * FROM Degrees WHERE degreeId = %s"
        params = (oid,)

        res = self.query(q, params)
        if len(res) > 0:
            degree = res[0]

        return degree

    def get_by_name(self, name):
        '''
        Get degree by name
        -Input:
            *The name of the degree that we want to get
        -Output:
            *Only one degree
            *None value if we cannot find the name
        '''

        degree = None
        q = "SELECT * FROM Degrees WHERE name = %s"
        params = (name,)

        res = self.query(q, params)
        if len(res) > 0:
            degree = res[0]

        return degree

    def insert(self, name, years):
        '''
        Insert a new degree
        -Input:
            *All of the properties of the degree
        - Output:
            *The OID assigned to the degree that we have inserted
        '''

        q = "INSERT INTO Degrees (name, years) VALUES (%s, %s)"
        params = (name, years)
        res = self.execute(q, params)
        return res

    def update(self, oid, name, years):
        '''
        Update one degree
        -Input:
            *All of the properties of the degree, including the OID that we want to update
        -Output:
            *The OID of the degree that we have updated
        '''

        q = "UPDATE Degrees SET name = %s, years = %s WHERE degreeId = %s"
        params = (name, years, oid)
        res = self.execute(q, params)
        return res

    def delete(self, oid):
        '''
        Delete one degree
        -Input:
            *The OID of the degree that we want to delete
        -Output:
            *The OID of the degree that was deleted
        '''

        q = "DELETE FROM Degrees WHERE degreeId = %s"
        params = (oid,)
        res = self.execute(q, params)
        return res
