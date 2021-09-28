import unittest
import task6


class TestLuckyTickets(unittest.TestCase):
    """
    This class tests task6.py
    """

    def test_number_of_lucky_tickets(self):
        self.assertEqual(task6.LuckyTickets('Moscow', ['000001', '111111', '222222']).number_of_lucky_tickets, 2)
        self.assertEqual(
            task6.LuckyTickets('Piter_alternative', ['000001', '111111', '222222']).number_of_lucky_tickets, 2)
        self.assertEqual(task6.LuckyTickets('Piter', ['000001', '111111', '222222']).number_of_lucky_tickets, 0)
        self.assertEqual(task6.LuckyTickets('Moscow', []).number_of_lucky_tickets, 0)
        self.assertEqual(task6.LuckyTickets('Piter_alternative', []).number_of_lucky_tickets, 0)
        self.assertEqual(task6.LuckyTickets('Piter', []).number_of_lucky_tickets, 0)
        self.assertEqual(task6.LuckyTickets('Moscow', ['000001', '111122', '221111']).number_of_lucky_tickets, 0)
        self.assertEqual(
            task6.LuckyTickets('Piter_alternative', ['000001', '111122', '221111']).number_of_lucky_tickets, 2)
        self.assertEqual(task6.LuckyTickets('Piter', ['000001', '111122', '221111']).number_of_lucky_tickets, 2)

    def test_lucky_tickets(self):
        self.assertEqual(task6.LuckyTickets('Moscow', ['000001', '111111', '222222']).lucky_tickets,
                         'Number of lucky tickets for the Moscow method is 2.')
        self.assertEqual(task6.LuckyTickets('Piter_alternative', ['000001', '111111', '222222']).lucky_tickets,
                         'Number of lucky tickets for the Piter method is 2.')
        self.assertEqual(task6.LuckyTickets('Piter', ['000001', '111111', '222222']).lucky_tickets,
                         'Number of lucky tickets for the Piter task method is 0.')
        self.assertEqual(task6.LuckyTickets('Moscow', []).lucky_tickets,
                         'Number of lucky tickets for the Moscow method is 0.')
        self.assertEqual(task6.LuckyTickets('Piter_alternative', []).lucky_tickets,
                         'Number of lucky tickets for the Piter method is 0.')
        self.assertEqual(task6.LuckyTickets('Piter', []).lucky_tickets,
                         'Number of lucky tickets for the Piter task method is 0.')
        self.assertEqual(task6.LuckyTickets('Moscow', ['000001', '111122', '221111']).lucky_tickets,
                         'Number of lucky tickets for the Moscow method is 0.')
        self.assertEqual(task6.LuckyTickets('Piter_alternative', ['000001', '111122', '221111']).lucky_tickets,
                         'Number of lucky tickets for the Piter method is 2.')
        self.assertEqual(task6.LuckyTickets('Piter', ['000001', '111122', '221111']).lucky_tickets,
                         'Number of lucky tickets for the Piter task method is 2.')

    def test_is_lucky(self):
        tickets = ['000001', '111111', '222222', '111122', '221111']

        self.assertTrue(task6.LuckyTickets('Moscow', tickets).is_lucky(tickets[1]))
        self.assertTrue(task6.LuckyTickets('Moscow', tickets).is_lucky(tickets[2]))
        self.assertTrue(task6.LuckyTickets('Piter_alternative', tickets).is_lucky(tickets[1]))
        self.assertTrue(task6.LuckyTickets('Piter_alternative', tickets).is_lucky(tickets[2]))
        self.assertTrue(task6.LuckyTickets('Piter_alternative', tickets).is_lucky(tickets[3]))
        self.assertTrue(task6.LuckyTickets('Piter_alternative', tickets).is_lucky(tickets[4]))
        self.assertTrue(task6.LuckyTickets('Piter', tickets).is_lucky(tickets[3]))
        self.assertTrue(task6.LuckyTickets('Piter', tickets).is_lucky(tickets[4]))

        self.assertFalse(task6.LuckyTickets('Piter_alternative', tickets).is_lucky(tickets[0]))
        self.assertFalse(task6.LuckyTickets('Piter', tickets).is_lucky(tickets[0]))
        self.assertFalse(task6.LuckyTickets('Piter', tickets).is_lucky(tickets[1]))
        self.assertFalse(task6.LuckyTickets('Piter', tickets).is_lucky(tickets[0]))
        self.assertFalse(task6.LuckyTickets('Piter', tickets).is_lucky(tickets[2]))
        self.assertFalse(task6.LuckyTickets('Moscow', tickets).is_lucky(tickets[0]))
        self.assertFalse(task6.LuckyTickets('Moscow', tickets).is_lucky(tickets[3]))
        self.assertFalse(task6.LuckyTickets('Moscow', tickets).is_lucky(tickets[4]))


if __name__ == '__main__':
    unittest.main()
