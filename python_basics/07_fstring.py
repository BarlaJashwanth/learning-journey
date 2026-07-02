name = "Jashwanth"
age = 20
language = "python"
hours = 3
# Jashwanth is 20 years old.
print(name,"is",age,"years old.")
# Jashwanth is 20 years old. He studies python 3 hours a day
print(name,"is",age,"years old. He studies",language,"for",hours,"hours a day.")
# using f-strings
print("{name} is {age} years old. He studies {language} for {hours} hours a day.")
print(f"{name} is {age} years old. He studies {language} for {hours} hours a day.")
# f is mandatory for fstring...

s1 = 95
s2 = 96
s3 = 97

print(f"{name} scored {s1+s2+s3} marks in total")

percent = (s1+s2+s3)/3
print(f"{name} scored {percent}%")
