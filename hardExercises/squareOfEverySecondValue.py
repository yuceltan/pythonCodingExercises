"""Given a list of numbers square every second value.
- Without list comprehension
- With list comprehension (optional)
Example: [ 1, 2, 3, 4, 5, 6 ] —> [ 1, 4, 3, 16, 5, 36 """

squareList = [ 1, 2, 3, 4, 5, 6 ]
#list comprehension
def squared(a):
  for i in a:
      if i%2==0:
         for j in len(a):
             a




print(squared(squareList))