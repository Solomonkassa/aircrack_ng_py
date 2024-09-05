import unittest
from modules.crack import WPA2Cracker

class TestWPA2Cracker(unittest.TestCase):

    def setUp(self):
        self.cracker = WPA2Cracker('TestSSID', 'test_wordlist.txt')

    def test_derive_pmk(self):
        passphrase = 'password'
        pmk = self.cracker.derive_pmk(passphrase)
        self.assertEqual(len(pmk), 32)

    def test_check_mic(self):
        pmk = b'\x00' * 32
        anonce = b'\x01' * 32
        snonce = b'\x02' * 32
        bssid = b'\xAA\xBB\xCC\xDD\xEE\xFF'
        client_mac = b'\x11\x22\x33\x44\x55\x66'
        eapol_frame = b'\x00' * 99

        mic = self.cracker.check_mic(pmk, anonce, snonce, bssid, client_mac, eapol_frame)
        self.assertEqual(len(mic), 16)

if __name__ == '__main__':
    unittest.main()

