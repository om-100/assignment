# question number 4
def reverse(str):
    rstr1 = ''
    index = len(str)
    while index > 0:
        rstr1 += str[ index - 1 ]
        index = index - 1
    return rstr1
print(reverse('1234abcd'))

