
from typing import Any, Optional

# THIS CLASS REPRESENTS A SINGLE ELEMENT (NODE) IN THE LINKED LIST
# IT HOLDS A VALUE AND A LINK TO THE NEXT NODE

class Element:
    def __init__(self, value, link=None):
        self.value = value      # THIS IS THE DATA STORED IN THE NODE
        self.link = link        # THIS POINTS TO THE NEXT NODE IN THE LIST


# THIS CLASS DEFINES A CUSTOM SINGLY LINKED LIST
# IT SUPPORTS BASIC OPERATIONS LIKE ADDING, REMOVING, SEARCHING, AND PRINTING NODES

class CustomLinkedList:

    def __init__(self):
        self.start = None  # THE LIST STARTS OUT EMPTY

    # RETURNS TRUE IF THERE ARE NO ELEMENTS IN THE LIST

    def is_empty(self) -> bool:
        return self.start is None

    # ADDS A NEW ELEMENT TO THE FRONT OF THE LIST

    def add_to_front(self, value: Any):

        # CREATE A NEW ELEMENT THAT POINTS TO THE CURRENT START

        new_element = Element(value, self.start)

        # UPDATE THE START TO BE THE NEW ELEMENT

        self.start = new_element
        

    # ADDS A NEW ELEMENT TO THE END OF THE LIST


    def add_to_end(self, value: Any):
        new_element = Element(value)
        if self.is_empty():

            # IF THE LIST IS EMPTY, JUST MAKE THE NEW ELEMENT THE START

            self.start = new_element
        else:
            # OTHERWISE, FIND THE LAST ELEMENT AND LINK IT TO THE NEW ONE

            pointer = self.start
            while pointer.link:
                pointer = pointer.link
            pointer.link = new_element



    # INSERTS A NEW ELEMENT AFTER A SPECIFIED NODE

    def insert_after_node(self, reference: Element, value: Any):
        if reference is None:
            return  # NOTHING TO DO IF THE GIVEN NODE IS NONE
        
        new_element = Element(value, reference.link)
        reference.link = new_element

    # REMOVES A SPECIFIC NODE FROM THE LIST

    def remove_node(self, target: Element) -> bool:
        if self.is_empty():
            return False
        if self.start == target:

            # IF THE TARGET IS THE FIRST ELEMENT, MOVE START TO THE NEXT NODE

            self.start = self.start.link
            return True
        pointer = self.start

        # TRAVERSE THE LIST TO FIND THE NODE BEFORE THE TARGET

        while pointer.link and pointer.link != target:
            pointer = pointer.link
        if pointer.link == target:

            # SKIP OVER THE TARGET NODE TO REMOVE IT

            pointer.link = target.link
            return True
        return False

    # SEARCHES FOR A NODE WITH A SPECIFIC VALUE

    def find(self, value: Any) -> Optional[Element]:
        pointer = self.start

        # CHECK EACH NODE UNTIL THE VALUE IS FOUND OR END IS REACHED

        while pointer:
            if pointer.value == value:
                return pointer
            pointer = pointer.link
        return None

    # COUNTS HOW MANY ELEMENTS ARE CURRENTLY IN THE LIST

    def total_elements(self) -> int:
        count = 0
        pointer = self.start
        while pointer:
            count += 1
            pointer = pointer.link
        return count

    # RETURNS A PYTHON LIST CONTAINING ALL THE VALUES IN THE LINKED LIST

    def convert_to_list(self) -> list:
        elements = []
        pointer = self.start
        while pointer:
            elements.append(pointer.value)
            pointer = pointer.link
        return elements

    # PRINTS THE CONTENTS OF THE LIST IN ORDER
    
    def display(self):
        pointer = self.start
        while pointer:
            print(pointer.value, end=" -> ")
            pointer = pointer.link
        print("None")
