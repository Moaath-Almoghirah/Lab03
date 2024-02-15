

employee_list = dict()
x = 0
while(True):
    employee_name = str(input("Enter employee's name\nIf you want to exit type 'no' \n"))
    if employee_name=='no':
        break
    employee_salary = int(input("Enter employee's salary\n"))
    employee_list[employee_name]={employee_salary}

print(employee_list)

    
