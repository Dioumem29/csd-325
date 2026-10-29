#im creating a loan interest calculator.
#lets start by defining a function with different parameters
def interest_calculator(loan_amount,interest_rate,years):
    simple_interest= loan_amount*interest_rate*years/100
    final_amount= loan_amount + simple_interest
    return simple_interest,final_amount
#now lets gather and validate the loan amount information
while True:
    try:
        loan_amount= float(input("enter the loan amount:$"))
        if loan_amount<0:
            print("loan amout cant be negative")
        else:
            break
    except ValueError:
        print("invalid value. reenter")

#gather information on interest rate and validate
while True:
    try:
        interest_rate= float(input("enter the interest rate"))
        if interest_rate<0:
            print("interest rate cant be negative")
        else:
            break
    except ValueError:
        print("invalid entry. Reenter")

#gather the lasy information which is year

while True:
    try:
        years= int(input("enter  how many years you should have to pay the loan:"))
        if years<0:
            print("years cant be negative")
        else:
            break
    except ValueError:
        print("invalid entry. Reenter")

#now call the function to calculate the simple interest
simple_interest,final_amount= interest_calculator(loan_amount,interest_rate,years)
#calculate the final amount

#now im printing the result of the final amount and the simple interest
print(f"The simple interest is ${simple_interest:.2f}\n The final amount is ${ final_amount:.2f}")
