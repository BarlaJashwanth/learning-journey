"""
Simple Intrest = (P * R * T) / 100
P = Pricipal amount
R = rate of intrest
T = Time duration of intrest
"""
principal = float(input("Enter the principal amount: "))
Rate = float(input("Enter the rate of intrest: "))
Time = float(input("Enter the time duration of intrest: "))
Simple_Intrest = (principal * Rate * Time) / 100
print("Simple Intrest is", Simple_Intrest )
