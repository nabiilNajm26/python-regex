import re 
# finditer(string text) : ngumpulin object yang stringnya sama kek pattern
test_string = 'abc1523rasd41g132abc[]41;'

pattern = re.compile(r"abc")

matches = pattern.finditer(test_string)

for match in matches : 
    print(match)

