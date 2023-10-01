class Student:

    # 생성자
    # self == this -> 자기 자신의 주소(생성된 객체의 주소)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # toString()
    def __str__(self):
        return f"Student[name: {self.name}, age: {self.age}]"

    def setName(self, name):
        self.name = name

# 함수정의후 : 를 찍었으면 pass라고 넣어줘야 다음줄이 실행됨
def student():
    pass

def main():
    # new 키워드가 필요없다.
    s1 = Student("김준일", 30)
    print(s1.name)

# 모듈이 main 일때만 main문을 실행한다.
if __name__ == "__main__":
    main()

print("학생모듈)", __name__)
