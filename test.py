import unittest

from enumit import Enum


class Status(Enum):
    WAITING = Enum.Field('waiting', 'Waiting')
    APPROVED = Enum.Field('approved', 'Approved')
    NOT_NAMED = Enum.Field('not_named')


class UserStatus(Status):
    SUSPENDED = Enum.Field('suspended', 'Suspended')


class OrderStatus(Status):
    CANCELLED = Enum.Field('cancelled', 'Cancelled')


class EnumTest(unittest.TestCase):
    def runTest(self):
        # Class attribute must be equal own value(first arg.)
        self.assertEqual(Status.WAITING, 'waiting')

        # if name isn't given, must be capitalized.
        self.assertEqual(Status['not_named'], 'Not Named')

        # values must be in defined order.
        self.assertListEqual(Status.values(), ['waiting', 'approved', 'not_named'])


class MagicMethodTest(unittest.TestCase):
    def runTest(self):
        # Enum field can't be changed.
        with self.assertRaises(ValueError):
            Status.APPROVED = 'approving'

        # Enum field can't be deleted.
        with self.assertRaises(ValueError):
            del Status.APPROVED

        # return True, value is in Enum Class.
        self.assertTrue('waiting' in Status)

        # return False, if not exist in Enum class.
        self.assertFalse('this_is_not_in_Status' in Status)

        # field name(second argument) is returned by __setattr__
        self.assertEqual(Status['waiting'], 'Waiting')

        self.assertEqual(Status.__len__(), 3)


class InheritanceTest(unittest.TestCase):
    def runTest(self):
        # attributes of parent class can be reached by inherited Enum class.
        self.assertEqual(UserStatus.WAITING, 'waiting')
        self.assertEqual(OrderStatus.CANCELLED, 'cancelled')


