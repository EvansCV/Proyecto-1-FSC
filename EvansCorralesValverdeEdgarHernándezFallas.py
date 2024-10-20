# Proyecto 1, Fundamentos de Sistemas Computacionales.
# CES Pinball
# Autores: Edgar Hernández Fallas, Evans Josué Corrales Valverde.
# Fecha de reación: Viernes 04 de octubre, 2024.
# Fecha de entrega: jueves 24 de octubre, 2024.

# Fecha de actualización 1: miércoles 09 de octubre, 2024
# Versión: Beta: 0.0.1

# Import the Pygame library and initialize it
'''import pygame
pygame.init()

# Constantes
ancho_pantalla = 1025
alto_pantalla = 1200
ancho_boton = 140
alto_boton = 40
botonx = 30
botony = 30
blanco = (255, 255, 255)
negro = (20, 20, 20)

# Initialize the Pygame mixer for playing music
pygame.mixer.init()

# Create the main window with a size of SCREEN_WIDTHxSCREEN_HEIGHT pixels
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Load the background image
fondo = pygame.image.load("8-bit style pinball game interface.png")

# Load the background music and start playing it
try:
    pista1 = pygame.mixer.music.load("Slushii - LUV U NEED U [Monstercat Release].mp3")
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Error loading music file: {e}")

# Set the font for the button text
fuente = pygame.font.Font(None, 36)

# Crea la ventana "Acerca de"
ventana_about = pygame.Surface((600, 400))
font = pygame.font.Font(None, 24)
titulo = font.render("Sobre nosotros", True, blanco)
ventana_about.blit(titulo, (20, 20))
autores = font.render("Autores: Evans Corrales Valverde y Edgar Hernández Fállas", True, blanco)
ventana_about.blit(autores, (20, 40))


# Función para dibujar el fondo.
def dibujar_fondo(pantalla, fondo):
    pantalla.blit(fondo, (0, 0))

# Function to draw the button
def dibujar_boton_acerca_de(pantalla, fuente, ejex, ejey, ancho, alto):
    pygame.draw.rect(pantalla, blanco, (ejex, ejey, ancho, alto))
    # Llena el botón con color negro.
    pygame.draw.rect(pantalla, negro, (ejex + 2, ejey + 2, ancho - 4, alto - 4))  

    button_surf = fuente.render("Acerca de", True, blanco)
    pantalla.blit(button_surf, (ejex + 10, ejey + 10))

    pygame.display.flip()  # Actualiza la pantalla


# Dibuja el fondo del
dibujar_fondo(pantalla, fondo)

# Dibuja el boton acerca_de 
dibujar_boton_acerca_de(pantalla, fuente, botonx, botony, ancho_boton, alto_boton)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Comprueba si el botón ha sido presionado 
            if botonx <= evento.pos[0] <= botonx + ancho_boton and botony <= evento.pos[1] <= botony + alto_boton:
                # Despliega la ventana de "Acerca de"
                acercade_open = True
                pantalla.blit(ventana_about, (ancho_pantalla // 2 - 300, alto_pantalla // 2 - 450)) 
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                acercade_open = False

if acercade_open:
    pantalla.blit(ventana_about, (ancho_pantalla // 2 - 200, alto_pantalla // 2 -150))

    # Actualiza la interfaz.
    pygame.display.flip()
    clock.tick(60)  # Control the game speed

# Quit Pygame
pygame.quit()'''

# Import the Pygame library and initialize it
import pygame
pygame.init()

# Constants
ancho_pantalla = 1025
alto_pantalla = 1200
ancho_boton = 140
alto_boton = 40
botonx = 30
botony = 30
blanco = (255, 255, 255)
negro = (20, 20, 20)

# Initialize the Pygame mixer for playing music
pygame.mixer.init()

# Create the main window
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Load the background image
fondo = pygame.image.load("8-bit style pinball game interface.png")

# Load the background music and start playing it
try:
    pista1 = pygame.mixer.music.load("Slushii - LUV U NEED U [Monstercat Release].mp3")
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Error loading music file: {e}")

# Set the font for the button text
fuente = pygame.font.Font(None, 36)

# Create the "Acerca de" window
ventana_about = pygame.Surface((600, 400))
font = pygame.font.Font(None, 24)
titulo = font.render("Sobre nosotros", True, blanco)
ventana_about.blit(titulo, (20, 20))
autores = font.render("Autores: Evans Corrales Valverde y Edgar Hernández Fállas", True, blanco)
ventana_about.blit(autores, (20, 40))

# Function to draw the background
def dibujar_fondo(pantalla, fondo):
    pantalla.blit(fondo, (0, 0))

# Function to draw the button
def dibujar_boton_acerca_de(pantalla, fuente, ejex, ejey, ancho, alto):
    pygame.draw.rect(pantalla, blanco, (ejex, ejey, ancho, alto))
    pygame.draw.rect(pantalla, negro, (ejex + 2, ejey + 2, ancho - 4, alto - 4))  
    button_surf = fuente.render("Acerca de", True, blanco)
    pantalla.blit(button_surf, (ejex + 10, ejey + 10))

# Draw the background
dibujar_fondo(pantalla, fondo)

# Draw the button
dibujar_boton_acerca_de(pantalla, fuente, botonx, botony, ancho_boton, alto_boton)

# Main game loop
clock = pygame.time.Clock()
running = True
acercade_open = False  # Initialize the variable to track the "Acerca de" window state

while running:
    # Event handling
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button has been pressed 
            if botonx <= evento.pos[0] <= botonx + ancho_boton and botony <= evento.pos[1] <= botony + alto_boton:
                # Display the "Acerca de" window
                acercade_open = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:  # Correctly check for the Escape key
                acercade_open = False

    # Clear the screen and redraw the background and button
    dibujar_fondo(pantalla, fondo)
    dibujar_boton_acerca_de(pantalla, fuente, botonx, botony, ancho_boton, alto_boton)

    # If the "Acerca de" window is open, draw it
    if acercade_open:
        pantalla.blit(ventana_about, (ancho_pantalla // 2 - 300, alto_pantalla // 2 - 500))

    # Update the interface
    pygame.display.flip()
    clock.tick(60)  # Control the game speed

# Quit Pygame
pygame.quit()