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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def main():
    phone_number = []

    for text in range(len(texts)):
        for number in range(2):
            phone_number.append(texts[text][number])  # retrieving sending/receiving phone numbers from texts file

    for call in range(len(calls)):
        for number in range(2):
            phone_number.append(calls[call][number])  # retrieving calling/receiving phone numbers from calls file

    unique_numbers = len(set(phone_number))
    print(f'There are {unique_numbers} different telephone phone_number in the records.')


if __name__ == '__main__':
    main()
