"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

max_call_time = 0
max_phone_num = None
phone_dict = defaultdict(int)

for call in calls:
    duration = int(call[3])

    # adding phone numbers along with the call duration into phone_dict
    if call[0] not in phone_dict:
        phone_dict[call[0]] = duration
    else:
        phone_dict[call[0]] += duration
    if call[1] not in phone_dict:
        phone_dict[call[1]] = duration
    else:
        phone_dict[call[1]] += duration

    # finding the longest call time and its phone number
    if phone_dict[call[0]] > max_call_time:
        max_call_time = phone_dict[call[0]]
        max_phone_num = call[0]
    if phone_dict[call[1]] > max_call_time:
        max_call_time = phone_dict[call[1]]
        max_phone_num = call[1]

print(f"{max_phone_num} spent the longest time, {max_call_time} seconds, on the phone during September 2016.")
