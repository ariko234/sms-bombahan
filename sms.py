import pyfiglet
from termcolor import colored
import time
import requests

# Banner
banner = pyfiglet.figlet_format("SMS Bomber")
colored_banner = colored(banner, color='red')
print(colored_banner)

# SMS Bomber Function
def sms_bomber(phone_number, num_sms):
    url = "https://api.example.com/sendSMS"  # Replace with a valid API endpoint
    for _ in range(num_sms):
        requests.post(url, data={'phone': phone_number})
        time.sleep(1)

# Usage
phone_number = '1234567890'
num_sms = 100
sms_bomber(phone_number, num_sms)
