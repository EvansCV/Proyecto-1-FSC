class Config_inicial:

    import pygame
    # Constants for the initial configuration
    blanco = (255, 255, 255)
    negro = (20, 20, 20)
    
    texto_info_inicial = [
        "El juego CES Pinball fue creado con la intención de incorporar la era digital con los juegos de arcade antiguos.",
        "Por lo mismo nos complace traer este juego que posee características de las máquinas conocidas como Pinball con la electrónica digital.",
        "El juego consiste en utilizar la maqueta que se le presenta a usted junto con el juego en pantalla.",
        "Actualmente se encuentra dentro de la pestaña de configuración inicial en la cual podrá seleccionar el modo de juego, para un jugador o dos jugadores", 
        "Una vez modo haya concluido con el modo de juego podrá irse a la pestaña de selección de personaje, la cual se realiza utilizando el potenciómetro de la maqueta.",
        "Una vez realizado, lo anterior podrá decidir si iniciar, el juego, cambiar de modo de juego, volver a seleccionar personajes o salir.",
        "Si desea iniciar el juego, entonces ahora podrá ver como se refleja en la pantalla el jugador en turno y la cantidad de tiros disponibles.",
        "Normalmente durante la ejecución del juego cada jugador posee tres tiros, una vez termina esos tres tiros cambia el turno.",
        "También se tiene en la pantalla la ventana de about o acerca de por si desea conocer más sobre los creadores."
    ]

    # Initial configuration background
    fondo_configuracion_inicial = pygame.image.load("un simple fondo liso celeste en estilo 8 bits sin figuras.png")

    def __init__(self, pantalla, fuente):
        self.pantalla = pantalla
        self.fuente = fuente
        self.ventana_info_inicial = self.pygame.Surface((1000, 300))

    def sep_texto_info_inicial(self):
        texto_final = []
        texto_total = "".join(self.texto_info_inicial)
        character_quantity = ""
        
        for caracter in texto_total:
            character_quantity += caracter
            if len(character_quantity) >= 120 and caracter in " ,.":
                texto_final.append(character_quantity)
                character_quantity = ""
        
        texto_final.append(character_quantity)
        return texto_final

    def info_inicial(self):
        salir = False
        font = self.pygame.font.Font(None, 24)
        
        self.ventana_info_inicial.fill(self.negro) 

        while not salir:
            self.pantalla.blit(self.ventana_info_inicial, (0, 200))
            sobre_el_juego = font.render("Sobre el juego: Ces Pinball", True, self.blanco)
            self.ventana_info_inicial.blit(sobre_el_juego, (10, 10))
            espacio_inter = 30
            texto_desplegar = self.sep_texto_info_inicial()
            
            for texto in texto_desplegar:
                texto_imp = font.render(texto, True, self.blanco)
                self.ventana_info_inicial.blit(texto_imp, (10, espacio_inter))
                espacio_inter += 20
            
            esc = font.render("Presione esc para salir", True, self.blanco)
            self.ventana_info_inicial.blit(esc, (780, 280))

            for evento in self.pygame.event.get():
                if evento.type == self.pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == self.pygame.KEYDOWN and evento.key == self.pygame.K_ESCAPE:
                    salir = True

            self.pygame.display.flip()

    def config_inicial(self, ver_config):
        if ver_config:
            return
        else:
            opciones = ["Iniciar Juego", "Opciones de juego", "Ayuda", "Salir"]
            seleccion = 0
            waiting = True

            while waiting:
                self.dibujar_fondo(self.fondo_configuracion_inicial)
                font = self.pygame.font.Font(None, 36)
                ces = font.render("CES Pinball", True, self.blanco)
                self.pantalla.blit(ces, (330, 40))
                title = font.render("Configuración Inicial", True, self.blanco)
                self.pantalla.blit(title, (self.pantalla.get_width() // 2 - title.get_width() // 2, self.pantalla.get_height() // 2 - 200))

                for index, opcion in enumerate(opciones):
                    color = self.blanco if index == seleccion else self.negro
                    option_text = font.render(opcion, True, color)
                    self.pantalla.blit(option_text, (self.pantalla.get_width() // 2 - option_text.get_width() // 2, self.pantalla.get_height() // 2 + index * 50))

                self.pygame.display.flip()

                for evento in self.pygame.event.get():
                    if evento.type == self.pygame.QUIT:
                        self.pygame.quit()
                        exit()
                    elif evento.type == self.pygame.KEYDOWN:
                        if evento.key == self.pygame.K_UP:
                            seleccion = (seleccion - 1) % len(opciones)
                        elif evento.key == self.pygame.K_DOWN:
                            seleccion = (seleccion + 1) % len(opciones)
                        elif evento.key == self.pygame.K_RETURN:
                            if seleccion == 0:
                                waiting = False
                            elif seleccion == 1:
                                self.modo_juego()
                            elif seleccion == 2:
                                self.info_inicial()
                            elif seleccion == 3:
                                self.pygame.quit()
                                exit()
    # Method for game mode selection
    def modo_juego(self):
        selecto = False
        seleccion_modo_juego = 0
        self.dibujar_fondo(self.fondo_configuracion_inicial)
        
        while not selecto:
            font = self.pygame.font.Font(None, 48)
            title = font.render("Opciones de juego", True, self.blanco)
            self.pantalla.blit(title, (self.pantalla.get_width() // 2 - title.get_width() // 2, self.pantalla.get_height() // 2 - 350))
            
            opciones_juego = ["1 jugador", "2 jugadores"]
            for index, opcion_juego in enumerate(opciones_juego):
                color = self.blanco if index == seleccion_modo_juego else self.negro
                option_mode_text = font.render(opcion_juego, True, color)
                self.pantalla.blit(option_mode_text, (self.pantalla.get_width() // 2 - option_mode_text.get_width() + 80,
                                                     self.pantalla.get_height() // 2 + index * 50 + 100))
            
            self.pygame.display.flip()
            
            for evento in self.pygame.event.get():
                if evento.type == self.pygame.QUIT:
                    self.pygame.quit()   
                    exit()
                elif evento.type == self.pygame.KEYDOWN:
                    if evento.key == self.pygame.K_UP:
                        seleccion_modo_juego = 0  # Move up the list
                    elif evento.key == self.pygame.K_DOWN:
                        seleccion_modo_juego = 1  # Move down the list
                    elif evento.key == self.pygame.K_RETURN:
                        print(seleccion_modo_juego)
                        selecto = True
                        return seleccion_modo_juego  # Choose the option

    def dibujar_fondo(self, fondo_pantalla):
        self.pantalla.blit(fondo_pantalla, (0, 0))
