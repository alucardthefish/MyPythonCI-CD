from separating_logic import most_common_word, most_common_word_in_web_page


def test_most_common_word():
    assert most_common_word(["a", "b", "c"], "abbbcc") == "b", "most_common_word with unique answer"

def test_most_common_word_empty_candidate():
    from pytest import raises
    with raises(Exception):
        most_common_word([], "abc")

def test_most_common_ambiguous_result():
    assert most_common_word(["a", "b", "c"], "ab") in ("a", "b"), "there might be a tie"

def test_with_test_double():
    class TestResponse():
        text = "a bbb c"

    class TestUserAgent():
        def get(self, url):
            self.url = url
            return TestResponse()

    test_ua = TestUserAgent()
    result = most_common_word_in_web_page(
        ["a", "b", "c"],
        "https://python.org/",
        user_agent=test_ua
    )

    assert result == "b", "most_common_word_in_web_page tested with test double"
    assert test_ua.url == "https://python.org/"


def test_with_test_mock():
    from unittest.mock import Mock
    mock_requests = Mock()
    mock_requests.get.return_value.text = "aa bbb c"

    result = most_common_word_in_web_page(
        ["a", "b", "c"],
        "https://python.org/",
        user_agent=mock_requests
    )

    assert result == "b", "most_common_word_in_web_page tested with test mock"
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] == "https://python.org/", "Called with right URL"
