# -*- coding: utf-8 -*-
import re


_INVALID_CPF = (
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

_INVALID_CNPJ = (
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


def is_valid_br_cpf(cpf):
    """
    Accept an string parameter cpf and
    Check if is brazilian CPF valid.
    Return True or False
    """

    # Extract dots, stroke
    cpf = re.sub('[.|-]', '', str(cpf))

    if not re.match(r'^\d{11}$', cpf) or cpf in _INVALID_CPF:
        return False

    # checks if all digits are equal
    for i in range(10):
        text = str(i) * 11
        if text == cpf:
            return False

    # first checksum
    multi = 10
    result = 0

    for i in cpf[:9]:
        result += int(i) * multi
        multi -= 1

    remainder = result % 11

    if remainder < 2:
        checksum1 = 0
    else:
        checksum1 = 11 - remainder

    assemble_cpf = cpf[:9] + str(checksum1)

    # secound checksum
    multi = 11
    result = 0

    for i in assemble_cpf:
        result += int(i) * multi
        multi -= 1

    remainder = result % 11

    if remainder < 2:
        checksum2 = 0
    else:
        checksum2 = 11 - remainder

    assemble_cpf += str(checksum2)

    return True if cpf == assemble_cpf else False


def is_valid_br_cnpj(cnpj):
    """
    Accept an string parameter cnpj and
    Check if is brazilian CNPJ valid.
    Return True or False
    """

    # Extract dots, stroke, slash
    cnpj = re.sub('[.|\-/|/]', '', str(cnpj))

    # if does not contain numerical characters
    if not re.match(r'^\d{14}$', cnpj) or cnpj in _INVALID_CNPJ:
        return False

    # checks if all digits are equal
    for i in range(10):
        text = str(i) * 14
        if text == cnpj:
            return False

    # first checksum1
    multi = 5
    result = 0
    for i in cnpj[:12]:
        result += int(i) * multi
        multi -= 1
        if multi < 2:
            multi = 9

    remainder = result % 11

    if remainder < 2:
        checksum1 = 0
    else:
        checksum1 = 11 - remainder

    assemble_cnpj = cnpj[:12] + str(checksum1)

    # secound checksum
    multi = 6
    result = 0

    for i in assemble_cnpj:
        result += int(i) * multi
        multi -= 1
        if multi < 2:
            multi = 9

    remainder = result % 11

    if remainder < 2:
        checksum2 = 0
    else:
        checksum2 = 11 - remainder

    assemble_cnpj += str(checksum2)

    return True if cnpj == assemble_cnpj else False


def is_br_cpf_or_cnpj(cpfcnpj):
    """
    Accept an string parameter cpfcnpj;
    If is brazilian CPF valid, return 'cpf'
    If is brazilian CNPJ valid, return 'cnpj'
    Else, return False
    """
    # Extract dots, stroke, slash
    cpfcnpj = re.sub('[.|\-/|/]', '', str(cpfcnpj))


    if len(cpfcnpj) == 11:
        return 'cpf' if is_valid_br_cpf(cpfcnpj) else False
    if len(cpfcnpj) == 14:
        return 'cnpj' if is_valid_br_cnpj(cpfcnpj) else False

    return False
