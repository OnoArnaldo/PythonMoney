# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal


class Money(object):
    default_currency = ''
    default_precision = 0

    def __init__(self, amount=0, precision=None, currency=None):
        self._amount = amount
        self._precision = precision if precision else self.default_precision
        self._currency = currency if currency else self.default_currency
        self._remain = Decimal(0)

    def __repr__(self):
        return 'Money(amount={}, precision={}, currency="{}")'.format(
            self.amount, self.precision, self.currency
        )

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def currency(self):
        return self._currency

    @property
    def precision(self):
        return self._precision

    @property
    def remain(self):
        return self._remain

    def _assert(self, money):
        return (self._precision == money.precision
            and self._currency == money.currency)

    def to_float(self):
        return self.amount / float(10**self.precision)

    def to_str(self):
        exp = Decimal(10) ** self.precision
        ret = Decimal(self.amount) / exp
        return '{:.{prec}f}'.format(ret, prec=self.precision)

    def add(self, amount):
        to_add = int(amount)
        self._amount += to_add
        self._remain = Decimal(str(amount)) - to_add

    def multiply(self, value):
        new_amount = self._amount * value
        self._amount = int(new_amount)
        self._remain = Decimal(str(new_amount)) - Decimal(int(new_amount))

    def split(self, value):
        new_amount = self.amount / value
        remain_amount = self.amount

        ret = []
        for i in range(value-1):
            money = self.copy()
            money.amount = new_amount
            remain_amount -= new_amount

            ret.append(money)

        if remain_amount:
            money = self.copy()
            money.amount = remain_amount
            ret.append(money)

        return ret

    def copy(self):
        return Money(self.amount, self.precision, self.currency)

    def __add__(self, other):
        new_money = self.copy()

        if isinstance(other, Money) and self._assert(other):
            new_money.add(other.amount)
        else:
            new_money.add(other)

        return new_money

    def __sub__(self, other):
        new_money = self.copy()

        if isinstance(other, Money) and self._assert(other):
            new_money.add(-other.amount)
        else:
            new_money.add(-other)

        return new_money

    def __mul__(self, other):
        new_money = self.copy()
        new_money.multiply(other)
        return new_money

    def __cmp__(self, other):
        if isinstance(other, Money) and self._assert(other):
            if self.amount > other.amount:
                return 1
            if self.amount < other.amount:
                return -1

            if self.remain > other.remain:
                return 1
            if self.remain < other.remain:
                return -1

            return 0

        raise Exception('Objects are not comparable')
