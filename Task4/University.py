

class Human:
    def __init__(self, name: str, second_name: str, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть < 0!")
        self.name = name
        self.second_name = second_name
        self.age = age

    def get_full_info(self) -> str:
        return f"{self.name} {self.second_name}, {self.age} лет"

    def calculate_scholarship(self):
        pass

    def scholarship_greater_than_other(self, other: 'Human') -> bool:
        return self.calculate_scholarship() > other.calculate_scholarship()


class Student(Human):
    def __init__(self, name: str, second_name: str,
                 age: int, group_number: str, average_grade: float):
        super().__init__(name, second_name, age)
        self.group_number = group_number
        self.average_grade = average_grade

    def calculate_scholarship(self):
        if self.average_grade == 5:
            return 6000
        elif self.average_grade >= 4:
            return 4000
        else:
            return 0

    def get_full_info(self) -> str:
        base_info = super().get_full_info()
        return (f"{base_info}, группа {self.group_number}"
                f", средний балл {self.average_grade}")


class GraduateStudent(Human):
    def __init__(self, name: str, second_name: str, age: int, group_number: str,
                 average_grade: float, research_work: str):
        super().__init__(name, second_name, age)
        self.group_number = group_number
        self.average_grade = average_grade
        self.research_work = research_work

    def calculate_scholarship(self) -> float:
        if self.average_grade == 5:
            return 8000
        elif self.average_grade >= 4:
            return 6000
        else:
            return 0

    def get_full_info(self) -> str:
        base_info = super().get_full_info()
        return (f"{base_info}, группа {self.group_number}, "
                f"средний балл {self.average_grade}, научная работа: '{self.research_work}'")


if __name__ == '__main__':
    Student = Student(name="Egor", second_name="Tertitsa", age=20,
                      group_number="5132704/30801", average_grade=4.31)
    GraduateStudent = GraduateStudent(name="Anshuman", second_name="Mishra",
                                      age=24, group_number="???", average_grade=5,
                                      research_work="PID_controllers_in_smart_house")
    print(Student.scholarship_greater_than_other(GraduateStudent))
