"""
we have the following dictionary containing details

user = {
"user_name": "my_user",
"password" : "test@123",
"email" : "my_user@gmail.com",
"address": "ABC road",
"country": "India"
}
Delete the sensitive information from the dictionary present in list
sensitive_info = ["password,address"]
"""


user = {
"user_name": "my_user",
"password" : "test@123",
"email" : "my_user@gmail.com",
"address": "ABC road",
"country": "India"
}
sensitive_info = ["password","address"]

for i in sensitive_info:
    user.pop(i)

print(user)


# here candies are only 10 so write code 10 times candies given if once candies completed then sorry
candies = 10
while candies > 0:  ### this is loop
    print("candies given")
    candies = candies - 1
    if candies == 0:   ### this is conditional statement
        break
print("sorry")

print("for loop based")

candies = 11

for i in range(1,candies):
    print("candies given")
print("sorry")

"""
guess the number game 
"""
print("Hi welcome")
print("you have 10 chances for finding the correct number")
print("number lies between 1 to 50")

secret_number = 12

attempts = 10

while attempts <= 10:
    user_number = int(input("Please enter your number: "))
    if user_number == secret_number:
        print("you guessed correctly")
        break
    elif user_number > secret_number:
        print("you guessed too high")
        attempts = attempts - 1
        print("remaining", attempts, "attempts are left")
    elif user_number < secret_number:
        print("you guessed too low")
        attempts = attempts - 1
        print("remaining", attempts,"attempts are left")
    elif user_number != secret_number:
        print("enter some valid number")
        attempts = attempts + 1
        print("remaining", attempts, "attempts are left")
    if attempts == 0:
        print("game over")
        break






























