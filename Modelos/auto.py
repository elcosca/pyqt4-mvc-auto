# -*- coding: utf-8 -*-

class Auto():

    def __init__(self):
        self.cantidad_personas = 0

    def subir_persona(self):
        self.cantidad_personas += 1

    def bajar_persona(self):
        self.cantidad_personas -= 1

    def subir_muchas_personas(self):
        self.cantidad_personas += 5

    def bajar_muchas_personas(self):
        self.cantidad_personas -= 5
