firstTerm = float(input("Enter your first exam grade"))
secondTerm = float(input("Enter your second exam grade"))
final = float(input("Enter your final exam grade"))


rateFirstTerm = (firstTerm *30) /100
rateSecondTerm = (secondTerm *30) /100
rateFinalTerm = (final*40)/100

print(rateFirstTerm)
print(rateSecondTerm)
print(rateFinalTerm)

sumTerms= rateFirstTerm +rateSecondTerm +rateFinalTerm

if sumTerms >= 90 :
	print("Your grade is AA")
elif sumTerms >= 85:
	print("Your grade is BA")
elif sumTerms >= 80:
	print("Your grade is BB")
elif sumTerms >= 75:
	print("Your grade is CB")
elif sumTerms >= 70:
	print("Your grade is CC")
elif sumTerms >= 65:
	print("Your grade is DC")
elif sumTerms >= 60:
	print("Your grade is DD")
elif sumTerms >= 55:
	print("Your grade is FD")
elif sumTerms >= 50:
	print("Your grade is FF")
elif sumTerms <=49:
    print("idiot")