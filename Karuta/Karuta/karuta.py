import pyautogui
import time

#posicao mouse goole = x=469, y=931
#posicao mouse opera = x=481, y=931
#posicao mouse brave = x=592, y=898

pyautogui.press("win")
time.sleep(1)
pyautogui.write("google")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("discord")
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=17, y=183)

time.sleep(4)

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

time.sleep(4)

pyautogui.press("win")
pyautogui.write("opera gx")
pyautogui.press("enter")
time.sleep(4)
pyautogui.write("discord")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=83, y=221)
time.sleep(0.7)
pyautogui.click(x=208, y=296)
time.sleep(1)

#começo do for

def executar_picks():

    # Primeiro pick - Opera @ZumbiBaiano  30 min 10 min
    pyautogui.click(x=1656, y=604)
    time.sleep(1.5)
    pyautogui.hotkey("Fn","end")
    time.sleep(2)
    pyautogui.click(x=504, y=998)
    time.sleep(3)
    pyautogui.write("kd")
    pyautogui.press("enter")
    time.sleep(7)
    pyautogui.click(x=454, y=936) # pegar cartas
    time.sleep(2)
    pyautogui.hotkey("alt", "tab")

# Segundo pick - Brave @willo 10 min
    pyautogui.click(x=1656, y=604)
    time.sleep(1.5)
    pyautogui.hotkey("Fn","end")
    time.sleep(7)
    pyautogui.click(x=458, y=895) # pegar cartas
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

# Terceiro pick - Google @ZumbiBaiano_Drop 10 min
    pyautogui.click(x=1656, y=604)
    time.sleep(1.5)
    pyautogui.hotkey("Fn","end")
    pyautogui.scroll(-10000) 
    time.sleep(7)
    pyautogui.click(x=508, y=871) # pegar cartas
    time.sleep(800)

# 2 - Repetição de picks - Google ZumbiBaiano_Drop 30 min 10 min
    pyautogui.click(x=1656, y=604)
    time.sleep(1.5)
    pyautogui.hotkey("Fn","end")
    time(1.5)
    pyautogui.click(x=605, y=987)
    time.sleep(5)
    pyautogui.write("kd")
    pyautogui.press("enter")
    time.sleep(7)
    pyautogui.click(x=454, y=936)
    time.sleep(2)

# voltar pro opera e pegar a 2 carta - OPERA Zumbi_Baiano 20 min 10 min

    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    time.sleep(3)
    pyautogui.click(x=1656, y=604)
    time.sleep(1.5)
    pyautogui.hotkey("Fn","end")
    time.sleep(5)
    pyautogui.click(x=458, y=895)
    time.sleep(2)

# 2 pick brave @Willo 10 min

    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    time.sleep(3)
    pyautogui.click(x=1656, y=604)
    time.sleep(1.5)
    pyautogui.hotkey("Fn","end")
    time.sleep(5)
    pyautogui.click(x=508, y=871)
    time.sleep(2)

    time.sleep(800)

# 3 - Repitação comecando pelo brave e tem q termina com o opera - Brave Willo 30 min 10 min
        
    pyautogui.click(x=1656, y=604)
    time.sleep(1.5)
    pyautogui.hotkey("Fn","end") 
    time.sleep(3)
    pyautogui.click(x=521, y=990)
    time.sleep(3)
    pyautogui.write("kd")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=454, y=936)
    time.sleep(3)

# alt tab pro chrome e pegar o 2 drop - ZumbiBaiano_drop 20 min 10 min

    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.keyUp('alt')   
    time.sleep(3)   
    pyautogui.click(x=1656, y=604)
    time.sleep(1.5)
    pyautogui.hotkey("Fn","end")
    time.sleep(5)
    pyautogui.click(x=458, y=895)
    time.sleep(2)

# alt tab pro Opera e Reiniciar o ciclo - ZumbiBaiano 10 min 10 min

    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    time.sleep(5)
    pyautogui.click(x=1656, y=604)
    time.sleep(1.5)
    pyautogui.hotkey("Fn","end")
    time.sleep(3)
    pyautogui.click(x=508, y=871)
    

    time.sleep(800)

    pyautogui.scroll(-10000) 
    
while True:
    executar_picks()