import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#variaveis/tamanho

largura = 640
altura = 480
titulo_janela = "Slither.io"


#informações da cobrinha
x_snake = largura/2
y_snake = altura/2
width_snake = height_snake = 20
lista_snake = []



#informações da maçã
x_maca = randint(40, 600)
y_maca = randint(40, 440)
width_maca = height_maca = 20

fonte = pygame.font.SysFont('arial', 20, True, False)
pontos = 0


#informações movimento
velocidade = 10 
movimento_x = velocidade
movimento_y = 0

key_a = False
key_s = False
key_w = False
key_d = True

def reiniciar_jogo():
    global pontod, x_snake, y_snake, lista_cabeca_snake, lista_snake, x_maca, y_maca, perdeu, velocidade, key_a, key_d, key_s, key_w
     
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption(titulo_janela)
relogio = pygame.time.Clock()



while True:
   
    tela.fill((255,255,255))
    relogio.tick(30)
    mensagem = f'pontos: {pontos}'
    caixa_texto = fonte.render(mensagem, True, (0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
       
        if event.type == KEYDOWN:
            if event.key == K_a and not(key_d):
                movimento_x = -velocidade
                movimento_y = 0
                key_d = key_s = key_w= False
                key_a = True
                
            elif event.key == K_d and not(key_a):
                movimento_x = velocidade
                movimento_y = 0
                key_a = key_s = key_w= False
                key_d = True
                
            elif event.key == K_w and not(key_s):
                movimento_x = 0
                movimento_y = -velocidade
                key_a = key_s = key_d= False
                key_w = True
                
            elif event.key == K_s and not(key_w):
                movimento_x = 0
                movimento_y = velocidade
                key_a = key_w = key_d= False
                key_s = True
    
    x_snake += movimento_x
    y_snake += movimento_y        
            
    # if pygame.key.get_pressed()[K_a]:
    #     x_snake -= 10
    # elif pygame.key.get_pressed()[K_d]:
    #     x_snake += 10
    # elif pygame.key.get_pressed()[K_w]:
    #     y_snake -= 10
    # elif pygame.key.get_pressed()[K_s]:
    #     y_snake += 10
   
    
    
    snake = pygame.draw.rect(tela, (0,255,0), (x_snake, y_snake, width_snake, height_snake))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, width_maca, height_maca))
    
    if snake.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(40,440)    
        pontos += 1
    
    
    if len(lista_snake) > pontos:
        del lista_snake[0]
    
    lista_cabeca_snake = []
    lista_cabeca_snake.append(x_snake)
    lista_cabeca_snake.append(y_snake)
    
   
    lista_snake.append(lista_cabeca_snake)
    
    for XeY in lista_snake:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], width_snake, height_snake))
    
    
    
    if lista_snake.count(lista_cabeca_snake) > 1:
        faleceu = True
        
        while faleceu:
            tela.fill((0,0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        perdeu= False
                    
    
    if x_snake > largura:
        x_snake = 0
    if x_snake < 0:
        x_snake = largura
    if y_snake > altura:
        y_snake = 0
    if y_snake < 0:
        y_snake = altura
    
    
    tela.blit(caixa_texto, (400,40))
    pygame.display.update()