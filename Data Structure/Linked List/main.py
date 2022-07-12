'''
Linked List has two main benifits over array

1. You don't need to pre-allocate space
2. Insertion is easier
'''


class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        # now we get the last itr
        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        ''' here the head only removed we had to remove other data but python will remove the other data
            since it no longer needed (python garbage collection)
        '''
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head

        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print_forward(self):
        if self.head == None:
            print('Linked List is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += '{} --> '.format(itr.data)
            itr = itr.next
        llstr += 'None'
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = 'None'
        while itr:
            llstr += '<-- {} '.format(itr.data)
            itr = itr.prev

        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(3)
    ll.insert_at_end(6)
    ll.insert_at_end(9)
    ll.insert_values([1, 2, 3, 4, 5])
    print(ll.get_length())
    ll.remove_at(2)
    ll.insert_at(3, 120)
    ll.insert_after_value(120, 'yoyo')
    ll.remove_by_value('yoyo')
    ll.print_forward()
    ll.print_backward()

# warp notion
