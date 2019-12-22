from dal.BaseDAL import BaseDAL

class GroupDAL(BaseDAL):

    def get_all(self):
        '''
        Get group by OID
        -Input:
            *The OID of the group that we want to get
        -Output:
            *Only one group
            *None value if we cannot find the OID
        '''

        q = "SELECT * FROM Groups"
        groups = self.query(q)
        return groups

    def get_by_oid(self, oid):
        '''
        Get group by OID
        -Input:
            *The OID of the group that we want to get
        -Output:
            *Only one group
            *None value if we cannot find the OID
        '''

        group = None
        q = "SELECT * FROM Groups WHERE groupId = %s"
        params = (oid,)

        res = self.query(q, params)
        if len(res) > 0:
            group = res[0]

        return group

    def get_by_name_year_subjectId(self, name, year, subjectId):
        '''
        Get group by name, year and subjectId
        -Input:
            *The name of the group that we want to get
        -Output:
            *Only one group
            *None value if we cannot find the name, year and subjectId
        '''

        group = None
        q = "SELECT * FROM Groups WHERE name = %s && year = %s && subjectId = %s"
        params = (name, year, subjectId)

        res = self.query(q, params)
        if len(res) > 0:
            group = res[0]

        return group

    def insert(self, name, activity, year, subjectId):
        '''
        Insert a new group
        -Input:
            *All of the properties of the group
        - Output:
            *The OID assigned to the group that we have inserted
        '''

        q = "INSERT INTO Groups (name, activity, year, subjectId) VALUES (%s, %s, %s, %s)"
        params = (name, activity, year, subjectId)
        res = self.execute(q, params)
        return res

    def update(self, oid, name, activity, year, subjectId):
        '''
        Update one group
        -Input:
            *All of the properties of the group, including the OID that we want to update
        -Output:
            *The OID of the group that we have updated
        '''

        q = "UPDATE Groups SET name = %s, activity = %s, year = %s, subjectId = %s WHERE groupId = %s"
        params = (name, activity, year, subjectId, oid)
        res = self.execute(q, params)
        return res

    def delete(self, oid):
        '''
        Delete one group
        -Input:
            *The OID of the group that we want to delete
        -Output:
            *The OID of the group that was deleted
        '''

        q = "DELETE FROM Groups WHERE groupId = %s"
        params = (oid,)
        res = self.execute(q, params)
        return res