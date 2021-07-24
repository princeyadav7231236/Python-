import re

# Task ----> Give a string with a lot of indian numbers starting from +91
string_2 = """
Phone number 1 :  +91 7408143680
Phone number 1 :  +91 8303434203
Phone number 1 :  +91 8175018176
Phone number 1 :  +91 9935453538
Phone number 1 :  +91 8574030374
Phone number 1 :  +91 9935619448
Phone number 1 :  +91 8896049100
"""
var1 = re.compile(r"\d{10}")

var2_iter = var1.finditer(string_2)
for i in var2_iter:
    print(i)