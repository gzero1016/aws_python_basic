class UserInfo:

    # cls 변수(클래스 변수 == static)
    adminUser = {
        "username": "root",
        "password": "1q2w3e4r"
    }

    # 맴버변수 선언할때는 init에 넣고 cls변수만 위쪽으로 넣는다.
    def __init__(self):
        self.adminUser = {
            "username": "user1",
            "password": "1234"
        }

    @classmethod
    def showAdminUser(cls):
        print("[showAdminUser]")
        print(cls.adminUser)

class User:

    def __init__(self):
        self.username = None
        self.password = None
        self.name = None
        self.email = None

    # 아무데도 접근할 수 없는 그냥 실행만 할 수 있는 메소드(싱글톤)
    @staticmethod
    def showUserClassInfo():
        print("그냥 실행할 수 있는 메소드")

if __name__ == "__main__":
    userInfo = UserInfo()
    #
    print(userInfo.adminUser)
    # 아래는 Static
    print(UserInfo.adminUser)

    userInfo.showAdminUser()
    UserInfo.showAdminUser()

    User.showUserClassInfo()