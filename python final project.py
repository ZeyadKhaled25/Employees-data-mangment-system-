class Employee:
    def __init__(self, emp_id, name, position, salary, email):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    def update_details(self, name=None, position=None, salary=None, email=None):
        if name: 
            self.name = name
        if position:
            self.position = position
        if salary:
            self.salary = salary
        if email:
            self.email = email

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Email: {self.email}"
import csv

class EmployeeManager:
    def __init__(self, file_name="employees.csv"):
        self.file_name = file_name
        self.employees = self.load_employees()

    def load_employees(self):
        employees = {}
        try:
            with open(self.file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    emp = Employee(row['ID'], row['Name'], row['Position'], float(row['Salary']), row['Email'])
                    employees[emp.emp_id] = emp
        except FileNotFoundError:
            pass
        return employees

    def save_employees(self):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Position", "Salary", "Email"])
            writer.writeheader()
            for emp in self.employees.values():
                writer.writerow({
                    "ID": emp.emp_id, 
                    "Name": emp.name, 
                    "Position": emp.position, 
                    "Salary": emp.salary, 
                    "Email": emp.email
                })

    def add_employee(self, emp_id, name, position, salary, email):
        if emp_id in self.employees:
            raise ValueError("Employee ID already exists.")
        self.employees[emp_id] = Employee(emp_id, name, position, float(salary), email)
        self.save_employees()

    def update_employee(self, emp_id, **kwargs):
        if emp_id not in self.employees:
            raise ValueError("Employee not found.")
        self.employees[emp_id].update_details(**kwargs)
        self.save_employees()

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            self.save_employees()
        else:
            raise ValueError("Employee not found.")

    def search_employee(self, emp_id):
        return self.employees.get(emp_id, None)

    def list_employees(self):
        return self.employees.values()
def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Data Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List All Employees")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                emp_id = input("Enter Employee ID: ").strip()
                name = input("Enter Name: ").strip()
                position = input("Enter Position: ").strip()
                salary = input("Enter Salary: ").strip()
                email = input("Enter Email: ").strip()
                manager.add_employee(emp_id, name, position, salary, email)
                print("Employee added successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                emp_id = input("Enter Employee ID to update: ").strip()
                name = input("Enter new Name (or press Enter to skip): ").strip()
                position = input("Enter new Position (or press Enter to skip): ").strip()
                salary = input("Enter new Salary (or press Enter to skip): ").strip()
                email = input("Enter new Email (or press Enter to skip): ").strip()
                manager.update_employee(emp_id, name=name or None, position=position or None, salary=salary or None, email=email or None)
                print("Employee updated successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                emp_id = input("Enter Employee ID to delete: ").strip()
                manager.delete_employee(emp_id)
                print("Employee deleted successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            emp_id = input("Enter Employee ID to search: ").strip()
            emp = manager.search_employee(emp_id)
            print(emp if emp else "Employee not found.")

        elif choice == '5':
            employees = manager.list_employees()
            if employees:
                for emp in employees:
                    print(emp)
            else:
                print("No employees found.")

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
