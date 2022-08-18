class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": "", "bonus": ""}

class Position(Worker):
    def get_full_name(self, name, surname, position):
        people = []
        people.append(name)
        people.append(surname)
        people.append(position)
        print(people)
    def get_total_income(self, _income):
        many_sum = 0
        many_sum = int(_income["wage"]) + int(_income["bonus"])
        print(many_sum)

p = Position()
p.name = input("Enter name: ")
p.surname = input("Enter surname: ")
p.position = input("Enter position: ")
p._income["wage"] = input("Enter wage: ")
p._income["bonus"] = input("Enter bonus: ")
p.get_full_name(p.name, p.surname, p.position)
p.get_total_income(p._income)



