import pytest
from palindrome import longest_palindromic_substring


def is_palindrome(text: str) -> bool:
    return text == text[::-1]


@pytest.mark.parametrize(
    "s, expected_options",
    [
        ("babad", {"bab", "aba"}),   
        ("cbbd", {"bb"}),
        ("racecar", {"racecar"}),
        ("a", {"a"}),
        ("ac", {"a", "c"}),          
        ("aaaa", {"aaaa"}),          
    ]
)
def test_known_examples(s, expected_options):
    result = longest_palindromic_substring(s)
    assert result in expected_options


@pytest.mark.parametrize(
    "s, expected_length",
    [
        ("", 0),                     
        ("abc", 1),                  
        ("abba", 4),                 
        ("bananas", 5),              
        ("forgeeksskeegfor", 10),    
    ]
)
def test_result_properties_and_length(s, expected_length):
    result = longest_palindromic_substring(s)

    
    assert isinstance(result, str)
    assert result in s  # substring
    assert is_palindrome(result)

    
    assert len(result) == expected_length


@pytest.mark.parametrize("bad_input", [None, 123, 12.5, ["aba"], {"s": "aba"}])
def test_rejects_non_string_input(bad_input):
    with pytest.raises(TypeError):
        longest_palindromic_substring(bad_input)