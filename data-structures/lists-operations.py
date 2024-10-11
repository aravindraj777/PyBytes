exp = [2200,2350,2600,2130,2190]

def compare_extra_amount():
    print(f"extra amount spent on februarry is {abs(exp[1] - exp[0])}")
    
def total_expense_first_quarter():
    print(f"Total expense in the first quarter is {(exp[0] + exp[1]+ exp[2])}")

def is_spend_2000():
    print(f"Did I spend 2000 exactly in any month? : ANS-->",2000 in exp)

def expense_after_june():
    exp.append(1980)
    print("Expense after june is ",exp)
    
def expense_correction_april():
   exp[3] = exp[3] - 200
   print("Expense correction after 200 dollar deduction in april :", exp)
    
compare_extra_amount()
total_expense_first_quarter()
is_spend_2000()
expense_after_june()
expense_correction_april()