# Proyecto 1, Fundamentos de Sistemas Computacionales.
# CES Pinball
# Autores: Edgar Hernández Fallas, Evans Josué Corrales Valverde.
# Fecha de reación: Viernes 04 de octubre, 2024.
# Fecha de entrega: jueves 24 de octubre, 2024.

# Fecha de actualización 1: miércoles 09 de octubre, 2024
# Versión: Beta: 0.2.0

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

# Varible que determina si la configuración inicial ya se realizó.
ver_config = False

# Initialize the Pygame mixer for playing music
pygame.mixer.init()

# Create the main window
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Load the background image
fondo = pygame.image.load("8-bit style pinball game interface.png")

# Load the background music and start playing it
'''try:
    pista1 = pygame.mixer.music.load("Slushii - LUV U NEED U [Monstercat Release].mp3")
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Error loading music file: {e}")'''

# Set the font for the button text
fuente = pygame.font.Font(None, 36)

# Ventana acerca de y sus características.
ventana_about = pygame.Surface((600, 400))
font = pygame.font.Font(None, 24)
titulo = font.render("CES Pinball", True, blanco)
ventana_about.blit(titulo, (20, 20))
autores = font.render("Autores: Evans Corrales Valverde y Edgar Hernández Fállas", True, blanco)
ventana_about.blit(autores, (20, 40))
version = font.render("Versión: Beta 0.2.0", True, blanco)
ventana_about.blit(version, (20, 60))
escuela = font.render("Ingeniería en Computadores", True, blanco)
ventana_about.blit(escuela, (20, 80))
esc = font.render("Presione esc para salir", True, blanco)
ventana_about.blit(esc, (380, 350))

fondo_configuracion_inicial = pygame.image.load("un simple fondo liso celeste en estilo 8 bits sin figuras.png")


# Function to draw the background
def dibujar_fondo(pantalla, fondo_pantalla):
    pantalla.blit(fondo_pantalla, (0, 0))

# Function to draw the button
def dibujar_boton_acerca_de(pantalla, fuente, ejex, ejey, ancho, alto):
    pygame.draw.rect(pantalla, blanco, (ejex, ejey, ancho, alto))
    pygame.draw.rect(pantalla, negro, (ejex + 2, ejey + 2, ancho - 4, alto - 4))  
    button_surf = fuente.render("Acerca de", True, blanco)
    pantalla.blit(button_surf, (ejex + 10, ejey + 10))


clock = pygame.time.Clock()
running = True
acercade_open = False  # Initialize the variable to track the "Acerca de" window state


# Función de selección de jugadores
# Add a button for changing player selection
def dibujar_boton_cambiar_jugador(pantalla, fuente, ejex, ejey, ancho, alto):
    pygame.draw.rect(pantalla, blanco, (ejex, ejey, ancho + 84, alto))
    pygame.draw.rect(pantalla, negro, (ejex + 2, ejey + 2, ancho + 80, alto - 4))  
    button_surf = fuente.render("Cambiar Jugador", True, blanco)
    pantalla.blit(button_surf, (ejex + 10, ejey + 10))

