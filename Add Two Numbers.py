class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_to_reversed_array(head):
    stack = []
    currentNode = head
    while currentNode:
        stack.append(currentNode.data)
        currentNode = currentNode.next
    reversed_array = []
    while stack:
        reversed_array.append(stack.pop())
    return reversed_array

def addTwoNumbers(l1, l2):
    Lar1 = linked_list_to_reversed_array(l1)
    Lar2 = linked_list_to_reversed_array(l2)
    
    
    max_len = max(len(Lar1), len(Lar2))
    
    
    while len(Lar1) < max_len:
        Lar1.append(0)
    while len(Lar2) < max_len:
        Lar2.append(0)
    
    
    Sarray = []
    carry = 0
    for i in range(max_len):
        total = Lar1[i] + Lar2[i] + carry
        Sarray.append(total % 10)
        carry = total // 10
    
    
    if carry > 0:
        Sarray.append(carry)
    
    
    head = None
    tail = None
    for num in Sarray:
        new_node = Node(num)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    
    return head

# Example usage:
# Creating two linked lists: 342 (2 -> 4 -> 3) and 465 (5 -> 6 -> 4)
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

# Add the two numbers
result = addTwoNumbers(l1, l2)

# Print the result
current = result
while current:
    print(current.data, end=" -> " if current.next else "")
    current = current.next
# Output: 7 -> 0 -> 8 (807)
