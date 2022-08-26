import re 
# match() : jika sama di awal , hanya ngembaliin 1 object. Yang dicek hanya awal2 , klo ga sama, hasilnya None
test_string = 'adsaasd4123a;][ads]rsfa14fy4'

pattern = re.compile(r"ads") # Output : ketemu, karena ads ada di awal string
pattern = re.compile(r"aas") # Output : None , karena aas tidak ada di awal2 string

match = pattern.match(test_string)

print(match)