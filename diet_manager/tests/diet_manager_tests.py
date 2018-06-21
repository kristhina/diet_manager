import unittest

from diet_manager.models import User


class TestDietManager(unittest.TestCase):

    def testUserBMI(self):
        u = User()
        u.weight = 50
        u.height = 155
        self.assertEqual(u.count_bmi(), 20.81)

    def testIfUserIsAdmin(self):
        u = User()
        u.admin = True
        self.assertTrue(u.is_admin())

