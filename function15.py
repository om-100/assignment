# question number 15
num = [1,2,3,4,5,6,7,8,9]
print(num)
even = list(filter(lambda x: x % 2 == 0, num))
print(even)
odd = list(filter(lambda x: x%2 != 0,num))
print(odd)