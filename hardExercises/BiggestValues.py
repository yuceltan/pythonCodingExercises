"""Example 2:
Given a list of numbers define a function to find the 2 biggest values.
- By using max()
- Without using max()
"""


"""def withMax(a):
    maxValueOne = max(a)
    index = a.index(maxValueOne)
    a.pop(index)
    maxValueTwo = max(a)

    return print("First max value is: {} Second Max Value is : {}".format(maxValueOne,maxValueTwo))

"""
listExample = [1, 2, 3, 4, 5, 6]

"""withMax(listExample)"""

def withoutMax(a):
    max = a[0]
    maxTwo = a[0]


    for x in a:
        if x > max:
            max = x
            
            if x > maxTwo:
                index = a.index(max)
                a.pop(index)
                maxTwo = x
    print("First Max Value:", max,maxTwo)




withoutMax(listExample)




