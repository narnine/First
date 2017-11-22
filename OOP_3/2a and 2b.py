class employee:
    def calculate_payroll():
        pass

class hourlyemployee (employee):

    def __init__(self,hours):
        self.hours=hours

    def calculate_payroll(self):
        self.payroll=20.8 * 8 * self.hours

    def print_payroll(self):
        print('БАБКИ ', self.payroll)

class fixed_termemployee (employee):

    def __init__(self,fixedmoney):
        self.fixedmoney=fixedmoney

    def calculate_payroll(self):
        self.payroll=self.fixedmoney

    def print_payroll(self):
        print('БАБКИ ', self.payroll)

worker1=hourlyemployee(10)
worker1.calculate_payroll()
worker1.print_payroll()

worker2=fixed_termemployee(10)
worker2.calculate_payroll()
worker2.print_payroll()
