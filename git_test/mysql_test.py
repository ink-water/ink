"""
    pymysql操作流程
"""
import pymysql

# 连接本地数据库，仅有端口号port是数字形式
db = pymysql.connect(  # 关键字传参
    host="127.0.0.1",  # 默认localhost，可以省略
    port=3306,  # 默认3306，可以省略
    user="root",
    password="123456",
    database="stu",
    charset="utf8"
)
# 生成游标对象(用于操作数据库数据，获取SQL执行结果的对象)，执行SQL命令
cur = db.cursor()

# 执行各种数据库SQL命令
# # 写操作
# try:
#     # 删除
#     # cur.execute("delete from cls_1 where name = 'Bob';")
#
#     # 添加
#     # cur.execute("insert into cls_1(name,age,score) values('Dave',16,92);")
#     #
#     # cur.execute("insert into cls_1(age,score) values('Dave',16,92);")
#     # (1136, "Column count doesn't match value count at row 1")
#     #
#     # name, age, score = "Black", 20, 89
#     # dict_1 = {
#     #     "name": "Timi",
#     #     "age": 21,
#     #     "score": 89
#     # }
#     # 合成SQL命令
#     # cur.execute("insert into cls_1(name,age,score) values('%s',%s,%s);" % (name, age, score))
#     # 传递参量，不要传表名，字段名，关键字等等，只传具体数据参量
#     # cur.execute("insert into cls_1(name,age,score) values(%s,%s,%s);", [name, age, score])
#     # 使用字典类型传参
#     # cur.execute("insert into cls_1(name,age,score) values(%(name)s,%(age)s,%(score)s);", dict_1)
#     # 总结：传递的参数仅有一个时，可以直接传递不用使用列表；字典传参一定不能使用列表
#
#     # 修改
#     # cur.execute("update cls_1 set sex=%s where name = %s;", ["女", "Timi"])
#
#     # 使用executemany同时执行多次sql语句
#     exe = [("AB", 24, 78), ("Jack", 25, 90)]  # 用元组包裹sql命令单次执行的参数
#     cur.executemany("insert into cls_1(name,age,score) values(%s,%s,%s);", exe)
#
#     # 提交sql操作到数据库执行
#     db.commit()
# except Exception as e:
#     print(e)
#     # 出错时，将数据库恢复到之前的状态
#     db.rollback()

# 读操作
cur.execute("select * from cls_1;")
# cur是可迭代对象
# for i in cur:
#     print(i)

# fetchone()
print(cur.fetchone())
print(cur.fetchmany(3))
print(cur.fetchall())

# 关闭游标和数据库
cur.close()
db.close()
