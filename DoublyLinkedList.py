class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #adds a node at the beggining
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    #adds node at the end
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    #add node after given key
    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                next_ = cur.next
                cur.next = new_node
                new_node.next = next_
                new_node.prev = cur
                next_.prev = new_node
                return
            cur = cur.next

    #add a node before the given key
    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node =Node(data)
                prev_ = cur.prev
                prev_.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev_
                return
            cur = cur.next

    #delete a node having data "key"
    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                #case 1, if a list has only one node
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                #case 2: A-> B "delete A" multiple nodes and key is head
                else:
                    next_ = cur.next
                    cur.next = None
                    next_.prev = None
                    cur = None
                    self.head = next_
                    return
            elif cur.data == key:
                #case 3: cur.next is not None, Node except last None
                if cur.next:
                    next_ = cur.next
                    prev_ = cur.prev
                    prev_.next = next_
                    next_.prev = prev_
                    cur.prev = None
                    cur.next = None
                    cur = None
                    return
                #case 4: cur.next is none i.e last node
                else:
                    prev_ = cur.prev
                    prev_.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    #delete a node with providednode
    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                #case 1, if a list has only one node
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                #case 2: A-> B "delete A" multiple nodes and key is head
                else:
                    next_ = cur.next
                    cur.next = None
                    next_.prev = None
                    cur = None
                    self.head = next_
                    return
            elif cur == node:
                #case 3: cur.next is not None, Node except last None
                if cur.next:
                    next_ = cur.next
                    prev_ = cur.prev
                    prev_.next = next_
                    next_.prev = prev_
                    cur.prev = None
                    cur.next = None
                    cur = None
                    return
                #case 4: cur.next is none i.e last node
                else:
                    prev_ = cur.prev
                    prev_.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    #reverses the list
    def reverse(self):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            #to next node because next and prev are swapped
            cur = cur.prev
        if temp:
            self.head = temp.prev

    #Remove the node with duplicate data
    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                next_ = cur.next
                self.delete_node(cur)
                cur = next_

    #makes pair to form the given sum
    #Example
    # 1-> 2 -> 3 -> 4 -> 5
    #(1,2), (1,3), (1,4), (1,5)
    #(2,3), (2,4), (2,5)
    #(3,4), (3,5)
    #(4,5)
    # no duplicate pairs, (1,3) and (3,1) are same so only one pair is taked
    def pairs_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs

    #prints the data of whole list
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
