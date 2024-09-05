import argparse
import logging
from modules.capture import PacketCapture
from modules.crack import WPA2Cracker
from modules.deauth import DeauthAttack
from utils.logger import setup_logger

def cli():
    setup_logger()
    parser = argparse.ArgumentParser(description="Aircrack-ng Python CLI")
    parser.add_argument("-i", "--interface", help="Network interface to use", required=True)
    parser.add_argument("-b", "--bssid", help="Target BSSID", required=True)
    parser.add_argument("-c", "--client", help="Client MAC address for deauth")
    parser.add_argument("-o", "--output", help="Output file for captured packets", default="capture.pcap")
    parser.add_argument("-w", "--wordlist", help="Wordlist for cracking")
    parser.add_argument("--deauth", action="store_true", help="Perform deauthentication attack")
    parser.add_argument("--capture", action="store_true", help="Capture WPA handshake")
    parser.add_argument("--crack", action="store_true", help="Crack WPA handshake")

    args = parser.parse_args()

    if args.deauth and args.client:
        deauth = DeauthAttack(args.interface, args.bssid, args.client)
        deauth.send_deauth()

    if args.capture:
        capture = PacketCapture(args.interface, args.output)
        capture.start_capture()

    if args.crack and args.wordlist:
        capture = PacketCapture(args.interface, args.output)
        capture.load_capture(args.output)
        handshake = capture.filter_handshake()
        if handshake:
            cracker = WPA2Cracker(args.bssid, args.wordlist)
            cracker.crack_handshake(*handshake)

if __name__ == "__main__":
    cli()

