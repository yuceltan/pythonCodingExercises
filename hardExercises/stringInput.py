userInput = input("Enter your string:")
stringList = []
for i in userInput:
    stringList.append(i)

    for j in stringList:

        if j.isupper() and 20 > len(stringList) > 10:
            print("")
print(userInput)

