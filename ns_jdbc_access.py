import jaydebeapi


class NetSuiteJdbcAccess:

    def __init__(self, nsUser, nsPassword, nsRole, nsAccount, nsHostname, nsPort, nsJarFilePath):
        self.nsUser = nsUser
        self.nsPassword = nsPassword
        self.nsRole = nsRole
        self.nsAccount = nsAccount
        self.nsHostname = nsHostname
        self.nsPort = nsPort
        self.nsJarFilePath = nsJarFilePath
        self.nsConn = None

    def openConnection(self):
        print(
            'jdbc:ns://' + self.nsHostname + ':' + self.nsPort +
            ';ServerDataSource=NetSuite.com;Encrypted=1;CustomProperties=(AccountID=' +
            self.nsAccount + ';RoleID=' + self.nsRole + ')')
        print(self.nsAccount)
        print(self.nsUser)
        self.nsConn = jaydebeapi.connect('com.netsuite.jdbc.openaccess.OpenAccessDriver',
                                         'jdbc:ns://' + self.nsHostname + ':' + self.nsPort +
                                         ';ServerDataSource=NetSuite.com;Encrypted=1;CustomProperties=(AccountID=' +
                                         self.nsAccount + ';RoleID=' + self.nsRole + ')',
                                         [self.nsUser, self.nsPassword],
                                         [self.nsJarFilePath],)

    def closeConnection(self):
        self.nsConn.close()

    def execute_sql_select_query(self, sqlQuery):
        sqlCurSor = self.nsConn.cursor()
        sqlCurSor.execute(sqlQuery)
        return sqlCurSor.fetchall()
