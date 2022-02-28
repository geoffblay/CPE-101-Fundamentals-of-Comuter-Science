import unittest
from fileMatchingFuncs import *


class TestCases(unittest.TestCase):

    def test_entry_init(self):
        entry = Entry('345', 'Bob Jones', 87.12, '8055551234', 'SLO')
        self.assertEqual(entry.account_num, '345')
        self.assertEqual(entry.name, 'Bob Jones')
        self.assertAlmostEqual(entry.balance, 87.12)
        self.assertEqual(entry.phone, '8055551234')
        self.assertEqual(entry.city, 'SLO')

    def test_read_file_0(self):
        entries = []
        entries.append(Entry('100', 'Alan Jones', 348.17, '8053564820', 'SLO'))
        entries.append(Entry('700', 'Suzy Green', -14.22, '8052586912', 'SLO'))
        # call read_file with 'test0.dat'
        self.assertEqual(read_file('test0.dat'), entries)

    def test_read_file_1(self):
        entries = []
        entries.append(Entry('100', 'Alan Jones', 348.17, '8053564820', 'SLO'))
        entries.append(Entry('700', 'Suzy Green', -14.22, '8052586912', 'SLO'))
        entries.append(Entry('300', 'Mary Smith', 27.19, '8057901237', 'Santa_Maria'))
        entries.append(Entry('800', 'Mike Rosen', -104.58, '8051200891', 'Pismo_Beach'))
        # call read_file with 'test1.dat'
        self.assertEqual(read_file('test1.dat'), entries)

    def test_get_transactions_0(self):
        transactions = [['100', '27.14'], ['300', '62.11'], ['400', '100.56'], ['700', '100.0']]
        self.assertEqual(get_transactions('test2.dat'), transactions)

    def test_get_transactions_1(self):
        transactions = [['100', '0'], ['700', '300.0'], ['900', '50.17'], ['500', '-55.25']]
        self.assertEqual(get_transactions('test3.dat'), transactions)

    def test_sort_account_nums_0(self):
        account_nums = [100, 600, 700]
        self.assertEqual(sort_account_nums('test4.dat'), account_nums)

    def test_sort_account_nums_1(self):
        account_nums = [120, 200, 340, 600]
        self.assertEqual(sort_account_nums('test5.dat'), account_nums)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
