
"""
Example IP changer
"""

import requests
from stem import Signal
from stem.control import Controller
import time

def send_request():
    url = 'https://myip.nl'
    
    # Set the proxy
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }

    try:
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            html_response = response.text
            start_index = html_response.find("<b>") + len("<b>")
            end_index = html_response.find("</b>", start_index)
            ip_address = html_response[start_index:end_index].strip()
            return ip_address
        else:
            return f"Request failed with status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {str(e)}"

def change_ip_address():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_password")  # Replace "your_password" with your actual password
        controller.signal(Signal.NEWNYM)

# Get the initial IP address
ip_address = send_request()
print(ip_address)

input("Press Enter to change IP address")

# Change the IP address
change_ip_address()

# Wait for a few seconds to allow the IP address to change
time.sleep(3)

# Get the new IP address
ip_address = send_request()
print(ip_address)
