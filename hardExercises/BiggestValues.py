"""Example 2:
Given a list of numbers define a function to find the 2 biggest values.
- By using max()
- Without using max()
"""


def withMax(a):
    maxValue = max(a)
    return maxValue


listExample = [1, 2, 3, 4, 5, 6]
print(withMax(listExample))


def withoutMax(a):
    max = a[0]


    for x in a:
        if x > max:
            max = x
    return print(max)

withoutMax(listExample)




