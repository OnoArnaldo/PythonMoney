# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from decimal import Decimal
from money import Money


class TestMoneyCreate(unittest.TestCase):

    def setUp(self):
        Money.default_currency = 'BRL'
        Money.default_precision = 2
        Money.default_locale = 'pt_BR'

    def testDefault(self):
        money = Money()

        self.assertEqual(0, money.amount)
        self.assertEqual(2, money.precision)
        self.assertEqual('BRL', money.currency)
        self.assertEqual(0.0, money.to_float())
        self.assertEqual('0.00', money.to_str())

    def testDifferentFromDefault(self):
        money = Money(12345, 4, 'EUR')

        self.assertEqual(12345, money.amount)
        self.assertEqual(4, money.precision)
        self.assertEqual('EUR', money.currency)
        self.assertEqual(1.2345, money.to_float())
        self.assertEqual('1.2345', money.to_str())


class TestMoneyOperationBetweenMoney(unittest.TestCase):

    def setUp(self):
        Money.default_currency = 'BRL'
        Money.default_precision = 2
        Money.default_locale = 'pt_BR'

    def testAddition(self):
        brl10 = Money(1000)
        brl20 = Money(2000)

        brl30 = brl10 + brl20

        self.assertEqual(3000, brl30.amount)
        self.assertEqual(2, brl30.precision)
        self.assertEqual('BRL', brl30.currency)

    def testSubtraction(self):
        brl20 = Money(2000)
        brl05 = Money(500)

        brl15 = brl20 - brl05

        self.assertEqual(1500, brl15.amount)
        self.assertEqual(2, brl15.precision)
        self.assertEqual('BRL', brl15.currency)


class TestMoneyOperation(unittest.TestCase):

    def setUp(self):
        Money.default_currency = 'BRL'
        Money.default_precision = 2
        Money.default_locale = 'pt_BR'

    def testAddition(self):
        brl10 = Money(1000)
        brl30 = brl10 + 2000

        self.assertEqual(3000, brl30.amount)
        self.assertEqual(2, brl30.precision)
        self.assertEqual('BRL', brl30.currency)

    def testSubtraction(self):
        brl20 = Money(2000)
        brl15 = brl20 - 500

        self.assertEqual(1500, brl15.amount)
        self.assertEqual(2, brl15.precision)
        self.assertEqual('BRL', brl15.currency)

    def testMultiplication(self):
        brl10 = Money(1000)
        brl30 = brl10 * 3

        self.assertEqual(3000, brl30.amount)
        self.assertEqual(2, brl30.precision)
        self.assertEqual('BRL', brl30.currency)

        brl = brl10 * 0.1234
        self.assertEqual(123, brl.amount)
        self.assertEqual(2, brl.precision)
        self.assertEqual('BRL', brl.currency)
        self.assertEqual(Decimal('0.4'), brl.remain)

    def testCompare(self):
        self.assertTrue(Money(1000) == Money(1000))
        self.assertTrue(Money(1000) >= Money(1000))
        self.assertTrue(Money(1000) <= Money(1000))
        self.assertTrue(Money(1000) > Money(500))
        self.assertTrue(Money(500) < Money(1000))


class TestMoneySplit(unittest.TestCase):

    def setUp(self):
        Money.default_currency = 'BRL'
        Money.default_precision = 2
        Money.default_locale = 'pt_BR'

    def testSplit(self):
        money = Money(1000)
        split = money.split(3)

        self.assertEqual(3, len(split))
        self.assertEqual(split[0], Money(333))
        self.assertEqual(split[1], Money(333))
        self.assertEqual(split[2], Money(334))


class TestMoneyCopy(unittest.TestCase):
    def setUp(self):
        Money.default_currency = 'BRL'
        Money.default_precision = 2
        Money.default_locale = 'pt_BR'

    def testCopy(self):
        orig = Money(1000)
        copy = orig.copy()

        self.assertEqual(orig, copy)
        self.assertNotEqual(id(orig), id(copy))
