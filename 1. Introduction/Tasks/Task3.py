"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
area_codes = []

for call in range(len(calls)):
    calling_number = calls[call][0]
    receiving_number = calls[call][1]

    if calling_number.startswith('(080)'):
        if receiving_number.startswith('(0'):   # case 1: fixed lines start with (0
            open_bracket_pos = receiving_number.find('(')
            close_bracket_pos = receiving_number.find(')')
            prefix = receiving_number[open_bracket_pos:close_bracket_pos+1]
            area_codes.append(prefix)

        elif receiving_number.startswith(('7', '8', '9')):    # case 2: mobile numbers start with 7 or 8 or 9
            area_codes.append(receiving_number[0:4])

        elif receiving_number.startswith('140'):    # case 3: telemarketers
            area_codes.append('140')

unique_area_codes = sorted(set(area_codes))
print('The numbers called by people in Bangalore have codes:')
for area_code in unique_area_codes:     # print all unique area codes in lexicographic order
    print(area_code)


# Part B:

call_count = 0
total_calls = len(area_codes)

for call in range(len(calls)):
    calling_number = calls[call][0]
    receiving_number = calls[call][1]

    if calling_number.startswith('(080)'):
        if receiving_number.startswith('(080)'):
            call_count += 1  # increase the count
fixed_line_ratio = round(call_count/total_calls*100, 2)
print(f'{fixed_line_ratio} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
