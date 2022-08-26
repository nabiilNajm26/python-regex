import re 
# findall(string text) : ngumpulin object yang stringnya sama kek pattern
test_string = 'abc1523rasdabc41g132abc[]41;'

pattern = re.compile(r"abc")
# pattern = r"abc"

matches = pattern.findall(test_string)

# matches = re.findall(pattern, test_string)

for match in matches : 
    print(match)

print(matches)