from register import *
from Gui import *
import unittest



class Testing(unittest.TestCase):

    def test_login(self):
        login = Register()
        result = login.login_backend('bipino', 'rollon')
        self.assertEqual((len(result)), 0)

    def test_login1(self):
        login = Register()
        result = login.login_backend('Dhiraj', '123')
        self.assertEqual((len(result)), 1)

    def test_add(self):
        login = Register()
        result = login.getting('roy', 'exporer', 'BipinDhakal', 'Thankt', '980778743', 'bipin7@gmail.com')
        self.assertTrue(result)

    def test_add1(self):
        login = Register()
        result = login.getting('bipino', 'explrer', '', 'Thnkot', '980678743', 'bipin7@gmail.com')
        self.assertFalse(result)

    def test_addplane1(self):
        login = Airline()
        result = login.register_plane('ss', 'ss', '', 'ssf', 'ff', 'iii')
        self.assertFalse(result)

    def test_addplane2(self):
        login = Airline()
        result = login.register_plane('ss', 'ss', 'dd', 'ssf', 'ff', 'iii')
        self.assertTrue(result)

    def test_delplane1(self):
        login = Airline()
        result = login.delete_item(10)
        self.assertTrue(result)

    def test_delplane2(self):
        login = Airline()
        result = login.delete_item('ss')
        self.assertFalse(result)

    def test_updplane1(self):
        login = Airline()
        result = login.update_item('ss','ss', 'ss', 'dd', 'ssf', 'ff', '1')
        self.assertTrue(result)

    def test_updplane2(self):
        login = Airline()
        result = login.update_item('ss','ss', 'ss', 'dd', 'ssf', 'ff', '')
        self.assertFalse(result)





