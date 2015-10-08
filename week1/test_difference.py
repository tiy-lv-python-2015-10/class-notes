from generic import difference, reduce_list, add


def test_difference():
    assert difference(2, 1) == 1
    assert difference(1, 2) == 1

def test_reduce_list():
    assert reduce_list([1,2,3,4,5])
    assert type(reduce_list([1,2,3,4,5,6])) == int

def test_add_normal():
    assert add(1, 2) == 3
    assert add(10, 15) == 25

def test_add_negative():
    assert add(-1, 2) == 1