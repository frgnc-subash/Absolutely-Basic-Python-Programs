print("A python program to find the Simple Interest.")
principal = float(input('Enter the principal amount:'))

rate = float(input('Enter the annual interest rate: '))

time = float(input('Enter the time period in years: '))

simple_interest = (principal * rate * time) / 100
print(simple_interest)
