#!/usr/bin/env python3
from typing import List, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Union[List, str]) -> Union[str, None]:
    if lst:
        return lst[0]
    else:
        return None
