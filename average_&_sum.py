print('A python program to find the average and sum till the nth term of natural numbers.')
#Enter the number of natural numbers you want to add.
n = float(input("Enter the nth term: "))
sum = (n*(n+1)) // 2 #Adding to the nth term.
avg = sum / 2  #Average
#Display
print(f"{sum} is the sum to the nth term of natural numers.")
print(f"{avg} is the sum to the nth term.")
