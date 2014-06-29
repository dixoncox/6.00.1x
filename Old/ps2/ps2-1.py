balance = float(raw_input('Enter starting balance:'))
annualInterestRate = float(raw_input('Enter annual interest rate:'))
monthlyPaymentRate = float(raw_input('Enter monthly payment rate:'))
monthlyInterestRate = annualInterestRate/12.0
updatedMonthlyBalance = balance
totalPaid = 0
print
for i in range (1,13):
    minPayment = updatedMonthlyBalance * monthlyPaymentRate
    monthlyUnpaidBalance = updatedMonthlyBalance - minPayment
    updatedMonthlyBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
    totalPaid = totalPaid + minPayment
    print 'Month:',i
    print 'Minimum monthly payment:', round(minPayment,2)
    print 'Remaining balance:', round(updatedMonthlyBalance,2)
print 'Total paid:', round(totalPaid,2)
print 'Remaining balance:', round(updatedMonthlyBalance,2)