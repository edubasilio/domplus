# -*- coding: utf-8 -*-
import pytest
from domplus.gov.br import (
    is_cpf,
    is_cnpj,
    is_cpf_or_cnpj
)

from domplus.gov.br.br import (
    _INVALID_CPF,
    _INVALID_CNPJ,
)


class TestBRGov:
    cpfs_valid = ('03167158590', '46736825563')
    cpfs_invalid = _INVALID_CPF + (
        '46736825566',
        '03167158590A',
        '467368255638',
        '4673682556',
        '00000000000',
        '00000000191',
        '99999999999',
        '11111111111',
        '22222222222',
        '33333333333',
        '44444444444',
        '55555555555',
        '66666666666',
        '77777777777',
        '88888888888',
        '99999999999',
    )
    cnpj_valid = ('11444777000161', '64746812000163')
    cnpj_invalid = _INVALID_CNPJ + (
        '84917968000166',
        '11444777000161A',
        '6474681200016',
        '11111111000191',
        '00000000000000',
        '22222222000191',
        '33333333000191',
        '44444444000191',
        '55555555000191',
        '66666666000191',
        '77777777000191',
        '88888888000191',
        '99999999000191',
    )

    def test_is_cnpj_with_valid_cnpj(self):
        assert all(is_cnpj(cnpj) for cnpj in self.cnpj_valid)

    def test_is_cnpj_with_invalid_sequential_numbers(self):
        assert all(True if is_cnpj(str(cnpj) * 14) is False else False for cnpj in range(10))

    def test_is_cpf_or_cnpj_with_invalid_numbers(self):
        assert all(True if is_cpf_or_cnpj(cnpj) is False else False for cnpj in self.cnpj_invalid)

    def test_is_cpf_with_invalid_number_type(self):
        with pytest.raises(TypeError):
            assert is_cpf(46736825563) is True

    def test_is_cpf_with_valid_number(self):
        assert all(is_cpf(cpf) for cpf in self.cpfs_valid) is True

    def test_is_cpf_with_invalid_number(self):
        assert all(True if is_cpf(cpf) is False else False for cpf in self.cpfs_invalid) is True

    def test_is_cpf_or_cnpj_with_valid_numbers(self):
        assert all([True if is_cpf_or_cnpj(cpf) is 'cpf' else False for cpf in self.cpfs_valid]) is True
        assert all([True if is_cpf_or_cnpj(cnpj) is 'cnpj' else False for cnpj in self.cnpj_valid]) is True

    def test_is_cpf_or_cnpj_with_invalid_numbers(self):
        assert all([False if is_cpf_or_cnpj(cpf_cnpj) in ['cpf', 'cnpj'] else True for cpf_cnpj in self.cpfs_invalid + self.cnpj_invalid]) is True
