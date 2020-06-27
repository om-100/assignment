# Question nummber 5

def adding(str):
  length = len(str)

  if length > 2:
    if str[3:] == 'ing':
      str = str + 'ly'
    else:
      str = str + 'ing'

  return str
print(adding('ab'))
print(adding('abc'))
print(adding('string'))
