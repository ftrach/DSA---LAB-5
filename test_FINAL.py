
import pytest
from FINAL import CustomLinkedList, Element



# CHECKS THAT A NEW LIST IS EMPTY

def test_empty_list():
    test_list = CustomLinkedList()
    assert test_list.is_empty()
    assert test_list.total_elements() == 0
    assert test_list.convert_to_list() == []

# TEST ADDING ONE ITEM TO THE FRONT

def test_add_to_front():
    test_list = CustomLinkedList()
    test_list.add_to_front(10)
    assert test_list.start.value == 10
    assert test_list.total_elements() == 1

# TEST ADDING TWO ITEMS TO THE END

def test_add_to_end():
    test_list = CustomLinkedList()
    test_list.add_to_end(20)
    test_list.add_to_end(30)
    assert test_list.convert_to_list() == [20, 30]

# TEST INSERTING AN ELEMENT IN THE MIDDLE

def test_insert_after_node():
    test_list = CustomLinkedList()
    test_list.add_to_end(1)
    test_list.add_to_end(2)
    ref_node = test_list.find(1)
    test_list.insert_after_node(ref_node, 1.5)
    assert test_list.convert_to_list() == [1, 1.5, 2]

# TEST REMOVING AN EXISTING NODE

def test_remove_node():
    test_list = CustomLinkedList()
    test_list.add_to_end(5)
    node_to_remove = test_list.find(5)
    assert test_list.remove_node(node_to_remove) is True
    assert test_list.convert_to_list() == []

# TEST FINDING A NODE BY VALUE

def test_find():
    test_list = CustomLinkedList()
    test_list.add_to_end(100)
    test_list.add_to_end(200)
    result_node = test_list.find(200)
    assert result_node is not None
    assert result_node.value == 200
