class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print("\n--- x --- X --- x ---")
        print("First name: %s\nLast name: %s\nAge: %s" % self.firstname, self.lastname, self.age)


class Student(Person):
    id = 0

    def __init__(self, firstname, lastname, age, recordBook):
        Person.__init__(self, firstname, lastname, age)
        self.studentID = Student.id
        self.recordBook = recordBook
        Student.id += 1

    def display(self):
        print("\n--- x --- X --- x ---")
        print("First name: {}\nLast name: {}\nAge: {}".format(self.firstname, self.lastname, self.age))
        print("StudentId: %s" % self.studentID)
        print("Record Book:\n" + "\n".join(
            [" {}: {}".format(i + 2, self.recordBook[i]) for i in range(len(self.recordBook))]))


a = Student("Vladimir", "Pshenichka", 11, [4, 2, 3, 0])
a.display()

b = Student("Olga", "Slita", 45, [1, 2, 4, 2])
b.display()

c = Student("Igor", "Kalinin", 27, [0, 0, 2, 7])
c.display()


class Professor(Person):
    id = 0

    def __init__(self, firstname, lastname, age, degree):
        Person.__init__(self, firstname, lastname, age)
        self.professorID = Professor.id
        self.degree = degree
        Professor.id += 1

    def display(self):
        print("\n--- x --- X --- x ---")
        print("First name: {}\nLast name: {}\nAge: {}".format(self.firstname, self.lastname, self.age))
        print("ProfessorId: %s" % self.professorID)
        print("Degree: %s" % self.degree)


d = Professor("Ekaterina", "Gusarova", 37, "master")
d.display()

e = Professor("Alexander", "Belozubov", 40, "master")
e.display()

f = Professor("Alexey", "Pismak", 33, "master")
f.display()
