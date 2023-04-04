import pymssql
import time
import uuid

# ip = "10.0.0.181,1433"
# uname = "sa"
# pwd = "admin@12345"
#cnxn = pymssql.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=shopdev;UID=%s;PWD=%s' % (ip, uname, pwd))
cnxn = pymssql.connect(host=r'10.0.0.181:1433',user=r'sa',password=r'admin@12345', database=r'shopdev')
cursor = cnxn.cursor()

# cursor.execute("SELECT * from shopdev.dbo.applog")
# for row in cursor.fetchall():
#     print(row)

while(1):
    uid1 = str(uuid.uuid4())[:3]
    uid2 = str(uuid.uuid4())[:4]
    query = "INSERT INTO applog(AsnName, eventtype, objectname, objecttype) VALUES( 'ASDFG', %s, %s, 'template')"
    params = (uid1, uid2)
    cursor.execute(query, params)
    cnxn.commit()
    time.sleep(3)

