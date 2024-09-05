from scapy.all import sniff, wrpcap, rdpcap
from scapy.layers.dot11 import Dot11Auth, Dot11AssoReq
import logging

class PacketCapture:
    def __init__(self, iface, output_file):
        self.iface = iface
        self.output_file = output_file
        self.packets = []

    def start_capture(self, packet_count=0):
        """Start capturing packets on the specified interface."""
        self.packets = sniff(iface=self.iface, count=packet_count, prn=self._packet_handler)
        wrpcap(self.output_file, self.packets)

    def load_capture(self, pcap_file):
        """Load packets from a pcap file."""
        self.packets = rdpcap(pcap_file)

    def _packet_handler(self, packet):
        """Handler for each captured packet."""
        print(f"Packet captured: {packet.summary()}")

    def filter_handshake(self):
        """
        Filters the captured packets to find WPA handshake packets.
        This method looks for packets with specific characteristics.
        """
        handshake_packets = []
        for packet in self.packets:
            if packet.haslayer(Dot11Auth) or packet.haslayer(Dot11AssoReq):  # WPA handshake packets
                handshake_packets.append(packet)
            else:
                logging.warning(f"Non-packet object found: {packet}")
        return handshake_packets

