from time import sleep
import pynput.mouse as ms
import pynput.keyboard as tc

mouse = ms.Controller()
teclado = tc.Controller()
ultimaPosicaoMouse = mouse.position
direcao = True

def verificarPosicaoMouse():
    global mouse
    return mouse.position

def verificarMouseParadoDoisMinutos():
    global ultimaPosicaoMouse

    sleep(55)
    if(ultimaPosicaoMouse == verificarPosicaoMouse()):
        ultimaPosicaoMouse = verificarPosicaoMouse()
        ativarFantasma()        
    else:
        ultimaPosicaoMouse = verificarPosicaoMouse()
    return verificarMouseParadoDoisMinutos()

def ativarFantasma():
    global direcao
    global teclado

    if(direcao):
        mouse.move(300,20)
        direcao = False
    else:
        mouse.move(-300,-20)
        direcao = True
    teclado.press(tc.Key.f5)
    teclado.release(tc.Key.f5)
    return

verificarMouseParadoDoisMinutos()