from time import sleep
from pynput.mouse import Controller

mouse = Controller()
ultimaPosicaoMouse = mouse.position
direcao = True

def verificarPosicaoMouse():
    global mouse
    return mouse.position

def verificarMouseParadoDoisMinutos():
    global ultimaPosicaoMouse

    sleep(3)
    if(ultimaPosicaoMouse == verificarPosicaoMouse()):
        ultimaPosicaoMouse = verificarPosicaoMouse()
        ativarFantasma()        
    else:
        ultimaPosicaoMouse = verificarPosicaoMouse()
    return verificarMouseParadoDoisMinutos()

def ativarFantasma():
    global direcao

    if(direcao):
        mouse.move(300,20)
        direcao = False
    else:
        mouse.move(-300,-20)
        direcao = True
    return

verificarMouseParadoDoisMinutos()