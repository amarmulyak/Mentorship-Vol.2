import pytest


# Example 1
@pytest.fixture
def fixture_name(request):
    my_dict = {
        "foo": "foo_",
        "bar": "baz",
        "some": "some"
    }
    print(request.param)
    return my_dict[request.param]


@pytest.mark.parametrize('fixture_name', ['foo', 'bar'], indirect=True)
def test_indirect(fixture_name):
    assert fixture_name == 'baz'


# Example 2
@pytest.fixture
def fixt(request):
    return request.param * 3


@pytest.mark.parametrize("fixt", ["a", "b"], indirect=True)
def test_indirect(fixt):
    assert len(fixt) == 3


# Example 3: Apply indirect on particular arguments
@pytest.fixture(scope="function")
def x(request):
    return request.param * 3


@pytest.fixture(scope="function")
def y(request):
    return request.param * 2


@pytest.mark.parametrize("x, y", [("a", "b")], indirect=["x"])
def test_indirect(x, y):
    assert x == "aaa"
    assert y == "b"
