import re 

test_string = 'aabcsfasfjadoj14ABC2;abc'

pattern = re.compile(r"aabc")

# finditer(string text) : ngumpulin object
matches_finditer = pattern.finditer(test_string) # Whole object

# findall() : just string
matches_findall = pattern.findall(test_string) 

# match() : jika sama di awal , hanya ngembaliin 1. Yang dicek hanya awal2 , klo ga sama, hasilnya None
match = pattern.match(test_string)


# search(string yangdicari) : mengembalikan 1 object yang match. 
match_search = pattern.search(r"abc") 

# matches = re.finditer(r"abc", test_string)

# match(), search(), findall()
# for match in matches_finditer : 
#     print(match) 

print(match)
print(match_search)
# r = raw string, kalo diprint bakal munculin apa adanya di string

a = r"\n\tHello"

print(a)