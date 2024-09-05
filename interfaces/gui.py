import tkinter as tk
from tkinter import messagebox
from modules.capture import PacketCapture
from modules.deauth import DeauthAttack
from modules.crack import WPA2Cracker
from utils.logger import setup_logger

def start_gui():
    setup_logger()
    root = tk.Tk()
    root.title("Aircrack-ng Python GUI")

    def capture_handshake():
        interface = interface_entry.get()
        output = output_entry.get()
        capture = PacketCapture(interface, output)
        capture.start_capture()

    def deauth_attack():
        interface = interface_entry.get()
        bssid = bssid_entry.get()
        client = client_entry.get()
        deauth = DeauthAttack(interface, bssid, client)
        deauth.send_deauth()

    tk.Label(root, text="Interface").grid(row=0, column=0)
    tk.Label(root, text="BSSID").grid(row=1, column=0)
    tk.Label(root, text="Client MAC").grid(row=2, column=0)
    tk.Label(root, text="Output File").grid(row=3, column=0)

    interface_entry = tk.Entry(root)
    bssid_entry = tk.Entry(root)
    client_entry = tk.Entry(root)
    output_entry = tk.Entry(root)

    interface_entry.grid(row=0, column=1)
    bssid_entry.grid(row=1, column=1)
    client_entry.grid(row=2, column=1)
    output_entry.grid(row=3, column=1)

    capture_button = tk.Button(root, text="Capture Handshake", command=capture_handshake)
    capture_button.grid(row=4, column=0)

    deauth_button = tk.Button(root, text="Deauth Attack", command=deauth_attack)
    deauth_button.grid(row=4, column=1)

    root.mainloop()

if __name__ == "__main__":
    start_gui()

