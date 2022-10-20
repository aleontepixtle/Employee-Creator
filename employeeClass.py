class Employee():
    
    def __init__(self, empName, empNumber, shiftNum, empSalary):
        self.empName = empName
        self.empNumber = empNumber
        self.shiftNum = shiftNum
        self.empSalary = empSalary
    
    def set_empName(self, empName):
        self.set_empName = empName
    
    def set_empNumber(self, empNumber):
        self.set_empNumber = empNumber   
    
    def set_shiftNum(self, shiftNum):
        self.set_shiftNum = shiftNum
    
    def set_empSalary(self, empSalary):
        self.set_empSalary
        
    def get_Name(self, empName):
        return self.empName
    
    def get_Number(self, empNumber):
        return self.empNumber
    
    def get_shiftNum(self, shiftNum):
        return self.set_shiftNum
    
    def get_empSalary(self, empSalary):
        return self.set_empSalary    

    
class Supervisor(Employee):
    
    def __init__(self, empName, empNumber, shiftNum, empSalary, bonusPay, metGoal):
        super().__init__(empName, empNumber, shiftNum, empSalary)
        self.bonusPay = bonusPay
        self.metGoal = metGoal
     
    def set_bonusPay(self, bonusPay):
        self.bonusPay
   
    def set_metGoal(self, metGoal):
        self.metGoal
      
    def get_bonusPay(self,bonusPay):
        return self.bonusPay
    
    def get_metGoal(self, metGoal):
        return self.get_metGoal


#newProductionWorker = ProductionWorker('Johnny Appleseed', '103', 3, 19.50)
#print("Worker Name:   " , newProductionWorker.empName)
#print("Worker Number: " , newProductionWorker.empNumber)
#print("Worker Shift:  " , newProductionWorker.shiftNumber)
#print("Worker Pay:    $", str(newProductionWorker.hourPay), sep="")

