from ns_jdbc_access import NetSuiteJdbcAccess

netsuite_db_params = {'user': 'fndbhyperspace@fashionnova.com', 'password': '', 'role': '1086', 'account': '',
                      'hostname': '', 'port': '1708'}
po_ns_connector = NetSuiteJdbcAccess(
    netsuite_db_params['user'], netsuite_db_params['password'], netsuite_db_params['role'],
    netsuite_db_params['account'], netsuite_db_params['hostname'], netsuite_db_params['port'],
    'NQjc.jar')
po_ns_connector.openConnection()
