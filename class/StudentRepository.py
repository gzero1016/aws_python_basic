class StudentRepository:

    def __init__(self):
        # self.studentList = list()     위아래 동일한 리스트생성하는 법
        self.studentList = []

    def add(self, student):
        self.studentList.append(student)
        print("학생을 추가하였습니다.")

    def findStudentByName(self, name):
        for student in self.studentList:
            if student.name == name:
                return student
        return None

def main():
    # Student 파일로부터 Student를 가져와라
    # from : 모듈파일
    # import : 모듈 내부의 클래스, 함수, 변수
    from Student import Student
    sr = StudentRepository()
    sr.add(Student("김준일", 30))
    sr.add(Student("김준이", 30))
    sr.add(Student("김준삼", 30))
    sr.add(Student("김준사", 30))
    print(sr.studentList)

    print(sr.findStudentByName("김준사"))

# 모듈이 main 일때만 main문을 실행한다.
if __name__ == "__main__":
    main()

print("학생저장소 모듈)", __name__)