class RentalProperty:
    def __init__(self, purchase_price, rental_income, expenses):
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.expenses = expenses
        
    def calculate_ROI(self):
        net_income = self.rental_income - self.expenses
        return net_income / self.purchase_price * 100
    
property1 = RentalProperty(100000, 10000, 2000)
print(property1.calculate_ROI())
#This function takes the monthly income, monthly expenses, and total investment as inputs,
# and returns the ROI as a percentage. The ROI is calculated as the annual cash 
# flow (which is the monthly income minus the monthly expenses, times 12) 
# divided by the total investment, times 100 to convert it to a percentage.

def calculate_roi(income, expenses, total_investment):
    annual_cash_flow = (income - expenses) * 12
    roi = (annual_cash_flow / total_investment) * 100
    return roi

# Input numbers
income = 2000  # Total Monthly Income
expenses = 1610  # Total Monthly Expense
total_investment = 50000  # Total Investment

# Calculate ROI
roi = calculate_roi(income, expenses, total_investment)
print(f"The ROI is {roi}%.")