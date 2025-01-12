class Employee():
    def __init__(self, name, id):
        self.name=name
        self.id=id
    def get_info(self):
        return F'Имя - {self.name}, ID - {self.id}'
    
class manager(Employee):
    def __init__(self, name, id, department=''):
        super().__init__(name, id)
        self.department= department
    def manage_project(self,):
        return f'Управление отделом -{self.department}'
    
class Technician(Employee):
    def __init__(self, name, id, specialization=''):
        super().__init__(name, id)
        self.specialization=specialization
    def perform_maintenance(self):
        return f"Выполнение технического обслуживания: {self.specialization}"
    
class TechManager(manager,Technician):
    def __init__(self, name, id, department,specialization):
        super().__init__(name,id)
        self.department=department
        self.specialization=specialization       

    def add_employee(self,employee):
        if not hasattr(self, 'team'):
            self.team = []
        self.team.append(employee)

    def get_team_info(self):
        if hasattr(self, 'team'):
            return [self.get_info() for emp in self.team]
        return "Нет сотрудников в команде"
        
    
emp1 = Employee('Иванов И.И.', 1)
emp2 = Employee('Петров П.П.', 2)
manager1 = manager('Сидоров С.С.', 3, 'Отдел разработки')
technician1 = Technician('Кузнецов К.К.', 4, 'Электроника')
tech_manager = TechManager('Смирнов С.С.', 5, 'Отдел IT', 'Сетевые технологии')


print(emp1.get_info())
print(manager1.manage_project())
print(technician1.perform_maintenance())
tech_manager.add_employee(emp1)
tech_manager.add_employee(emp2)
print(tech_manager.get_team_info())