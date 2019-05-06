class Stack:
    def __init__(self):
        self.items =[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is Empty")

    def get_stack(self):
        return self.items
        
    def size(self):
        return len(self.items)

    #loop through the string and push contents
    #character by character onto stack
    def reverse_string(stack, input_str):
        for i in range(len(input_str)):
            stack.push(input_str[i])

        rev_str = ""
        while not stack.is_empty():
            rev_str += stack.pop()

        return rev_str
