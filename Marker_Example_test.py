import pytest

abc = "Hi1"


@pytest.fixture()
def hello():
    return "hello"


@pytest.mark.hello
def test_hello(hello):
    assert hello == "hello"

@pytest.mark.skipif('abc == "Hi"')
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.skip(reason="This test is not ready yet")
def test_failing():
    assert (1, 3, 3) == (1, 2, 3)


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        raise (TypeError)


@pytest.mark.smoke
def test_list_raises1():
    """list() should raise an exception with wrong type param."""
    assert True


@pytest.mark.smoke
@pytest.mark.win32
def test_list_raises2():
    """list() should raise an exception with wrong type param."""
    assert True


# pytest -m "smoke or win32" marker_examples_test.py
# pytest -m "smoke and win32" marker_examples_test.py
# pytest -m "smoke" marker_examples_test.py

# pytest -m "smoke and not win32" marker_examples_test.py


@pytest.mark.xfail(reason="This test is a negative test scenario")
def testthis_should_fail():
    assert True
