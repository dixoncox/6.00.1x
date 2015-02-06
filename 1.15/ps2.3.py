balance = 320000
balance = 999999
#annualInterestRate = 0.2
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12.0
lowPayment = balance/12.0
highPayment = (balance*(1+monthlyInterestRate)**12)/12.0
newBalance = balance
while abs(newBalance) > 0.10:
    newBalance = balance
    payment = (highPayment + lowPayment)/2.0
    for i in range(12):
        newBalance = ((newBalance-payment) + 
                      (newBalance-payment)*monthlyInterestRate)
    if abs(newBalance) > 0.10:
        if newBalance > 0:
            lowPayment = payment
        else:
            highPayment = payment
print 'Lowest payment:', round(payment,2)