# -*- coding: utf-8 -*-
import pytest
from domplus.gov.br import (
    is_cpf,
    is_cnpj,
    is_cpf_or_cnpj,
    is_cnh
)

from domplus.gov.br.br import (
    _INVALID_CPF,
    _INVALID_CNPJ,
    is_renavam,
)


class TestCPF:
    valid_cpf = ('03167158590', '46736825563')
    invalid_cpf = _INVALID_CPF + (
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

    
    def test_is_cpf_with_invalid_number_type(self):
        with pytest.raises(TypeError):
            is_cpf(46736825563)

    def test_is_cpf_with_valid_number(self):
        assert all(is_cpf(cpf) for cpf in self.valid_cpf) is True

    def test_is_cpf_with_invalid_number(self):
        assert all(is_cpf(cpf) for cpf in self.invalid_cpf) is False


class TestCNPJ:
    valid_cnpj = ('11444777000161', '64746812000163')
    invalid_cnpj = _INVALID_CNPJ + (
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

    def test_is_cnpj_with_invalid_number_type(self):
        with pytest.raises(TypeError):
            is_cpf(11444777000161)

    def test_is_cnpj_with_valid_number(self):
        assert all(is_cnpj(cnpj) for cnpj in self.valid_cnpj) is True

    def test_is_cnpj_with_invalid_sequential_numbers(self):
        assert all(is_cnpj(str(cnpj) * 14) for cnpj in range(10)) is False


class TestCPFCNPJ(TestCPF, TestCNPJ):    
    def test_is_cpf_or_cnpj_with_valid_numbers(self):
        assert all([True if is_cpf_or_cnpj(cpf) == 'cpf' else False for cpf in self.valid_cpf]) is True
        assert all([True if is_cpf_or_cnpj(cnpj) == 'cnpj' else False for cnpj in self.valid_cnpj]) is True

    def test_is_cpf_or_cnpj_with_invalid_numbers(self):
        assert all([True if is_cpf_or_cnpj(cpf_cnpj) in ['cpf', 'cnpj'] else False for cpf_cnpj in self.invalid_cpf + self.invalid_cnpj]) is False


class TestCNH:
    valid_cnh = (
        '74922801713',
        '60284242178',
        '28420804088',
        '77325969189',
        '10755468757',
        '84124243041'
    )

    invalid_cnh = (
        '74922801714',
        '70284242178',
        '2a420804088',
        '7732596918',
        '1075546875.7'
        '00000000000',
        '8412424304e'
    )

    def test_is_cnh_with_valid_number(self):
        assert all([is_cnh(cnh) for cnh in self.valid_cnh]) is True
    
    def test_is_cnh_with_invalid_number(self):
        assert all([is_cnh(str(cnh)) for cnh in self.invalid_cnh]) is False


class TestRENAVAM:
    valid_renavam = (
        '70627923195',
        '63850231769',
        '39162320030',
        '17105496086',
    )

    invalid_renavam = (
        '70627923196',
        '63850231760',
        '3916232003',
        '1a105496086',
    )

    def test_is_renavam_with_invalid_number_type(sekf):
        with pytest.raises(TypeError):
            is_renavam(70627923195)

    def test_is_renavam_with_valid_number(self):
        assert all([is_renavam(renavam) for renavam in self.valid_renavam]) is True
    
    def test_is_renavam_with_invalid_number(self):
        assert all([is_renavam(renavam) for renavam in self.invalid_renavam]) is False