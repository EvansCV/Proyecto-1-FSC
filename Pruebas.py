'''import pygame
import random
import socket

# Sustituye con la IP de la Pico W
ip_pico = "192.168.43.104"  # Cambia a la dirección IP de tu Pico W
port = 8080

try:
    with socket.create_connection((ip_pico, port), timeout=30) as s:
        print(f"Conexión exitosa a {ip_pico}:{port}")
        # Recibe la respuesta del servidor
        data = s.recv(1024)
        print("Mensaje del servidor:", data.decode())
except (socket.timeout, ConnectionRefusedError):
    print(f"No se pudo conectar a {ip_pico}:{port}. Verifica el servidor o la red.")



# Initialize Pygame
pygame.init()


# Socket configuration
pico_ip = "172.18.193.82"  # Dirección IP de la Raspberry Pi Pico W
pico_port = 8080
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((pico_ip, pico_port))

# Command sender function.
def send_command(command):
    client_socket.send(command.encode())

# Use example
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Activar flipper al presionar la barra espaciadora
                send_command("FLIPPER_ON")
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE:  # Desactivar flipper al soltar la barra espaciadora
                send_command("FLIPPER_OFF")
                
    # Tu código para actualizar y renderizar la interfaz de Pygame
    pygame.display.flip()
    clock.tick(60)

client_socket.close()'''

import pygame
import socket

# Sustituye con la IP correcta de la Raspberry Pi Pico W
pico_ip = "192.168.43.104"  # Cambia a la dirección IP de tu Pico W
pico_port = 8080

# Iniciar la conexión del socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((pico_ip, pico_port))
    print("Conexión establecida con la Pico.")
except (socket.timeout, ConnectionRefusedError, socket.error) as e:
    print(f"No se pudo conectar a {pico_ip}:{pico_port}. Verifica el servidor o la red. Error: {e}")
    client_socket.close()  # Cierra si falla la conexión

# Inicializa Pygame
'''pygame.init()
clock = pygame.time.Clock()
running = True

# Función para enviar comandos
def send_command(command):
    try:
        client_socket.send(command.encode())
    except socket.error as e:
        print(f"Error al enviar el comando: {e}")

# Ejemplo de uso en el ciclo
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                send_command("FLIPPER_ON")
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE:
                send_command("FLIPPER_OFF")
                
    pygame.display.flip()
    clock.tick(60)

# Cerrar el socket y salir de Pygame
client_socket.close()
pygame.quit()'''
