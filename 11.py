#Question number 11
def word_count(str):
    count = dict()
    words = str.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

print( word_count('welcome to  Insight Workshop Academy '))