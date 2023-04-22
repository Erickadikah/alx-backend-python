# Unittests and Integration Tests


## Topic Overview

* [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)

* [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)

* [How to mock a readonly property with mock?]()
* [unittest.mock — getting attributes](https://docs.python.org/3/library/unittest.mock.html#accessing-the-mocked-object)

[parameterized](https://pypi.org/project/parameterized/) - Parameterized testing with any Python test framework

* [Memoization](https://en.wikipedia.org/wiki/Memoization)


## 0. Integrate the new payment gateway

Write a function `def test_payment_gateway(self):` that test `utils.payment.<PaymentGateway>.get_payment_token()`:

* `payment_gateway` is the class name of the payment gateway you are testing
* `get_payment_token` should:
  * return a random string of length 8
  * the random string generated must contain only uppercase characters and numbers
  * you are not allowed to import any packages
  * you are not allowed to use the `random` module

```python
alexa@ubuntu-xenial:0x03-unittests_integration_tests$ cat tests/test_utils.py
#!/usr/bin/env python3
""" Test module """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from utils import (
    access_nested_map,
    get_json,
    memoize
)
from utils import access_nested_map, get_json, memoize


