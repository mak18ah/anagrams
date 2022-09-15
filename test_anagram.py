from typing import Tuple, List
import pytest 

from anagram import isAnagram

words: List[Tuple[str,str,bool]] = [
    ("anagram","nagaram", True),
    ("rat","car", False),
    ("anagram","anagram", False),
    ("anagram","anagramm", False),
    ("","", False),
    ("car","", False),
    ("","car", False),
    ("rat","tar", True)
]

@pytest.mark.parametrize("word,anagram,assertion_val", words)
def test_isAnagram(word: str, anagram: str, assertion_val: bool):
    assert(isAnagram(word,anagram) == assertion_val)
