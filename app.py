from builtins import dict
from dataclasses import dataclass
from from_dict import from_dict
import json
import os
import socket

path_json = "hde62.json"
current_directory = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(current_directory, path_json)


def file_config():
    with open(file, 'r', encoding='utf-8') as f:
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


print(parameters(station=4, application="timer"))






# @dataclass
# class Variables:
#     timer: str
#     stop: str
#     play: str
#     red: str
#     normal: str
#     off: str
#     on: str

#
# @dataclass
# class Station:
#     station_1: dict
#     station_2: dict
#     station_3: dict
#     station_4: dict
#     station_5: dict


    # dictionary_general = from_dict(Station, file_config())
    # data = from_dict(Variables, station)
    # print(data)
    # return data













# y = Data(variables=file_config())


# y = from_dict(Data, file_config())
# print(y)

# config_data = file_config()
# data_dict = {}
# for key, value in config_data.items():
#     variables_obj = Variables(**value)
#     data_dict[key] = variables_obj













#
# x = file_config
# y = from_dict(Data, file_config())
# print(y)
#
# print(file_config()['1']['timer'])



# value = from_dict(QueueConfig, dict_config())





























# import socket

# running_timer_v2_station_5 = "4854001f00891473fff27cbc5f1d2f097320e44cc402190000003000350051166464190001000000000000000000000000ffffb9b000110001010000001100400011ffffffff323032332f30352f31372031323a31383a32362c2c6864323031382c39354334463342302d304342382d344246362d414642412d3433463444303330343542311fa6aa"
# x = "485273fff27cbc5f1d2f097320e44cc40219001c140000000000003507f1aa"
# ip = '192.168.100.6'
# puerto = 6101
# # Contenido del mensaje a enviar
# mensaje = bytes.fromhex(running_timer_v2_station_5)  # Asegúrate de definir display_normal_v2_station_5
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.settimeout(5)  # Establece un tiempo de espera de 5 segundos
#
# try:
#     sock.sendto(mensaje, (ip, puerto))
#     data, addr = sock.recvfrom(1024)  # Espera recibir una respuesta del servidor
#     print(data)
#     print("La IP responde correctamente.")
#     # Aquí puedes realizar alguna acción adicional con la respuesta recibida, si es necesario
# except socket.timeout:
#     print("Error: No se recibió ninguna respuesta.")
# except socket.error as e:
#     print(f"Error: {str(e)}")
#
# sock.close()
