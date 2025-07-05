# IMPORT THE SORTED LINKED LIST CLASS FROM FINAL.PY

from FINAL import SortedLinkedList



# TEST INSERTION OF ELEMENTS AND CHECK IF LENGTH AND ORDER ARE CORRECT

def test_insert_and_len():

    slist = SortedLinkedList()         # CREATE A NEW SORTED LINKED LIST INSTANCE

    slist.insert(3)                    # INSERT ELEMENT 3

    slist.insert(1)                    # INSERT ELEMENT 1

    slist.insert(2)                    # INSERT ELEMENT 2

    assert len(slist) == 3             # VERIFY THE LENGTH OF THE LIST IS 3

    assert list(slist) == [1, 2, 3]    # VERIFY THE ELEMENTS ARE IN SORTED ORDER



# TEST REMOVAL FUNCTIONALITY

def test_remove():

    slist = SortedLinkedList()         # CREATE A NEW SORTED LINKED LIST INSTANCE

    slist.insert(5)                    # INSERT ELEMENT 5

    slist.insert(6)                    # INSERT ELEMENT 6

    assert slist.remove(5) == True     # VERIFY REMOVAL OF EXISTING ELEMENT RETURNS TRUE

    assert slist.remove(7) == False    # VERIFY REMOVAL OF NON-EXISTENT ELEMENT RETURNS FALSE

