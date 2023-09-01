# -*- coding: utf-8 -*-
from domplus import finance


class TestCreditCard:
    def test_is_creditcard(self):
        """
        Test is_creditcard
        """
        # True
        assert True is finance.is_creditcard('376226864104614')  # Amex
        assert True is finance.is_creditcard('6762498687801564')  # Maestro
        assert True is finance.is_creditcard('4021087370711545')  # Visa
        assert True is finance.is_creditcard('5480450562290085')  # Mastercard
        assert True is finance.is_creditcard('3095734612723704')  # Diners Club
        assert True is finance.is_creditcard('5078601870000127985')  # Aura
        assert True is finance.is_creditcard('6011111111111117')  # Discover
        assert True is finance.is_creditcard('6362970000457013')  # Elo
        assert True is finance.is_creditcard('6062825624254001')  # Hipercard
        assert True is finance.is_creditcard('3530111333300000')  # JCB
        assert True is finance.is_creditcard('50339619890917')  # Maestro

        # False
        assert False is finance.is_creditcard('376226864104610')  # Amex
        assert False is finance.is_creditcard('6762498687801560')  # Maestro
        assert False is finance.is_creditcard('4021087370711540')  # Visa
        assert False is finance.is_creditcard('5480450562290080')  # Mastercard
        assert False is finance.is_creditcard('3095734612723700')  # Diners Club
        assert False is finance.is_creditcard('5078601870000127980')  # Aura
        assert False is finance.is_creditcard('6011111111111110')  # Discover
        assert False is finance.is_creditcard('6362970000457010')  # Elo
        assert False is finance.is_creditcard('6062825624254000')  # Hipercard
        assert False is finance.is_creditcard('3530111333000000')  # JCB
        assert False is finance.is_creditcard('50339619890910')  # Maestro
