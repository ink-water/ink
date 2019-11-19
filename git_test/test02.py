import pymysql

db = pymysql.connect(password="123456", database="stu", user="root", charset="utf8")
cur = db.cursor()
# with open("jth.jpg", "rb") as f_obj:
#     data = f_obj.read()
# try:
#     sql = "insert into cls_1 values(%s,%s,%s,%s,%s,%s)"
#     cur.execute(sql, [16, data, "jth", 17, "女", 100])
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
sql = "select img from cls_1 where name=%s;"
cur.execute(sql, "jth")
print(cur)
data = cur.fetchone()
with open("jth.jpg", "wb") as fw:
    fw.write(data[0])

cur.close()
db.close()
