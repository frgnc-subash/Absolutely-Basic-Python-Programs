#Example no. 1
# Take user input
number = 1 

# Condition of the while loop
while number <= 5 :  
    print("*" * number)
    # Increment the value of the variable "number by 1"
    number = number+1
print('done')

#Example no. 2
#Guess the number from 1-10
secret = 7
i = 0
while i < 3:
    guess = int(input('Guess:'))
    i+=1
    if guess == secret:
        print('Congratulations! You guessed the number.')
        break
else:
    print('Sorry, you have not guessed the number. The secret number was', secret)
    

    
    