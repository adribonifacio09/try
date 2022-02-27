first = input("First Name: ")
last = input("Last Name: ")
full = (first + " " + last)
bud = input("Amount: P")
budget = float(bud)

print(" ")

print("My name is " + full + ".")
print(first + " is my first name, and " + last + " is my last name. I have P" + bud + " as my budget.")

print(" ")

if budget > 12 :
    print("I'll buy a new pencil.")
else:
    print("I'll buy next time.")