# Create a Node class with value and next attributes
# Use the class to create the head node with the value 2
# Create and link a second node containing the value 1
# Try printing the values (1 and 2) on the nodes you created (to make sure that you can access them!)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
head.next = Node(1)

print(head.value)
print(head.next.value)

# Step 3. Write a function that loops through the nodes of the list and prints all of the values
def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


print_linked_list(head)     # 2, 1, 4, 3, 5


# Step 4. See if you can write the code for the create_linked_list function below
# -The function should take a Python list of values as input and return the head of a linked list that has those values
def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(value)

    return head

