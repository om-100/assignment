#QUESTION NUMBER 8
def remove(str , n):
    str1 = str[:n]
    str2 = str[n+1:]
    return str1 + str2
print(remove('hello',4))

