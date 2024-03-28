from heap5 import Heap5, HeapEmptyError
import pytest

def test_heap_creation():
    heap = Heap5([1, 3, 10, 2])
    assert heap.get_top() == 10

def test_heap_insert():
    heap = Heap5()
    heap.insert(5)
    heap.insert(11)
    heap.insert(2)
    heap.insert(-1)
    assert heap.get_top() == 11

def test_heap_delete_top():
    heap = Heap5()
    heap.insert(5)
    heap.insert(11)
    heap.insert(2)
    heap.insert(-1)
    assert heap.delete_top() == 11
    assert heap.delete_top() == 5
    assert heap.delete_top() == 2
    assert heap.delete_top() == -1

def test_heap_delete_top_too_many():
    heap = Heap5()
    heap.insert(5)
    heap.delete_top()
    with pytest.raises(HeapEmptyError):
        heap.delete_top()