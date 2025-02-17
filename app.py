import json
import os
import socket

path_json = "hde62.json"
current_directory = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(current_directory, path_json)


def file_config():
    with open(file, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config


def send_data(data, ip, port):
    try:
        message = bytes.fromhex(data)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)
        sock.sendto(message, (ip, port))
        sock.close()
        result = "OK"
    except socket.timeout:
        result = "ERROR"

    return result


def number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def parameters(station: int, application: str):
    if number(station):
        dictionary = file_config()
        station = dictionary["station_" + str(station)]
        data = station[application]
        ip = station["ip"]
        port = 6101
        result = send_data(data, ip, port)
        return result
    else:
        return "Error number station"


print(parameters(station=2, application="timer"))

# Esto es un ejemplo
