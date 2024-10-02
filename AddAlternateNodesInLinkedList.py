class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev and current one step forward
        current = next_node
    
    head = prev  # The new head of the reversed list
    return head
def AddAlternateNodes(head):
    head=reverse_linked_list(head)
    curr=head
    s1=head
    s2=head.next
    while s1 and s1.next and s1.next.next:
        s1.data+=s1.next.next.data
        s1=s1.next.next
    while s2 and s2.next and s2.next.next:
        s2.data+=s2.next.next.data
        s2=s2.next.next
    curr=reverse_linked_list(curr)
    return curr
        
    

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

# Example usage
values = [2,1,9,2]
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

# Call your function (which you'll implement)
AddAlternateNodes(head)

print("Modified Linked List:")
print_linked_list(head)
