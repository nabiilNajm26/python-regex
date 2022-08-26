import re 
# search(string yangdicari) : mengembalikan 1 object yang match. 
test_string = 'abc1523rasd41g13rasd2abc[]41;'

pattern = re.compile(r"rasd")

match = pattern.search(test_string)

print(match)


