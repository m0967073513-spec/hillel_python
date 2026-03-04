
from student_group import Student, Group, GroupLimitError

def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)

    print(gr)

    assert gr.find_student('Jobs') == st1  
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Taylor')
    print(gr)

    # Доп-проверка лимита 
    try:
        for i in range(20):
            gr.add_student(Student('Male', 18 + i, f'Name{i}', f'Last{i}', f'RB{i}'))
    except GroupLimitError as e:
        print("Caught:", e)


if __name__ == "__main__":
    main()