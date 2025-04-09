##################
# 프로그램명: 성적관리 프로그램
# 작성자: 소프트웨어학과/김재훈
# 작성일: 2025-04-09
# 프로그램 설명: 5명의 학생 정보를 객체지향 방식으로 관리하며,
#               입력, 출력, 삽입, 삭제, 탐색, 정렬, 통계 기능 포함
##################

class Student:
    def __init__(self, s_num, name, english, c_lang, python):
        self.s_num = s_num
        self.name = name
        self.english = english
        self.c_lang = c_lang
        self.python = python
        self.total = 0
        self.average = 0.0
        self.grade = ''
        self.rank = 0
        self.calculate_total_average()
        self.calculate_grade()

    def calculate_total_average(self):
        self.total = self.english + self.c_lang + self.python
        self.average = self.total / 3

    def calculate_grade(self):
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

class GradeManager:
    def __init__(self):
        self.students = []

    def input_student(self):
        s_num = int(input("학번: "))
        name = input("이름: ")
        english = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python = int(input("파이썬 점수: "))
        student = Student(s_num, name, english, c_lang, python)
        self.students.append(student)
        self.assign_ranks()

    def assign_ranks(self):
        self.students.sort(key=lambda s: s.total, reverse=True)
        for idx, student in enumerate(self.students):
            student.rank = idx + 1

    def print_all(self):
        print("\n성적관리 프로그램")
        print("=" * 70)
        print(f"{'학번':<10}{'이름':<10}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<6}{'등수':<6}")
        print("-" * 70)
        for s in self.students:
            print(f"{s.s_num:<10}{s.name:<10}{s.english:<8}{s.c_lang:<8}{s.python:<8}{s.total:<8}{s.average:<8.2f}{s.grade:<6}{s.rank:<6}")

    def delete_student(self, s_num):
        self.students = [s for s in self.students if s.s_num != s_num]
        self.assign_ranks()

    def search_by_number(self, s_num):
        return [s for s in self.students if s.s_num == s_num]

    def search_by_name(self, name):
        return [s for s in self.students if s.name == name]

    def sort_by_total(self):
        self.assign_ranks()

    def count_above_80(self):
        return sum(1 for s in self.students if s.average >= 80)

def main():
    gm = GradeManager()
    for i in range(5):
        print(f"\n학생 {i+1} 정보 입력")
        gm.input_student()

    while True:
        print("\n[메뉴]")
        print("1. 성적 출력")
        print("2. 학생 추가")
        print("3. 학생 삭제")
        print("4. 학번으로 검색")
        print("5. 이름으로 검색")
        print("6. 총점 기준 정렬")
        print("7. 평균 80점 이상 학생 수")
        print("0. 종료")
        choice = input("메뉴 선택: ")

        if choice == '1':
            gm.print_all()
        elif choice == '2':
            gm.input_student()
            print("학생이 추가되었습니다.")
        elif choice == '3':
            s_num = int(input("삭제할 학생의 학번: "))
            gm.delete_student(s_num)
            print("학생이 삭제되었습니다.")
        elif choice == '4':
            s_num = int(input("검색할 학번: "))
            result = gm.search_by_number(s_num)
            GradeManager().students = result
            gm.print_all()
        elif choice == '5':
            name = input("검색할 이름: ")
            result = gm.search_by_name(name)
            GradeManager().students = result
            gm.print_all()
        elif choice == '6':
            gm.sort_by_total()
            print("총점 기준 정렬 완료.")
        elif choice == '7':
            count = gm.count_above_80()
            print(f"80점 이상 평균을 받은 학생 수: {count}명")
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()