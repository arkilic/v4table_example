from pvaccess import PvObject, STRING, DOUBLE, NtTable

import pvaccess

pvObject = PvObject({'labels' : [STRING], 'value' : {'column0' : [DOUBLE], 'column1' : [DOUBLE], 'column2' : [DOUBLE]}})

pvObject.setScalarArray('labels', ['x', 'y', 'z'])
pvObject.setStructure('value', {'column0' : [0.1, 0.2, 0.3], 'column1' : [1.1, 1.2, 1.3], 'column2' : [2.1, 2.2, 2.3]})
table3 = NtTable(pvObject)

print table3

rpc = pvaccess.RpcClient('table')
request = table3

rpc.invoke(request)

