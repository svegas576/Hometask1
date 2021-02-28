class Worker:
    def __init__(self,name,surname,position,wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Оклад: ": wage, "Премия: ": bonus}

class Position(Worker):
    def __init__(self,name,surname,position,wage, bonus):
        Worker.__init__(self,name,surname,position,wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return int(self._income["Оклад: "]) + int(self._income["Премия: "])

ivanov = Position("Иван", "Иванов", "слесарь", "30000", "10000")
petrov = Position("Петр", "Петров", "механик", "35000", "7000")
sidorov = Position("Федор", "Сидоров", "менеджер", "40000", "20000")
print(ivanov.name,ivanov.surname,ivanov.position,ivanov._income)
print(sidorov.get_full_name())
print(petrov.get_total_income())
