import unittest
from unittest.mock import patch, MagicMock
from modules.capture import PacketCapture

class TestPacketCapture(unittest.TestCase):

    @patch('modules.capture.sniff')
    @patch('modules.capture.wrpcap')
    def test_start_capture(self, mock_wrpcap, mock_sniff):
        mock_sniff.return_value = ['packet1', 'packet2']
        capture = PacketCapture('wlan0', 'test_capture.pcap')
        capture.start_capture(packet_count=2)

        mock_sniff.assert_called_once_with(iface='wlan0', count=2, prn=capture._packet_handler)
        mock_wrpcap.assert_called_once_with('test_capture.pcap', ['packet1', 'packet2'])

    @patch('modules.capture.rdpcap')
    def test_load_capture(self, mock_rdpcap):
        mock_rdpcap.return_value = ['packet1', 'packet2']
        capture = PacketCapture('wlan0', 'test_capture.pcap')
        capture.load_capture('test_capture.pcap')

        mock_rdpcap.assert_called_once_with('test_capture.pcap')
        self.assertEqual(capture.packets, ['packet1', 'packet2'])

if __name__ == '__main__':
    unittest.main()

