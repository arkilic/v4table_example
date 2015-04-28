import pvaccess
import hashlib
from pvaccess import PvObject, STRING, DOUBLE, NtTable


srv = pvaccess.RpcServer()

def hash(x):
    md5 = hashlib.md5()
    md5.update(str(x))
    h = md5.hexdigest()
    dict = x.getStructureDict()
    dict['hash'] = pvaccess.STRING
    response = pvaccess.PvObject(dict)
    response.setString('hash', h)
    return response

def table(x):
    ntTable = pvaccess.NtTable(x)
    col1 = ntTable.getColumn(1)
    print "server got column 1"
    r = pvaccess.PvString('abcd')
    return r

srv.registerService('hash', hash)
srv.registerService('table', table)

srv.listen()
