import pygame
from random import randint
pygame.init()
x = 470  #valor maximo 600 #valor minimo 360 #centro 470
y = 300
pos_x = 526
pos_y = 800
pos_y_a = 800
pos_y_c = 800

velocidade = 15

velocidade_outros = 20
fundo = pygame.image.load('pista.png')
carro = pygame.image.load('carro1 (4).png')
carro_vermelho = pygame.image.load('carros2 (4).png')
ambulancia = pygame.image.load('carros2 (5).png')
carro_amarelo = pygame.image.load('carros2 (6).png')

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x <= 600:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 351:
        x -= velocidade

    if (pos_y <= -200) and (pos_y_a <= -200) and (pos_y_c <= -200):
        pos_y = randint(800,2000)
        pos_y_a = randint(800,1850)
        pos_y_c = randint(800,1500)

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +5
    pos_y_c -= velocidade_outros +10

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(carro_vermelho,(pos_x - 210, pos_y))
    janela.blit(ambulancia,(pos_x - 170, pos_y_a))
    janela.blit(carro_amarelo,(pos_x - 70, pos_y_c))
    pygame.display.update()

pygame.quit()