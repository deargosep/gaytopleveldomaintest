import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import json
from tinydb import TinyDB, Query

db = TinyDB('db.json')


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


with open('list.json') as json_file:
    data = json.load(json_file)

    # Print the type of data variable
    print("Type:", type(data))

    for i in data:
        if ping(f"gay{i['tlds'][0]}"):
            db.insert({'country': i['country'], 'tlds': i['tlds'][0]})
