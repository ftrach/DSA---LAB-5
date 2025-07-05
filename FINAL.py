# CLASS FOR A SINGLE NODE IN THE SORTED DOUBLY LINKED LIST


class Node:
    def __init__(self, item):


        self.item_value = item  # STORES THE VALUE OF THE NODE


        self.next_node = None   # POINTER TO THE NEXT NODE


        self.prev_node = None   # POINTER TO THE PREVIOUS NODE



# CLASS FOR THE SORTED DOUBLY LINKED LIST


class SortedLinkedList:
    def __init__(self):
        self.head_node = None  # START OF THE LINKED LIST


        self.count = 0         # TRACK NUMBER OF ELEMENTS IN THE LIST



    # INSERTS AN ELEMENT WHILE MAINTAINING SORTED ORDER


    def insert(self, new_item):
        new_node = Node(new_item)
        if self.head_node is None:
            self.head_node = new_node
        elif new_item < self.head_node.item_value:
            new_node.next_node = self.head_node
            self.head_node.prev_node = new_node
            self.head_node = new_node
        else:
            current = self.head_node
            while current.next_node and current.next_node.item_value < new_item:
                current = current.next_node
            new_node.next_node = current.next_node
            new_node.prev_node = current
            if current.next_node:
                current.next_node.prev_node = new_node
            current.next_node = new_node


        self.count += 1  # INCREMENT NODE COUNT


    # REMOVES A NODE WITH THE GIVEN VALUE, RETURNS TRUE IF REMOVED


    def remove(self, target_item):
        current = self.head_node
        while current:
            if current.item_value == target_item:
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                else:
                    self.head_node = current.next_node
                if current.next_node:
                    current.next_node.prev_node = current.prev_node


                self.count -= 1  # DECREMENT NODE COUNT


                return True
            current = current.next_node


        return False  # RETURN FALSE IF NOT FOUND

    

    # CHECKS IF A VALUE IS PRESENT IN THE LIST



    def is_present(self, query_item):
        current = self.head_node
        while current:
            if current.item_value == query_item:
                return True
            current = current.next_node
        return False


    # RETURNS THE LENGTH OF THE LIST


    def __len__(self):
        return self.count


    # ITERATOR TO LOOP THROUGH VALUES IN THE LIST


    def __iter__(self):
        current = self.head_node
        while current:
            yield current.item_value
            current = current.next_node



# MAIN PROGRAM FOR TESTING



if __name__ == "__main__":
    test_list = SortedLinkedList()
    test_list.insert(10)
    test_list.insert(5)
    test_list.insert(7)
    test_list.insert(1)

    print("Current List:")
    for val in test_list:
        print(val)

    print("Removing 7:", test_list.remove(7))
    print("Is 5 present?", test_list.is_present(5))
    print("Length of list:", len(test_list))
