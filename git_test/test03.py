import pymysql


class Database:
    def __init__(self):
        self.db = pymysql.connect(password="123456", database="client", user="root", charset="utf8")
        self.cur = self.db.cursor()

    def register(self):
        print("按回车键退出注册界面")
        while True:
            name = input("请输入用户名：")
            if not name:
                break
            password = input("请输入密码：")
            if not password:
                break
            try:
                self.cur.execute("insert into user_info(uname,password) values(%s,%s)", [name, password])
                self.db.commit()
                print("用户" + name + "注册成功")
                break
            except:
                print("用户名重复，请重新输入")
                self.db.rollback()

    def login_in(self):
        print("按回车键退出登录界面")
        while True:
            name = input("请输入用户名：")
            if not name:
                break
            password = input("请输入密码：")
            if not password:
                break
            try:
                self.cur.execute("select * from user_info where uname=%s and password=%s", [name, password])
            except Exception as e:
                print(e)
            # print(cur)
            if self.cur.fetchone():
                print("欢迎" + name + "回来")
            else:
                print("用户名或者密码错误，请重新输入")

    def choose(self):
        while True:
            item = input("登录请按1，注册请按2，其余任意键退出")
            if item == "1":
                self.login_in()
            elif item == "2":
                self.register()
            else:
                break

    def main(self):
        self.choose()
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    database = Database()
    database.main()
