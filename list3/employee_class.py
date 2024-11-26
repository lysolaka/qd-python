class Employee:
    def __init__(self, emp_id: str, emp_name: str, emp_salary: int,
                 emp_department: str):
        self.id = emp_id
        self.name = emp_name
        self.salary = emp_salary
        self.department = emp_department

    def assign_department(self, emp_department: str):
        self.department = emp_department

    def print_details(self):
        print(f"{self.name}: {self.id}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

    def calculate_salary(self, hours_worked: int) -> float:
        overtime = hours_worked - 50
        if overtime > 0:
            payout = overtime * (self.salary / 50)
            return payout + float(self.salary)
        else:
            return float(self.salary)
