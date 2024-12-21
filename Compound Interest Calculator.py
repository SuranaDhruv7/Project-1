print("Compound Interest Calculator \n")
p=int(input("Enter the principle amount: "))
r=int(input("Enter the monthly rate amount: "))
n=int(input("Enter the number of times interest applied per time period: "))
t=int(input("Enter the number of time periods elapsed: "))
a = 1
b = r/100
c =p*(a+b/n)**(n*t)
d = c - p
print("The payable amount: ",c)
print("The compound interest: ",d)

