# Author: Andres Leon T
# Date: 03/2021
# Purpose: This program creats employee objects and asks for user input for their attributes.
# The program will ask if the employee is a supervisor and will increase their pay if they met the bonus goal.
# Then it will neatlty print the details of the employee/supervisor.
import employeeClass as EMP # imports employee class from seperate file

def createEmployee(): # create employee object
    """self, empName, empNumber, shiftNum, empSalary"""
    empName = input("Enter employee Name:\t")
    empNumber = input("Enter employee Number:\t ")
    shiftNum = input("Enter Shift number:\t")
    empSalary = int(input("Enter employee Salary:\t$"))
    newEmployee = EMP.Employee(empName, empNumber, shiftNum, empSalary)
    return newEmployee

def createSuperVisor(newEmployee): # creates supervisor object
    """empName, empNumber, shiftNum, empSalary, bonusPay, metGoal"""
    goalCheck = input('Did supervisor ' + newEmployee.get_Name(newEmployee) +
                    ' meet the production goal? Y/N ').upper()
    if goalCheck == 'Y': # checks for goal requirement
        metGoal = True
        bonusPay = 7500 + newEmployee.empSalary # increases base pay
    else:
        metGoal = False
        bonusPay = 0 + newEmployee.empSalary
        
    newSupervisor = EMP.Supervisor(newEmployee.get_Name(newEmployee), 
        newEmployee.get_Number(newEmployee),                        
        newEmployee.get_shiftNum(newEmployee),
        newEmployee.get_empSalary(newEmployee),
        bonusPay,
        metGoal)
    
    return newSupervisor
           
def supervisorCheck(newEmployee): # asks user for if employee is a supervisor
    
    userinput = input("Is " + newEmployee.get_Name(newEmployee) + " a supervisor? Y/N ").upper()
    if userinput == 'Y':
        return True
    else:
        return False

    
def main(): # main creates employee/supervisor based on user input for type of employee
    newEmployee = createEmployee()
    superFlag = supervisorCheck(newEmployee)
    
    if superFlag == True:
        newSuperVisor = createSuperVisor(newEmployee)
        print('-------------------------------------')
        print("Supervisor Name:   ", newEmployee.empName)
        print("Supervisor Number: ", newEmployee.empNumber)
        print("Supervisor Shift:  ", str(newEmployee.shiftNum))    
        print("Supervisor Pay:    ", "${:,.2f}".format(newSuperVisor.get_bonusPay(newSuperVisor)), sep="")

    else:
        print('-------------------------------------')
        print("Worker Name:   ", newEmployee.empName)
        print("Worker Number: ", newEmployee.empNumber)
        print("Worker Shift:  ", str(newEmployee.shiftNum))
        print("Worker Pay:   ", "${:,.2f}".format(newEmployee.empSalary), sep="")

main()
