# Question number 20
def a(str):
    count = 0
    for x in str:
        if len(x) >1 and x[0] == x[-1]:
            count += 1
    return count
print(a(['aba', 'sfsd','121', 'coc']))
