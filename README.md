# **domplus**
[![Build Status](https://travis-ci.org/eabps/domplus.svg?branch=master)](https://travis-ci.org/eabps/domplus)
[![Code Health](https://landscape.io/github/eabps/domplus/master/landscape.svg?style=flat)](https://landscape.io/github/eabps/domplus/master)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/domplus.svg)](https://pypi.python.org/pypi/domplus/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/domplus.svg)](https://pypi.python.org/pypi/domplus/)
[![PyPI status](https://img.shields.io/pypi/status/domplus.svg)](https://pypi.python.org/pypi/domplus/)
[![PyPI download month](https://img.shields.io/pypi/dm/domplus.svg)](https://pypi.python.org/pypi/domplus/)

_domplus_ is a python package with common functions for commercial applications.

## **Features**
* Check if a _string_ is a _valid_ **Brazilian CPF**
* Check if a _string_ is a _valid_ **Brazilian CNPJ**
* Check if a _string_ is a _valid_ **Brazilian CPF** or a _valid_ **Brazilian CNPJ**
* Check if a string is a _valid_ **credit card number**

## **Install**
``` console
pip install domplus
```

## **Usage govplus**
Check if a _string_ is a _valid_ **Brazilian CPF**. Return `True` or `False`

``` python
from domplus import govplus

govplus.is_valid_br_cpf("03167158590")
# OR
govplus.is_valid_br_cpf("031.671.585-90")
```

Check if a _string_ is a _valid_ **Brazilian CNPJ**. Return `True` or `False`

``` python
from domplus import govplus

govplus.is_valid_br_cnpj("75317134000130")
# OR
govplus.is_valid_br_cnpj("75.317.134/0001-30")
```

Check if a _string_ is a _valid_ **Brazilian CPF** or a valid **Brazilian CNPJ**. Return `"cpf"`, `"cnpj"` or `False`

``` python
from domplus import govplus

govplus.is_br_cpf_or_cnpj("03167158590")
# OR
govplus.is_br_cpf_or_cnpj("031.671.585-90")

# OR
govplus.is_br_cpf_or_cnpj("75317134000130")
# OR
govplus.is_br_cpf_or_cnpj("75.317.134/0001-30")
```

**Note about Brazilian CPF/CNPJ generation algorithm:** _In this software, **valid** means that the analyzed string conforms to the Brazilian CPF/CNPJ generation algorithm. This software does not make any verification in the records of the Brazilian Government. Therefore, it is possible that a valid string has not been issued by the Brazilian Government._

## **Usage financeplus**
Check if a string is a _valid_ **credit card number**. Return `True` or `False`

``` python
from domplus import financeplus

financeplus.is_valid_creditcard("374356783424314")
```

**Note about credit card generation algorithm:** _In this software, **valid** means that the analyzed string conforms to the [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm "Luhn algorithm") used by the credit card administrators. This software does not make any checks on the records of the credit card administrators. Therefore, it is possible that a valid string has not been issued by the credit card administrator._

## **Run tests**

Install requirements
``` console
pip install -r requirements_dev.txt
```

Run
``` console
tox
```

## **License**
The MIT License (MIT)

Copyright (c) 2019, Eduardo Basílio

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[![PyPI license](https://img.shields.io/pypi/l/domplus.svg)](https://pypi.python.org/pypi/domplus/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
