import employeeClass as EMP

def createEmployee():
    """self, empName, empNumber, shiftNum, empSalary"""
    empName = input("Enter employee Name:\t")
    empNumber = input("Enter employee Number:\t ")
    shiftNum = input("Enter Shift number:\t")
    empSalary = int(input("Enter employee Salary:\t$"))
    newEmployee = EMP.Employee(empName, empNumber, shiftNum, empSalary)
    return newEmployee

def createSuperVisor(newEmployee):
    """empName, empNumber, shiftNum, empSalary, bonusPay, metGoal"""
    goalCheck = input('Did supervisor ' + newEmployee.get_Name(newEmployee) +
                    ' meet the production goal? Y/N ').upper()
    if goalCheck == 'Y':
        metGoal = True
        bonusPay = 7500 + newEmployee.empSalary
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
           
def supervisorCheck(newEmployee):
    
    userinput = input("Is " + newEmployee.get_Name(newEmployee) + " a supervisor? Y/N ").upper()
    if userinput == 'Y':
        return True
    else:
        return False

    
def main():
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