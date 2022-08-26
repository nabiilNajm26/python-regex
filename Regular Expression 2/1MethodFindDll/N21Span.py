import re 
# Mengembalkan posisi string yang ditemukan sama/ match. Posisi seperti index pada list
test_string = 'abc1523rasd41g132abc[]41;'

pattern = re.compile(r"abc")

matches = pattern.finditer(test_string)

for match in matches : 
    print(match.span(), match.start(), match.end())
    print(match.group())


# match.start() : mengembalikan index awal dari string yang match

# match.end() : mengembalikan index awal dari string yang match

# match.group() : mengembalikan string dari object hasil finditer