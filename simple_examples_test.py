
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

# execute the test from terminal using
# >pytest simple_examples_test.py
# you will see passed tests with green dots.
# also if everything is passed then you will see green line with number
# of passed tests and time it took for execution

def test_passing1():
    assert (1, 2, 3) == (1, 2, 3)

# failing test
def test_failing():
    assert (1, 2, 3) == (3, 2, 3)

def test_failing1():
    assert (1, 2, 3) == (3, 2, 3)

def test_failing2():
    assert (1, 2, 3) == (3, 2, 3)

# terminal will show you all the passed and fail tests
# along with the exact reason for failure


# running one specific test
# > pytest simple_examples_test.py::test_failing
# > pytest -q simple_examples_test.py   # quiet reporting mode with minimum info

# running pytest to check what will happen
# > pytest simple_examples_test.py --collect-only
# above will not execute any tests
