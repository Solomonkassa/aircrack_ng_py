import unittest
from unittest.mock import patch, MagicMock, ANY
from modules.capture import PacketCapture
from modules.crack import WPA2Cracker
from modules.deauth import DeauthAttack

class TestIntegration(unittest.TestCase):

    @patch('modules.capture.sniff')
    @patch('modules.capture.wrpcap')
    @patch('modules.deauth.sendp')
    def test_capture_and_deauth(self, mock_sendp, mock_wrpcap, mock_sniff):
        mock_sniff.return_value = [MagicMock(), MagicMock()]
        capture = PacketCapture('wlan0', 'test_capture.pcap')
        capture.start_capture(packet_count=2)

        deauth = DeauthAttack('wlan0', 'AA:BB:CC:DD:EE:FF', '11:22:33:44:55:66')
        deauth.send_deauth(count=10)

        mock_sniff.assert_called_once_with(iface='wlan0', count=2, prn=capture._packet_handler)
        mock_wrpcap.assert_called_once_with('test_capture.pcap', ANY)
        mock_sendp.assert_called_once()

    @patch('modules.capture.rdpcap')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="password\n")
    def test_handshake_cracking(self, mock_open, mock_rdpcap):
        mock_rdpcap.return_value = [MagicMock()]
        capture = PacketCapture('wlan0', 'test_capture.pcap')
        capture.load_capture('test_capture.pcap')
        handshake = capture.filter_handshake()

        cracker = WPA2Cracker('TestSSID', 'test_wordlist.txt')
        passphrase = cracker.crack_handshake('AA:BB:CC:DD:EE:FF', '11:22:33:44:55:66', b'\x01'*32, b'\x02'*32, b'\x00'*16, b'\x00'*99)

        self.assertEqual(passphrase, "password")

if __name__ == '__main__':
    unittest.main()

