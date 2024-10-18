import os
import requests
import urllib
import sys


def menu():
    ascii_path = 'sample.txt'
    with open(ascii_path, 'r') as ascii:
            ascii_content = ascii.read()
            print(ascii_content)
    print("\n")
    print("[0] - Exit   [1] - Start   [2] - Proxies")
    print("\n")

def main():
    link = ""
    file = "proxy.txt"
    times = 0
    menu()
    choice = int(input("Cern@User-[$]#"))
    menu();




