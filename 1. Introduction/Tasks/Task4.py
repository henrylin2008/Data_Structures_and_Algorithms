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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

text_senders = set([text[0] for text in texts])
text_receivers = set([text[1] for text in texts])
call_senders = set([call[0] for call in calls])
call_receivers = set([call[1] for call in calls])

telemarketers = []  # possible telemarketers
for call_sender in call_senders:
    if (call_sender not in call_receivers) and (call_sender not in text_senders) and \
            (call_sender not in text_senders):
        telemarketers.append(call_sender)

telemarketers.sort()    # sorting the telemarketers list in lexicographic order

print("These numbers could be telemarketers: ")
for telemarketer in telemarketers:
    print(telemarketer)
