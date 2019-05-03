# -*- coding: utf-8 -*-
import unittest
from domplus import govplus
from domplus.govplus import (
    _INVALID_CPF,
    _INVALID_CNPJ
)


class TestGovplus(unittest.TestCase):

    def setUp(self):
        self.cpfs_valid = ('03167158590', '467.368.255-63', '467368255-63')
        self.cpfs_invalid = _INVALID_CPF + (
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

        self.cnpj_valid = ('11444777000161', '11.444.777/0001-61', '64.746.812/0001-63')
        self.cnpj_invalid = _INVALID_CNPJ + (
            '84917968000166',
            '11444777000161A',
            '64.746.812/0001,63',
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

    def test_is_valid_br_cnpj(self):
        self.assertTrue(all(govplus.is_valid_br_cnpj(cnpj) for cnpj in self.cnpj_valid), "All CNPJ Valid how success!")

    def test_invalid_br_cnpj_sequential(self):
        self.assertTrue(all(True if govplus.is_valid_br_cnpj(str(cnpj) * 14) is False else False for cnpj in range(10)),
                        "CNPJs Invalids")

    def test_invalid_br_cpf(self):
        self.assertTrue(all(True if govplus.is_br_cpf_or_cnpj(cnpj) is False else False for cnpj in self.cnpj_invalid),
                        "CNPJs Invalid")

    def test_valid_br_cpf_type_int(self):
        self.assertTrue(govplus.is_valid_br_cpf(46736825563), "Valid cpf type int how success!")

    def test_valid_br_cpf(self):
        self.assertTrue(all(govplus.is_valid_br_cpf(cpf) for cpf in self.cpfs_valid), "All Cpfs Valid how success!")

    def test_invalid_br_cpf(self):
        self.assertTrue(all(True if govplus.is_valid_br_cpf(cpf) is False else False for cpf in self.cpfs_invalid), "Cpfs Invalid")

    def test_is_br_cpf_or_cnpj(self):
        self.assertTrue(all([True if govplus.is_br_cpf_or_cnpj(cpf) is 'cpf' else False for cpf in self.cpfs_valid]), "All CPF")
        self.assertTrue(all([True if govplus.is_br_cpf_or_cnpj(cnpj) is 'cnpj' else False for cnpj in self.cnpj_valid]), "All CNPJ")

    def test_invalid_not_cpf_or_cnpj(self):
        self.assertTrue(all([False if govplus.is_br_cpf_or_cnpj(cpf_cnpj) in ['cpf', 'cnpj'] else True
                             for cpf_cnpj in self.cpfs_invalid + self.cnpj_invalid]), "All not CPF or CNPJ")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()