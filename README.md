[![Build Status](https://app.travis-ci.com/edubasilio/domplus.svg?branch=master)](https://app.travis-ci.com/edubasilio/domplus)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/domplus.svg)](https://pypi.python.org/pypi/domplus/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/domplus.svg)](https://pypi.python.org/pypi/domplus/)
[![PyPI download month](https://img.shields.io/pypi/dm/domplus.svg)](https://pypi.python.org/pypi/domplus/)

_domplus_ is a python package with common functions for commercial applications.

# **Features**
* Check if a _string_ is a valid **Brazilian CPF**
* Check if a _string_ is a valid **Brazilian CNPJ**
* Check if a _string_ is a valid **Brazilian CPF** or a valid **Brazilian CNPJ**
* Check if a _string_ is a valid **Brazilian CNH**
* Check if a _string_ is a valid **Brazilian RENAVAM**
* Check if a _string_ is a valid **credit card number**

# **Install**
```sh
pip install domplus
```

# **Usage**
## Brazilian CPF and CNPJ
Check if a _string_ is a valid **Brazilian CPF**:

```python
from domplus.gov.br import is_cpf

is_cpf("03167158590")  # return True or False
```

Check if a _string_ is a valid **Brazilian CNPJ**:

```python
from domplus.gov.br import is_cnpj

is_cnpj("75317134000130")  # return True or False
```

Check if a _string_ is a valid **Brazilian CPF** or a valid **Brazilian CNPJ**:

```python
from domplus.gov.br import is_cpf_or_cnpj

is_cpf_or_cnpj("03167158590")  # return 'cpf', 'cnpj' or False
# OR
is_cpf_or_cnpj("75317134000130")  # return 'cpf', 'cnpj' or False
```

**Note about Brazilian CPF/CNPJ validate algorithm:** _In this software, **valid** means that the analyzed string conforms to the Brazilian CPF/CNPJ generation algorithm. This software does not make any verification in the records of the Brazilian Government. Therefore, it is possible that a valid string has not been issued by the Brazilian Government._

## Brazilian CHN and RENAVAM
Check if a _string_ is a valid **Brazilian CNH**:

```python
from domplus.gov.br import is_cnh

is_chh("67377435789")  # return True or False
```

Check if a _string_ is a valid **Brazilian RENAVAM**:

```python
from domplus.gov.br import is_renavam

is_renavam("54949744211")  # return True or False
```

**Note about Brazilian CHN/RENAVAM validate algorithm:** _In this software, **valid** means that the analyzed string conforms to the Brazilian CHN/RENAVAM generation algorithm. This software does not make any verification in the records of the Brazilian Government. Therefore, it is possible that a valid string has not been issued by the Brazilian Government._

## **Creditcard**
Check if a string is a valid **credit card number**:

```python
from domplus.finance import is_creditcard

is_creditcard("374356783424314")  # return True or False
```

**Note about credit card validate algorithm:** _In this software, **valid** means that the analyzed string conforms to the [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm "Luhn algorithm") used by the credit card administrators. This software does not make any checks on the records of the credit card administrators. Therefore, it is possible that a valid string has not been issued by the credit card administrator._

# For development
## Requirements:
* Python 3.8
* Poetry 1.6.1

## Install requirements:
```sh
poetry install
```

## Run tests
```sh
poetry run pytest
```

## Commit
Before commit, in `domplus` directory, run:
```sh
poetry export -f requirements.txt --output requirements.txt --with test
```
And add `requirements.txt` in git staged

# History
**1.0.2 (2023-09-04)**
* domplus.govplus.is_validbr_cpf -> domplus.gov.br.is_cpf
* domplus.govplus.is_validbr_cnpj -> domplus.gov.br.is_cnpj
* domplus.govplus.is_br_cpf_or_cnpj -> domplus.gov.br.is_cpf_or_cnpj
* domplus.financeplus.is_validcreditcard -> domplus.finance.is_creditcard
* Add brazilian CNH validate
* Add brazilian RENAVAM validate

**0.1.9 (2019-05-01)**
* Update to Python 3.6
* Added invalid CPF / CNPJ list used by Brazilian Government - Serpro at [irpf-livre-src](http://www.fsfla.org/~lxoliva/fsfla/irpf-livre/2009/r6675/irpf-livre-src.tar.bz2)

**0.1.3 (2015-04-19)**
* First release on PyPI.

# **License**
The MIT License (MIT)

Copyright (c) 2019, Eduardo Basílio

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[![PyPI license](https://img.shields.io/pypi/l/domplus.svg)](https://pypi.python.org/pypi/domplus/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
