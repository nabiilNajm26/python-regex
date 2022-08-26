import re 
# ^ Starts with "^hello"
# $ Ends with "world$"
test_string = '123abc1523ra123sd41g132abc[]41;.'

pattern1 = re.compile(r"^123") # Output : 123
pattern2 = re.compile(r"41;.$") # Output : 41;.

matches1 = pattern1.finditer(test_string)
matches2 = pattern2.finditer(test_string)

for match in matches1 : 
    # print(match.span(), match.start(), match.end())
    print(match.group())


for match in matches2 : 
    # print(match.span(), match.start(), match.end())
    print(match.group())