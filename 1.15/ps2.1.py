balance = 4213
annualInterestRate = 0.2 
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.0
totalPaid = 0
for i in range(12):
    minimumPayment = balance*monthlyPaymentRate
    balancePreInterest = balance - minimumPayment
    balance = balancePreInterest + balancePreInterest*monthlyInterestRate
    totalPaid += minimumPayment
    print 'Month:',i+1
    print 'Minimum monthly payment:', round(minimumPayment,2)
    print 'Remaining balance:',round(balance,2)
    print
print 'Total paid:',round(totalPaid,2)    
print 'Remaining balance:',round(balance,2)