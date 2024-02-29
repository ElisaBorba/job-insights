from src.pre_built.counter import count_ocurrences


def test_counter():

    path = "tests/mocks/mock_counter.csv"
    word = "python"
    expected = 7

    result = count_ocurrences(path, word)
    assert result == expected
