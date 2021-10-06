import pygame
from random import randint
pygame.init()
x = 250  #valor maximo 600 #valor minimo 360 #centro 470
y = 270
pos_x = 526
pos_y = 1500
pos_y_a = 800
pos_y_c = 2000
timer = 0
tempo_segundo = 0

velocidade = 15

velocidade_outros = 20
fundo = pygame.image.load('pista.png')
carro = pygame.image.load('carros2 (11).png')
carro_vermelho = pygame.image.load('carros2 (13).png')
ambulancia = pygame.image.load('carros2 (12).png')
policia = pygame.image.load('carros2 (10).png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo:",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_RIGHT] and x <= 350:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 141:
        x -= velocidade

    #detecta colisao

    if ((x + 300 > pos_x and y + 15 > pos_y)): # colisao lado direito
        y = 1200

    if ((x - 15 < pos_x - 400 and y + 2 > pos_y_a)): #colisao lado esquerdo
        y = 1200

   # if ((x + 40 > pos_x and y + 20 > pos_y))or((x - 20 < pos_x - 270 and y + 2 > pos_y_a)):


    if (pos_y <= -120) :
        pos_y = randint(800,1000)

    if ((pos_y_a <= -270)):
        pos_y_a = randint(1200,2000)

    if ((pos_y_c <= -120)):
        pos_y_c = randint(2200,3000)

    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render("Tempo:"+str(tempo_segundo),True,(255,255,255),(0,0,0))
        timer = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +5
    pos_y_c -= velocidade_outros +10

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(carro_vermelho,(pos_x - 360, pos_y))
    janela.blit(ambulancia,(pos_x - 190, pos_y_a))
    janela.blit(policia,(pos_x + 20, pos_y_c))
    janela.blit(texto,pos_texto)
    pygame.display.update()

pygame.quit()


