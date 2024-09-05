import unittest
from unittest.mock import patch, MagicMock
from modules.deauth import DeauthAttack

class TestDeauthAttack(unittest.TestCase):

    @patch('modules.deauth.sendp')
    def test_send_deauth(self, mock_sendp):
        deauth = DeauthAttack('wlan0', 'AA:BB:CC:DD:EE:FF', '11:22:33:44:55:66')
        deauth.send_deauth(count=10)

        self.assertEqual(mock_sendp.call_count, 1)
        self.assertEqual(mock_sendp.call_args[1]['count'], 10)

if __name__ == '__main__':
    unittest.main()

