print("EMI Calculator \n")
p=int(input("Enter the principle amount: "))
r=int(input("Enter the monthly interest rate: "))
n=int(input("Enter the loan tenure in months: "))
a=1
b=r/100
EMI=p*b*(a+b)**(n)/(a+b)**(n-a)
c=p+EMI
print("Total EMI",EMI)
print("Total amount payable with EMI:",c)
