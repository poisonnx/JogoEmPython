import pygame
pygame.init()
x = 400
y = 300
pos_x = 350
pos_y = 300
velocidade = 15
velocidade_outros = 20
fundo = pygame.image.load('Apresentação1.png')
carro = pygame.image.load('carro1 (4).png')
policia = pygame.image.load('carros2 (4).png')
ambulancia = pygame.image.load('carros2 (5).png')
carro_amarelo = pygame.image.load('carros2 (6).png')
carro_preto = pygame.image.load('carros2 (7).png')
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade

    if (pos_y <= -200):
        pos_y = 600

    pos_y -= velocidade_outros

    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(policia,(pos_x - 200, pos_y))
    janela.blit(ambulancia,(pos_x + 150, pos_y))
    janela.blit(carro_amarelo,(pos_x + 135, pos_y))
    janela.blit(carro_preto,(pos_x,pos_y))
    pygame.display.update()

pygame.quit()
