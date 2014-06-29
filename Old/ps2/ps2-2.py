balance = float(raw_input('Enter starting balance:'))
annualInterestRate = float(raw_input('Enter annual interest rate:'))
monthlyPayment = 0
monthlyInterestRate = annualInterestRate/12.0
finalBalance = balance
while finalBalance > 0:
    monthlyPayment = monthlyPayment + 10
    updatedMonthlyBalance = balance    
    print   
    for i in range (1,13):
        monthlyUnpaidBalance = updatedMonthlyBalance - monthlyPayment
        updatedMonthlyBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate)
        print 'Remaining balance:', round(updatedMonthlyBalance,2)
    finalBalance = updatedMonthlyBalance
print
print 'Lowest payment:',monthlyPayment