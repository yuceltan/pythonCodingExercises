a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
c = int(input("Enter your third number"))

if b < a and c < a:
    print("Bigest number is: a")
elif a < b and c < b:
    print("Bigest number is: b")
elif a < c and b < c:
    print("Bigest number is: c")

