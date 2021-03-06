# Problem Statement
# Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the
# brackets balanced.
#
# For example:
#
# For input_string = "}}}}, the number of reversals required is 2.
# For input_string = "}{}}, the number of reversals required is 1.
# If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.
class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of bracket reversals needed
    """
    if len(input_string) % 2 == 1:  # if the len of input_string is odd
        return -1

    stack = Stack()
    count = 0
    for bracket in input_string:
        """automatically remove the balanced brackets that are in the string if they are next to each other and only
         keep in the stack the unbalanced brackets."""
        if stack.is_empty():   # if stack is empty, then add the string to the stack
            stack.push(bracket)
        else:
            top = stack.top()   # top of the stack
            if top != bracket:  # if current bracket is not the same as the top of the stack
                if top == '{':  # when top of the stack == '{' and current bracket == '}'
                    stack.pop()  # pop the top out and continue; ex: top of stack "{", and current bracket == "}"
                    continue
            stack.push(bracket)  # add the bracket to the stack if current bracket == top of the stack

    ls = list()
    while not stack.is_empty():
        """pop top 2 items and compare them, then add the number of time the reverse needed to the count variable"""
        first = stack.pop()     # top item
        second = stack.pop()    # second top item
        ls.append(first)
        ls.append(second)
        if first == "}" and second == "}":  # only need to reverse one
            count += 1
        elif first == "{" and second == "}":    # need to reverse both two, as they are in a different order
            count += 2
        elif first == "{" and second == "{":    # only need to reverse one
            count += 1
    return count


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


# Test 1:
# test_case_1 = ["}}}}", 2]
# test_function(test_case_1)  # Pass


# Test 2:
# test_case_2 = ["}}{{", 2]
# test_function(test_case_2)    # Pass


# Test 3:
# test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
# test_function(test_case_1)    # Pass


# Test 4:
# test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
# test_function(test_case_2)    # Pass

# Test 5:
# test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
# test_function(test_case_3)    # Pass




