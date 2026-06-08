s1 = "python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))

#concatenation of strings
language = "python"
version = " 3.13.3"
print(language + version)

# * repetition opearator in strings
s2 = "python "
print(s2 * 3)

# membership operation
# 01] in
# print("python in" s1) wont works rmember 'in' operation should be outside the "
print("python" in s1)
print(" " in s1)
print("k" in s1)
# 02] not in
# same work functions as 'in'
print("python" not in s1)
print(" " not in s1)
print("k" not in s1)
## 'in' and 'no in' are case sensetive

# Comparision of strings
print("python" == "python")
print("python " == "python")

# Removing spaces from string - strip() remove starting and ending spaces not in between strings
s3 = " python is cool "
s4 = s3.strip()
s5 = "python is cool"
print(s4)
print(s3.strip() == s5)

# replace()
s6 = "we are learning python"
print(s6)
print(s6.replace("python","java"))
print(s6.replace("e","E"))
print(s6.replace("e","E",1))
print(s6.replace("e","E",2))
# not changing anything under existing stringits just creating new string

# count()
# counting substrings from a string
# string.count(substring)
s7 = "don't trouble the trouble if you trouble the trouble trouble trouble's you"
s8 = "trouble"
print(s7.count(s8))
print(f"occurrences of {s8} is {s7.count(s8)}")
# same also apllies for alphabets and spaces too not only for words

# changing case of a string
# upper(), lower(), title(), capitilize()
s9 = "Python"
print(s9.upper())
print(s9.lower())
s10 = ('python3.13 is fun to learn')
print(s10.upper())
print(s10.title())
print(s10.capitalize())

#startswith()
# string.startswith("substring")
s11 = "India is great country"
print(s11.startswith("India"))
print(s11.startswith("india"))
print(s11.startswith("great country"))
#endswith()
# string.endswith("substring")
print(s11.endswith("India"))
print(s11.endswith("india"))
print(s11.endswith("great country"))
print(s11.endswith("Great country"))