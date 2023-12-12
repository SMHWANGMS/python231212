class Person:
    def __init__(self, person_id, name, phone_num):
        self.id = person_id
        self.name = name
        self.phone_num = phone_num

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Phone Number: {self.phone_num}")


class Employee(Person):
    def __init__(self, person_id, name, phone_num, title):
        super().__init__(person_id, name, phone_num)
        self.title = title


class Manager(Person):
    def __init__(self, person_id, name, phone_num, skill):
        super().__init__(person_id, name, phone_num)
        self.skill = skill


class Alba(Person):
    pass


# 샘플 코드로 10개의 객체 생성
people_list = [
    Employee(1, "John Doe", "123-456-7890", "Software Engineer"),
    Employee(2, "Jane Smith", "987-654-3210", "Data Scientist"),
    Manager(3, "Mike Johnson", "555-123-4567", "Leadership"),
    Manager(4, "Emily Davis", "888-999-0000", "Project Management"),
    Alba(5, "Alex Kim", "777-111-2222"),
    Alba(6, "Grace Lee", "333-444-5555"),
    Employee(7, "Bob Brown", "999-888-7777", "UX Designer"),
    Manager(8, "Alice White", "666-555-4444", "Communication"),
    Employee(9, "Charlie Green", "222-333-4444", "Software Developer"),
    Alba(10, "Sophia Park", "111-222-3333"),
]

# 객체 정보 출력
for person in people_list:
    person.printInfo()
