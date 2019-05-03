# -*- coding: utf-8 -*-
import unittest
from domplus import financeplus


class CreditCard(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_valid_creditcard(self):
        """
        Test is_valid_creditcard
        """
        # True
        self.assertEqual(True, financeplus.is_valid_creditcard('376226864104614'))  # Amex
        self.assertEqual(True, financeplus.is_valid_creditcard('6762498687801564'))  # Maestro
        self.assertEqual(True, financeplus.is_valid_creditcard('4021087370711545'))  # Visa
        self.assertEqual(True, financeplus.is_valid_creditcard('5480450562290085'))  # Mastercard
        self.assertEqual(True, financeplus.is_valid_creditcard('3095734612723704'))  # Diners Club
        self.assertEqual(True, financeplus.is_valid_creditcard('5078601870000127985'))  # Aura
        self.assertEqual(True, financeplus.is_valid_creditcard('6011111111111117'))  # Discover
        self.assertEqual(True, financeplus.is_valid_creditcard('6362970000457013'))  # Elo
        self.assertEqual(True, financeplus.is_valid_creditcard('6062825624254001'))  # Hipercard
        self.assertEqual(True, financeplus.is_valid_creditcard('3530111333300000'))  # JCB
        self.assertEqual(True, financeplus.is_valid_creditcard('50339619890917'))  # Maestro

        # False
        self.assertEqual(False, financeplus.is_valid_creditcard('376226864104610'))  # Amex
        self.assertEqual(False, financeplus.is_valid_creditcard('6762498687801560'))  # Maestro
        self.assertEqual(False, financeplus.is_valid_creditcard('4021087370711540'))  # Visa
        self.assertEqual(False, financeplus.is_valid_creditcard('5480450562290080'))  # Mastercard
        self.assertEqual(False, financeplus.is_valid_creditcard('3095734612723700'))  # Diners Club
        self.assertEqual(False, financeplus.is_valid_creditcard('5078601870000127980'))  # Aura
        self.assertEqual(False, financeplus.is_valid_creditcard('6011111111111110'))  # Discover
        self.assertEqual(False, financeplus.is_valid_creditcard('6362970000457010'))  # Elo
        self.assertEqual(False, financeplus.is_valid_creditcard('6062825624254000'))  # Hipercard
        self.assertEqual(False, financeplus.is_valid_creditcard('3530111333000000'))  # JCB
        self.assertEqual(False, financeplus.is_valid_creditcard('50339619890910'))  # Maestro
