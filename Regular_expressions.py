import re

mystr = """Tata limited
Dr. Dravid, Landsman, Executive Director
18, Grosvenor Palace
London SWIX 7HSC
phone :  +44 (20) 7235 8281
Fax : +44 (20) 7235 8727
Email : tata@tata.com
Directions : View map

Tata Sons North America
1700 North Moore ST, Suite 1520
Arlington, VA 22209 - 1911
USA
Phone : +1 (703) 243 9787
Fax : +1 (703) 243 9791
66 - 66
455 - 4545
Email : northamerica@tata.com
Websites : www.northamerica@tata.com
Directions : View map pass
Harry bhai lekin
bahut hi badhiya aadmi haiiiiiiiiiiiii
"""

# patt = re.compile(r'pass')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iii$')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ii){2}')
# patt = re.compile(r'ai{1} | Fax')

# Special sequences
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
patt = re.compile(r'\d{5} - \d{4}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)

