# question number 1
def max1(x,y):
    if x > y:
        return x
    return y
def max2(x,y,z):
    return max1(x,max1(y,z))
print(max2(3,4,5))