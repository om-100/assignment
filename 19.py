#Question number 19
def min(num):
    num1 = num[0]
    for x in num:
        if x < num1:
            num1 = x
    return num1
print(min([1,2,3,4,0]))