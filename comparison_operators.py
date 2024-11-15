# Example no. 1
#A python program to to see how good the day is.
Temperature = 4
if Temperature > 20: #Boolean expression
    # == denotes equa4l and != denotes not equal
    print("Its a hot day.")
elif Temperature < 20: #Boolean expression
    print("Its a cold day.")
else:
    print("Its a lovely day. ")
    
# Example no. 2
#A python program to know the name length.
name = "ram"
print(len(name))
if len(name) < 3:
    print("Name is too short.")
elif len(name) > 50:
    print("Name is too long.")
else:
    print("Name is valid.")
    
# Example no. 3
#A python program to know your weight in Lbs or Kg.
weight = int(input("Weight: "))
unit = input('(L)bs or (k)g:')
if unit.upper == "L":
    converted = weight * 0.45
    print(f"You are {converted}Kg.")
else:
    converted = weight / 0.45
    print(f"You are {converted}Lbs.")
    
    
