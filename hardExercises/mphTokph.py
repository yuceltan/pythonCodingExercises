"""Example 1:
Define a function that converts a given speed from miles per hour (mph) to kilometers per hour
(kph). Look for the formula online.
"""


def converter(a):
    kph = a * 1.60934
    return kph


mph = 1300
result = converter(mph)
print(result)
