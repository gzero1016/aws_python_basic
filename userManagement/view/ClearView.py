import os

def clear():
    while(True):
        cmd = input("다음으로 넘어가시려면 Enter를 입력하세요.")
        if(not bool(cmd.replace(" ", ""))):
            break
        else:
            print("잘못된 명령입니다.")

    # os.system('cls')  #윈도우 콘솔 비워주는거
    os.system('clear')  #맥 콘솔 비워주는거