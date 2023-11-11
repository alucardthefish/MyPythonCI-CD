from unittest.mock import Mock, patch

from webcount.functions import most_common_word_in_web_page


def test_with_patch():
    mocky_requests = Mock()
    mocky_requests.get.return_value.text = "aa bbb c"
    with patch("webcount.functions.requests", mocky_requests):
        result = most_common_word_in_web_page(
            ["a", "b", "c"],
            "https://python.org/",
        )
    assert result == "b", "most_common_word_in_web_page tested with test patch"
    assert mocky_requests.get.call_count == 1
    assert mocky_requests.get.call_args[0][0] == "https://python.org/", "Called with right URL"
