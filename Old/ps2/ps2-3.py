balance = float(raw_input('Enter starting balance:'))
annualInterestRate = float(raw_input('Enter annual interest rate:'))
monthlyInterestRate = annualInterestRate/12.0
lowPayment = balance/12.0
highPayment = (balance*(1+monthlyInterestRate)**12)/12.0
payment = (highPayment - lowPayment)/2.0
finalBalance = balance
while abs(finalBalance) > 0.10:
    updatedMonthlyBalance = balance    
    print   
    print 'Payment:',round(payment,2)
    for i in range (1,13):
        monthlyUnpaidBalance = updatedMonthlyBalance - payment
        updatedMonthlyBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate)
        print 'Remaining balance:', round(updatedMonthlyBalance,2)
    finalBalance = updatedMonthlyBalance
    if finalBalance > 0.1:
        lowPayment = payment
    elif finalBalance < -0.1:
        highPayment = payment
    payment = (lowPayment + highPayment)/2.0
print
print 'Lowest payment:',round(payment,2)