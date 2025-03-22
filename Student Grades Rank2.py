def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def get_student_data():
    students = []
    for i in range(5):
        s_num = int(input(f"학생 {i + 1}의 학번: "))
        name = input(f"학생 {i+1}의 이름: ")
        english = int(input(f"{name}의 영어 점수: "))
        c_lang = int(input(f"{name}의 C-언어 점수: "))
        python = int(input(f"{name}의 파이썬 점수: "))
        total = english + c_lang + python
        average = total / 3
        grade = calculate_grade(average)
        students.append((s_num, name, english, c_lang, python, total, average, grade))
    return students

def assign_ranks(students):
    students.sort(key=lambda s: s[5], reverse=True)  # 총점 기준 정렬
    ranked_students = []
    for idx, student in enumerate(students):
        ranked_students.append(student + (idx + 1,))  # 등수 추가
    return ranked_students

def print_results(students):
    print("\n성적관리 프로그램")
    print("=" * 50)
    print(f"{'학번':<20}{'이름':<10}{'영어':<8}{'C-언어':<8}{'파이썬':<8}{'총점':<8}{'평균':<8}{'학점':<6}{'등수':<6}")
    print("-" * 50)
    for student in students:
        print(f"{student[0]:<20}{student[1]:<10}{student[2]:<8}{student[3]:<8}{student[4]:<8}{student[5]:<8}{student[6]:<8.2f}{student[7]:<6}{student[8]:<6}")

def main():
    students = get_student_data()
    students_with_ranks = assign_ranks(students)
    print_results(students_with_ranks)

if __name__ == "__main__":
    main()
