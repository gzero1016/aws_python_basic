import pandas as pd
from userManagement.controller.UserController import UserController

class UserView:

    @staticmethod
    def register():
        from userManagement.entity.User import User
        print()
        print("[사용자 등록 화면]")
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
            print("데이터를 추가하는 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")
        else :
            print("데이터 추가 성공!")

    @staticmethod
    def showAllUser():
        print()
        print("[사용자 전체 조회]")
        response = UserController.getUsersALl()

        if bool(response.body):
            print(pd.DataFrame(response.body))
        else :
            print("조회 할 데이터가 없습니다.")

    @staticmethod
    def showFindUser():
        print()
        print("[username 조회]")
        username = input("조회할 username >>> ")
        print()

        response = UserController.getUser(username)

        if bool(response.body):
            print(pd.Series(response.body))
        else :
            print("조회 할 데이터가 없습니다.")

    @staticmethod
    def deleteRegister():
        print()
        print("[사용자 삭제]")
        username = input("삭제할 username >>> ")

        response = UserController.deleteUser(username)

        if bool(response.body):
            print("삭제 성공!")
        else :
            print("삭제 할 데이터가 없습니다.")
