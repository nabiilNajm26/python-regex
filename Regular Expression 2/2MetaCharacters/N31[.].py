import re 
# . = Any character (except newline character) "he..o."
test_string = 'abc1523rasd41g132abc[]41;.'

pattern = re.compile(r".") # Output : semua karakter kecuali newline
pattern = re.compile(r"\.") # Output : .

matches = pattern.finditer(test_string)

for match in matches : 
    # print(match.span(), match.start(), match.end())
    print(match.group())