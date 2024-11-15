# Example no. 1    
print("To find the greater number among 2 numbers. ")
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
if a>b: 
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")
    
# Example no. 2
print("To find greater number among 3 numbers.3")
x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
z = float(input("Enter a number: "))

if x >= y and x >= z:
    print(f"{x} is the largest number.")
elif y >= z and y >= x:
    print(f"{y} is the largest number.")
else:
    print(f"{z} is the largest number.")