import re

import pymysql

db = pymysql.connect(password="123456", database="dict", user="root", charset="utf8")
cur = db.cursor()
fr = open("dict.txt")
exe = []
for line in fr:
    if line == "\n":
        break
    # print(line)
    tup = re.findall(r"(\S+)\s*( .*)", line)
    # print(tup)
    exe.append(tup[0])
sql = "insert into words(word,mean) values(%s,%s);"
try:
    cur.executemany(sql, exe)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
fr.close()
cur.close()
db.close()
