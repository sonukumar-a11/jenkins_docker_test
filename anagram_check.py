import sys
from collections import Counter
def check_anagaram(str1,str2) -> str:
  
    if(Counter(str1) == Counter(str2)):
        return f"{str1} is anagrams with {str2}"
    else:
        return f"{str1} aren't anagrams with {str2}"
  
  