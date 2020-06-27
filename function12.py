# question number 12
def a(num):
    return lambda x : x * num
result = a(2)
print("the double will be: ", result(4))