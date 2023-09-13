import pandas as pd
from userManagement.controller.UserController import UserController
from userManagement.entity.User import User

class UserView:

    @staticmethod
    def register():
        print("\n[사용자 등록 화면]")
        username = input("사용자 이름 >>> ")
        password = input("비밀번호 >>> ")
        name = input("이름 >>> ")
        email = input("이메일 >>> ")

        response = UserController.registerUser(User(
            username = username,
            password = password,
            name = name,
            email = email
        ))

        if not response.__dict__.get("body"):
            print("\n데이터를 추가하는 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")
        else :
            print("\n<< 데이터 추가 성공 >>")

    @staticmethod
    def showAllUser():
        print("\n[사용자 전체 조회]")
        response = UserController.getUsersALl()

        if bool(response.body):
            print(pd.DataFrame(response.body))
        else :
            print("\n조회 할 데이터가 없습니다.")

    @staticmethod
    def showFindUser():
        print("\n[username 조회]")
        username = input("조회할 username >>> ")

        response = UserController.getUser(username)

        if bool(response.body):
            print()
            print(pd.Series(response.body))
        else :
            print("\n조회 할 데이터가 없습니다.")

    @staticmethod
    def deleteRegister():
        print("\n[사용자 삭제]")
        username = input("삭제할 username >>> ")

        response = UserController.deleteUser(username)

        if bool(response.body):
            print("\n정말로 삭제하시겠습니까?")
            check = input("Y/N 로 응답해주세요 >>> ")
            if check == "Y" or "y" :
                print("\n << 삭제 완료 >>")
            elif check == "N" or "n" :
                print("<< 취소 완료 >>")
        else :
            print("\n삭제 할 데이터가 없습니다.")

    @staticmethod
    def updateUser():
        while True:
            print("\n[사용자 정보 수정]")
            response = UserController.getUsersALl()
            if not bool(response.body):
                print("\n수정할 사용자 정보가 없습니다.")
                return
            df = pd.DataFrame(response.body)
            print(df)
            userId = input("\n수정하실 userId를 입력하세요 >>> ")

            try:
                index = df.index[df["userId"] == int(userId)].values[0]

                user = UserView.showUpdateMenu(response.body[index])
                if not bool(user):
                    print("\n수정을 취소하였습니다.")
                    return

                response = UserController.updateUser(user)
                if bool(response.body):
                    print("\n<< 수정 완료! >>")

            except Exception:
                print("\n존재하지 않는 userId입니다.")

    @staticmethod
    def showUpdateMenu(oldUser):
        newUser = oldUser.copy()
        while True:
            print("-" * 50)
            df = pd.DataFrame([oldUser, newUser], index=["전", "후"])
            print(df)
            print("-" * 50)
            print("1. password 수정")
            print("2. name 수정")
            print("3. email 수정")
            print("s. 저장")
            print("c. 취소")
            print("-" * 50)
            select = input("메뉴 선택 >>> ")

            if select == "c":
                return None

            elif select == "s":
                return newUser

            elif select == "1":
                password = input("\n변경하실 password를 입력해주세요 >>> ")

                if not UserView.isValid(oldUser.get("password"), password):
                    continue

                checkPassword = input("비밀번호 확인 입력 >>> ")

                if checkPassword != password:
                    print("비밀번호가 일치하지 않습니다.")
                    continue

                newUser["password"] = password

            elif select == "2":
                name = input("\n변경하실 name을 입력해주세요 >>> ")

                if not UserView.isValid(oldUser.get("name"), name):
                    continue

                newUser["name"] = name

            elif select == "3":
                email = input("\n변경하실 email을 입력해주세요 >>> ")

                if not UserView.isValid(oldUser.get("email"), email):
                    continue

                newUser["email"] = email

            else:
                print("선택하신 번호는 등록되지 않은 메뉴입니다.")

        print()
        return False

    @staticmethod
    def isValid(oldValue, value):

        if not bool(value):
            print("공백일 수 없습니다.")
            return False

        elif oldValue == value:
            print("기존의 정보와 동일합니다.")
            return False

        return True