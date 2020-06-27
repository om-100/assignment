#Question number 18
def max(num):
    num1 = num[0]
    for x in num:
        if x > num1:
            num1 = x
    return num1
print(max([1,2,33,4,5,6]))