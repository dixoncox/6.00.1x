numberOfMonths = 12
totalPaid = 0
for i in range(0, numberOfMonths):
    monthlyPayment = balance*monthlyPaymentRate
    monthlyUnpaidBalance  = balance - monthlyPayment
    monthlyInterestRate = annualInterestRate/12.0
    balance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
    totalPaid = totalPaid + monthlyPayment
    print 'Month:', i+1
    print 'Minimum monthly payment:', round(monthlyPayment,2)
    print 'Remaining balance:', round(balance,2)
print 'Total Paid:',round(totalPaid,2)
print 'Remaining balance:', round(balance,2)