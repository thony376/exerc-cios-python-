import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

altura = 480
largura = 640
tituloJanela = "Primeiro Jogo"

#informações circulo
pos_x_circle = 200
pos_y_circle = 200
raio = 15
rgb_circle = 147,197,114


#informações Retangulo
pos_x_rect = 500
pos_y_rect = 200
width_rect = 25
height_rect = 25
rgb_rect = 141,182,0

fonte = pygame.font.SysFont('arial', 40, True, False)
pontos = 0

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption(tituloJanela)
relogio = pygame.time.Clock()

while True:
    
    relogio.tick(30)
    tela.fill((0,0,0))

    mensagem = f'pontos: {pontos}'
    caixaTexto = fonte.render(mensagem, False, (255,255,255))




    for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              exit()
              
    
        #   if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         pos_x_rect -= 10
        #     if event.key == K_d:
        #         pos_x_rect += 10
        #     if event.key == K_w:
        #         pos_y_rect -= 10
        #     if event.key == K_s:
        #         pos_y_rect += 10
              
    if pygame.key.get_pressed()[K_a]:
              pos_x_rect -= 10
        
    elif pygame.key.get_pressed()[K_d]:
              pos_x_rect += 10
              
    elif pygame.key.get_pressed()[K_w]:
              pos_y_rect -= 10
              
    elif pygame.key.get_pressed()[K_s]:
              pos_y_rect += 10
      
      
    if pos_x_rect >= largura:
        pos_x_rect = 0
        
    elif pos_x_rect <= 0:
        pos_x_rect = largura
        
    if pos_y_rect >= altura:
        pos_y_rect = 0
        
    elif pos_y_rect <=0:
        pos_y_rect = altura
    
    
        
    
      #criando um retangulo
    retangulo = pygame.draw.rect(tela, (rgb_rect), (pos_x_rect, pos_y_rect, width_rect, height_rect))
      
      
      #criando circulo
    circulo = pygame.draw.circle(tela, (rgb_circle), (pos_x_circle, pos_y_circle), raio)
      
    # if pos_y_rect >= altura:
    #       pos_x_rect = 0
          
          
    # pos_y_rect += 5
    if retangulo.colliderect(circulo):
        pos_x_circle = randint(40,600)
        pos_y_circle = randint(40,600)
        pontos += 1
        
        
        
    tela.blit(caixaTexto, (400,40))    
        
              
    
    pygame.display.update()