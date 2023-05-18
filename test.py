# from dataclasses import dataclass
# from dacite import from_dict
#
#
# @dataclass
# class A:
#     x: str
#     y: int
#
#
# @dataclass
# class B:
#     a: A
#
#
# data = {
#     'a': {
#         'x': 'test',
#         'y': 1,
#     }
# }
#
# result = from_dict(data_class=B, data=data)
# print(result.a.y)

# assert result == B(a=A(x='test', y=1))



import socket

running_timer_v2_station_5 = "4854001f00891473fff27cbc5f1d2f097320e44cc402190000003000350051166464190001000000000000000000000000ffffb9b000110001010000001100400011ffffffff323032332f30352f31372031323a31383a32362c2c6864323031382c39354334463342302d304342382d344246362d414642412d3433463444303330343542311fa6aa"
x = "485273fff27cbc5f1d2f097320e44cc40219001c140000000000003507f1aa"
ip = '192.168.100.75'
puerto = 6101
# Contenido del mensaje a enviar
mensaje = bytes.fromhex(running_timer_v2_station_5)  # Asegúrate de definir display_normal_v2_station_5

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)  # Establece un tiempo de espera de 5 segundos

try:
    sock.sendto(mensaje, (ip, puerto))
    # data, addr = sock.recvfrom(1024)  # Espera recibir una respuesta del servidor
    # print(data)
    print("La IP responde correctamente.")
    # Aquí puedes realizar alguna acción adicional con la respuesta recibida, si es necesario
except socket.timeout:
    print("Error: No se recibió ninguna respuesta.")
except socket.error as e:
    print(f"Error: {str(e)}")

sock.close()