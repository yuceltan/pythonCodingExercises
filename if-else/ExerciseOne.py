height = float(input("Enter your height"))
weight = float(input("Enter your weight"))

index = weight / height ** 2

if index < 18.5:
    print("you are thiny")
elif index >= 18.5 and index < 25:
    print("You are Normal")
elif index >= 25 and index < 30:
    print("over weight")

elif index < 30:
    print("You are fat")

else:
    print("Error")