# Modify the game loop to include the button
def game(running, botonx, ancho_boton, botony, alto_boton):
    global acercade_open, jugadores, jugador_seleccionado, ver_config 
    jugador_seleccionado = 0  # Initialize player selection
    jugadores = ["Jugador 1", "Jugador 2"]

    ver_config = config_inicial(ver_config)
    
    while running:
        # Event handling
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Check if the button acerca_de has been pressed 
                if botonx <= evento.pos[0] <= botonx + ancho_boton and botony <= evento.pos[1] <= botony + alto_boton:
                    # Display the "Acerca de" window
                    acercade_open = True
                # Check if the change player button has been pressed
                if 30 <= evento.pos[0] <= 30 + ancho_boton and 100 <= evento.pos[1] <= 100 + alto_boton:
                    seleccion()  # Call the selection function
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    acercade_open = False

        # Clear the screen and redraw the background and button
        dibujar_fondo(pantalla, fondo)
        dibujar_boton_acerca_de(pantalla, fuente, botonx, botony, ancho_boton, alto_boton)
        dibujar_boton_cambiar_jugador(pantalla, fuente, 30, 100, ancho_boton, alto_boton)  # Draw the change player button
        jugador_en_turno(pantalla, jugador_seleccionado)

        # If the "Acerca de" window is open, draw it
        if acercade_open:
            pantalla.blit(ventana_about, (ancho_pantalla // 2 - 300, alto_pantalla // 2 - 500))
        else:
            dibujar_fondo(pantalla, fondo)
            dibujar_boton_acerca_de(pantalla, fuente, botonx, botony, ancho_boton, alto_boton)
            dibujar_boton_cambiar_jugador(pantalla, fuente, 30, 100, ancho_boton, alto_boton)  # Draw the change player button
            jugador_en_turno(pantalla, jugador_seleccionado)

        # Update the interface
        pygame.display.flip()
        clock.tick(60)  # Control the game speed


# Modify the seleccion function to allow quitting
def seleccion():
    global jugador_seleccionado, jugadores
    estado_seleccion = True  # Variable that determines the state of player selection
    while estado_seleccion:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                estado_seleccion = False
                return  # Exit the function if the game is closed
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    jugador_seleccionado = (jugador_seleccionado - 1) % 2  # Cycle left
                elif evento.key == pygame.K_DOWN:
                    jugador_seleccionado = (jugador_seleccionado + 1) % 2  # Cycle right
                elif evento.key == pygame.K_RETURN:
                    # Here you can handle the selection (e.g., start the game)
                    print(f"{jugadores[jugador_seleccionado]} seleccionado.")
                    estado_seleccion = False  # Exit the selection window

        # Clear the screen
        dibujar_fondo(pantalla, fondo)

        # Draw the player selection text
        font = pygame.font.Font(None, 48)
        title = font.render("Selecciona tu jugador", True, blanco)
        pantalla.blit(title, (ancho_pantalla // 2 - title.get_width() // 2, alto_pantalla // 2 - 100))

        # Highlight the selected player
        for i, name in enumerate(jugadores):
            color = blanco if i == jugador_seleccionado else negro
            texto_jugador = font.render(name, True, color)
            pantalla.blit(texto_jugador, (ancho_pantalla // 2 - texto_jugador.get_width() // 2, alto_pantalla // 2 + i * 50))

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Control the game spe90
# Representación del jugador en turno.
jugador1_imagen = pygame.image.load("Gon from HunterxHunter, 8-bit style, head only, looking left.png")
jugador2_imagen = pygame.image.load("la cabeza de Killua de HunterxHunter en 2d, con un estilo de 8bits.png")

def jugador_en_turno(pantalla, jugador_seleccionado):
    pygame.draw.rect(pantalla, blanco, (825, 10, 180, 150))
    pygame.draw.rect(pantalla, negro, (815, 12, 190, 145))
    font = pygame.font.Font(None, 38)
    texto_jugador1 = font.render("Jugador 1", True, blanco)
    texto_jugador2 = font.render("Jugador 2", True, blanco)

    # Determinando la imagen del jugador. 
    if jugador_seleccionado == 0:
        imagen_jugador = jugador1_imagen
        pantalla.blit(texto_jugador1, (845, 165))
    else:
        imagen_jugador = jugador2_imagen
        pantalla.blit(texto_jugador2, (845, 165))

    # Adimensionar la imagen para que se acople a las del rectangulo.
    imagen_jugador = pygame.transform.scale(imagen_jugador, (170, 140))

    # Desplegar la imagen del jugador.
    pantalla.blit(imagen_jugador, (830, 15))


# Ahora toca continuar con la configuración inicial. Por terminar.


def config_inicial(ver_config):
    if ver_config:
        return
    else:
        opciones = ["Iniciar Juego", "Opciones de juego", "Ayuda", "Salir"]
        seleccion = 0  # Track the currently selected option
        waiting = True

        while waiting:
            # Draw the configuration background
            dibujar_fondo(pantalla, fondo_configuracion_inicial)

            # Draw the title
            font = pygame.font.Font(None, 48)
            ces = font.render("CES Pinball", True, blanco)
            pantalla.blit(ces, (420, 130))
            title = font.render("Configuración Inicial", True, blanco)
            pantalla.blit(title, (ancho_pantalla // 2 - title.get_width() // 2, alto_pantalla // 2 - 200))

            # Draw options
            for index, opcion in enumerate(opciones):
                color = blanco if index == seleccion else negro
                option_text = font.render(opcion, True, color)
                pantalla.blit(option_text, (ancho_pantalla // 2 - option_text.get_width() // 2, alto_pantalla // 2 + index * 50))

            # Update the display
            pygame.display.flip()

            # Event handling
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        seleccion = (seleccion - 1) % len(opciones)  # Move up the list
                    elif evento.key == pygame.K_DOWN:
                        seleccion = (seleccion + 1) % len(opciones)  # Move down the list
                    elif evento.key == pygame.K_RETURN:
                        if seleccion == 0:  # Comienza el juego
                            waiting = False
                        elif seleccion == 1:
                            seleccion_modo_juego = modo_juego()
                        elif seleccion == 2:
                            info_inicial()
                        elif seleccion == 3:  # Exit option
                            pygame.quit()
                            exit()


# Función información inical.
# Esta función brindará información sobre el juego como tal.
# Entradas: no posee entradas.
# Salidas: no posee salidas.
# Restricciones: no posee restricciones.
ventana_info_inicial = pygame.Surface((800, 600))
texto_info_inicial = ["El juego CES Pinball fue creado con la intención de incorporar la era digital con los juegos de arcade antiguos.",
"Por lo mismo nos complace traer este juego que posee características de las máquinas conocidas como Pinball con la electrónica digital.",
"El juego consiste en utilizar la maqueta que se le presenta a usted junto con el juego en pantalla.",
"Actualmente se encuentra dentro de la pestaña de configuración inicial en la cual podrá seleccionar el modo de juego, para un jugador o dos jugadores", 
"Una vez modo haya concluido con el modo de juego podrá irse a la pestaña de selección de personaje, la cual se realiza utilizando el potenciómetro de la maqueta.",
"Una vez realizado, lo anterior podrá decidir si iniciar, el juego, cambiar de modo de juego, volver a seleccionar personajes o salir.",
"Si desea iniciar el juego, entonces ahora podrá ver como se refleja en la pantalla el jugador en turno y la cantidad de tiros disponibles.",
"Normalmente durante la ejecución del juego cada jugador posee tres tiros, una vez termina esos tres tiros cambia el turno."
,"También se tiene en la pantalla la ventana de about o acerca por si desea conocer más sobre los creadores."]


# Función separar_texto_info inicial.
# Esta función busca que el texto que aparece en la ventana de ayuda sea legible.

def sep_texto_info_inicial():
    character_quantity = ""
    texto_final = []
    texto_total = ""
    for cadena in texto_info_inicial:
        texto_total += cadena

    while texto_total != "" and len(texto_total) < 120:
        for indice, caracter in enumerate(texto_total):
            character_quantity += caracter
            if len(character_quantity) >= 120 and (caracter == " " or caracter == "," or caracter == "."):
                texto_final += [character_quantity]
                texto_total = texto_total[len(character_quantity):]
                character_quantity = ""
                break
    texto_final += texto_total
    return texto_final

print(sep_texto_info_inicial())


# Falta trabajar en el texto.
def info_inicial():
    global blanco, negro
    salir = False
    font = pygame.font.Font(None, 24)
    
    # Fill the info surface with a background color (optional)
    ventana_info_inicial.fill(negro)  # Fill with black or any color you want

    while not salir:
        # Draw the info surface on the main screen
        pantalla.blit(ventana_info_inicial, (200, 300))
        
        # Render the text
        sobre_el_juego = font.render("Sobre el juego: Ces Pinball", True, blanco)    
        ventana_info_inicial.blit(sobre_el_juego, (10, 10))  # Adjust the position as needed
        espacio_inter = 30
        texto_desplegar = sep_texto_info_inicial
        for texto in texto_desplegar:
            texto_imp = font.render(texto, True, blanco)
            ventana_info_inicial.blit(texto_imp, (10, espacio_inter))
            espacio_inter += 20

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    salir = True  # Corrected assignment

        # Update the display
        pygame.display.flip()  # Ensure the display is updated




# Función modo_juego.
# Función que define el modo de juego en el que se irá a jugar.
# Entradas: ninguna.
# Salidas: el valor de la selección del modo de juego.
# Restricciones: no posee restricciones
def modo_juego():
    selecto = False
    seleccion_modo_juego = 0
    dibujar_fondo(pantalla, fondo_configuracion_inicial)
    while not selecto:
        font = pygame.font.Font(None, 48)
        title = font.render("Opciones de juego", True, blanco)
        pantalla.blit(title, (ancho_pantalla // 2 - title.get_width() // 2, alto_pantalla // 2 - 350))
        opciones_juego = ["1 jugador", "2 jugadores"]
        for index, opcion_juego in enumerate(opciones_juego):
            color = blanco if index == seleccion_modo_juego else negro
            option_mode_text =  font.render(opcion_juego, True, color)
            pantalla.blit(option_mode_text, (ancho_pantalla // 2 - option_mode_text.get_width() + 80,
            alto_pantalla // 2 + index * 50 + 100))
        pygame.display.flip()
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()   
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        seleccion_modo_juego = 0  # Move up the list
                    elif evento.key == pygame.K_DOWN:
                        seleccion_modo_juego = 1  # Move down the list
                    elif evento.key == pygame.K_RETURN:
                        print(seleccion_modo_juego)
                        selecto = True
                        return seleccion_modo_juego  # Choose the option
                            



game(running, botonx, ancho_boton, botony, alto_boton)

# Quit Pygame
pygame.quit()

