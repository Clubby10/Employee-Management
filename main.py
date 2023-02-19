import json

# Define the Employee class
class Employee:
    def __init__(self, id, name, position, department, salary):
        self.id = id
        self.name = name
        self.position = position
        self.department = department
        self.salary = salary

# Define the Employee Management system
class EmployeeManagement:
    def __init__(self):
        self.employees = []

    # Function to add a new employee
    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_data()

    # Function to edit an existing employee
    def edit_employee(self, id, name, position, department, salary):
        for employee in self.employees:
            if employee.id == id:
                employee.name = name
                employee.position = position
                employee.department = department
                employee.salary = salary
                self.save_data()
                return True
        return False

    # Function to delete an existing employee
    def delete_employee(self, id):
        for i, employee in enumerate(self.employees):
            if employee.id == id:
                del self.employees[i]
                self.save_data()
                return True
        return False

    # Function to search for an employee by name or ID
    def search_employee(self, search_term):
        results = []
        for employee in self.employees:
            if search_term.lower() in employee.name.lower() or search_term == employee.id:
                results.append(employee)
        return results

    # Function to generate a report
    def generate_report(self):
        report_data = []
        for employee in self.employees:
            report_data.append({
                'id': employee.id,
                'name': employee.name,
                'position': employee.position,
                'department': employee.department,
                'salary': employee.salary
            })
        with open('report.txt', 'w') as f:
            f.write(json.dumps(report_data, indent=4))

    # Function to load employee data from a file
    def load_data(self):
        try:
            with open('employees.txt', 'r') as f:
                data = json.load(f)
                for employee_data in data:
                    employee = Employee(
                        employee_data['id'],
                        employee_data['name'],
                        employee_data['position'],
                        employee_data['department'],
                        employee_data['salary']
                    )
                    self.employees.append(employee)
        except FileNotFoundError:
            pass

    # Function to save employee data to a file
    def save_data(self):
        data = []
        for employee in self.employees:
            data.append({
                'id': employee.id,
                'name': employee.name,
                'position': employee.position,
                'department': employee.department,
                'salary': employee.salary
            })
        with open('employees.txt', 'w') as f:
            f.write(json.dumps(data, indent=4))


# Initialize the Employee Management system
employee_management = EmployeeManagement()

# Load employee data from a file
employee_management.load_data()

while True:
    # Print the menu options
    print('\nEmployee Management System')
    print('--------------------------')
    print('1. Add Employee')
    print('2. Edit Employee')
    print('3. Delete Employee')
    print('4. Search Employee')
    print('5. Generate Report')
    print('6. Exit')

    # Get the user's choice
    choice = input('\nEnter your choice: ')

    if choice == '1':
        # Get the employee details from the user
        id = input('Enter ID: ')
        name = input('Enter Name: ')
        position = input('Enter Position: ')
        department = input('Entet Department: ')
        salary = input('Enter Salary: ')

        # Create a new Employee object and add it to the system
        employee = Employee(id, name, position, department, salary)
        employee_management.add_employee(employee)

    elif choice == '2':
        # Get the employee ID to edit from the user
        id = input('Enter ID of the employee to edit: ')

        # Get the updated employee details from the user
        name = input('Enter Name (leave blank to keep existing value): ')
        position = input('Enter Position (leave blank to keep existing value): ')
        department = input('Enter Department (leave blank to keep existing value): ')
        salary = input('Enter Salary (leave blank to keep existing value): ')

        # Edit the employee details
        if employee_management.edit_employee(id, name, position, department, salary):
            print('Employee details updated successfully.')
        else:
            print('Employee not found.')

    elif choice == '3':
        # Get the employee ID to delete from the user
        id = input('Enter ID of the employee to delete: ')

        # Delete the employee
        if employee_management.delete_employee(id):
            print('Employee deleted successfully.')
        else:
            print('Employee not found.')

    elif choice == '4':
        # Get the search term from the user
        search_term = input('Enter the name or ID of the employee to search for: ')

        # Search for the employee and print the results
        results = employee_management.search_employee(search_term)
        if results:
            print('\nSearch Results:')
            for employee in results:
                print(f'{employee.id} - {employee.name}, {employee.position}, {employee.department}, {employee.salary}')
        else:
            print('No results found.')

    elif choice == '5':
        # Generate the report
        employee_management.generate_report()
        print('Report generated successfully.')

    elif choice == '6':
        # Exit the program
        break

    else:
        print('Invalid choice. Please try again.')

# Save the employee data to a file before exiting
employee_management.save_data()

