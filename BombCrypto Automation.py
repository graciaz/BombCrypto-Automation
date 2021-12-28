import pyautogui as pg
import time
import datetime
import random

def screen1():
    
    # Clear the error message
    pg.moveTo(270,240)
    time.sleep(2)
    pg.click()
    time.sleep(10)

    # Click on connect wallet
    pg.moveTo(270, 290)
    time.sleep(2)
    pg.click()
    time.sleep(2)

    # Click on Sign
    pg.moveTo(430, 560)
    time.sleep(5)
    pg.click()
    time.sleep(10)

    # Click on Back
    pg.moveTo(52, 65)
    time.sleep(3)
    pg.click()
    time.sleep(1)    

    # Click on Hero
    pg.moveTo(475, 320)
    time.sleep(3)
    pg.click()
    time.sleep(1)  

    # Scroll down
    pg.moveTo(185, 220)
    for i in range (45):
        pg.scroll(-1)

    # Click on Work
    time.sleep(1)    
    for i in range (16):
        pg.click(230, 300)
        time.sleep(1)

    # Click on Close
    pg.moveTo(300, 105)
    time.sleep(2)    
    pg.click()
    time.sleep(1)  

    # Click on Teasure Hunt 
    pg.moveTo(270, 200)
    time.sleep(4)    
    pg.click()
    time.sleep(1)  

    # Click on new map | In case of new map
    pg.moveTo(270, 240)
    time.sleep(5)
    pg.click()

def screen2():
    
    # Clear the error message
    pg.moveTo(270,640)
    time.sleep(2)
    pg.click()
    time.sleep(10)

    # Click on connect wallet
    pg.moveTo(270, 670)
    time.sleep(2)
    pg.click()
    time.sleep(2)

    # Click on Sign
    pg.moveTo(425, 940)
    time.sleep(5)
    pg.click()
    time.sleep(10)

    # Click on Back
    pg.moveTo(52, 450)
    time.sleep(3)
    pg.click()
    time.sleep(1)    

    # Click on Hero
    pg.moveTo(475, 700)
    time.sleep(3)
    pg.click()
    time.sleep(1)    

    # Scroll down
    pg.moveTo(185, 600)
    for i in range (45):
        pg.scroll(-1)

    # Click on Work
    time.sleep(1)    
    for i in range (16):
        pg.click(230, 685)
        time.sleep(1)

    # Click on Close
    pg.moveTo(300, 490)
    time.sleep(2)    
    pg.click()
    time.sleep(1)    

    # Click on Teasure Hunt 
    pg.moveTo(270, 580)
    time.sleep(4)    
    pg.click()
    time.sleep(1)    

    # Click on new map | In case of new map
    pg.moveTo(270, 640)
    time.sleep(5)
    pg.click()

def screen3():
    
    # Clear the error message
    pg.moveTo(790,240)
    time.sleep(2)
    pg.click()
    time.sleep(10)

    # Click on connect wallet
    pg.moveTo(790, 290)
    time.sleep(2)
    pg.click()
    time.sleep(2)

    # Click on Sign
    pg.moveTo(950, 560)
    time.sleep(5)
    pg.click()
    time.sleep(10)

    # Click on Back
    pg.moveTo(575, 65)
    time.sleep(3)
    pg.click()
    time.sleep(1)    

    # Click on Hero
    pg.moveTo(998, 320)
    time.sleep(3)
    pg.click()
    time.sleep(1)  

    # Scroll down
    pg.moveTo(720, 220)
    for i in range (45):
        pg.scroll(-1)

    # Click on Work
    time.sleep(1)    
    for i in range (16):
        pg.click(750, 300)
        time.sleep(1)

    # Click on Close
    pg.moveTo(820, 105)
    time.sleep(2)    
    pg.click()
    time.sleep(1)  

    # Click on Teasure Hunt 
    pg.moveTo(790, 200)
    time.sleep(4)    
    pg.click()
    time.sleep(1)  

    # Click on new map | In case of new map
    pg.moveTo(790, 240)
    time.sleep(5)
    pg.click()

def screen4():
    
    # Clear the error message
    pg.moveTo(790,640)
    time.sleep(2)
    pg.click()
    time.sleep(10)

    # Click on connect wallet
    pg.moveTo(790, 670)
    time.sleep(2)
    pg.click()
    time.sleep(2)

    # Click on Sign
    pg.moveTo(950, 940)
    time.sleep(5)
    pg.click()
    time.sleep(10)

    # Click on Back
    pg.moveTo(575, 450)
    time.sleep(3)
    pg.click()
    time.sleep(1)    

    # Click on Hero
    pg.moveTo(998, 700)
    time.sleep(3)
    pg.click()
    time.sleep(1)    

    # Scroll down
    pg.moveTo(720, 600)
    for i in range (45):
        pg.scroll(-1)

    # Click on Work
    time.sleep(1)    
    for i in range (16):
        pg.click(750, 685)
        time.sleep(1)

    # Click on Close
    pg.moveTo(820, 490)
    time.sleep(2)    
    pg.click()
    time.sleep(1)    

    # Click on Teasure Hunt 
    pg.moveTo(790, 580)
    time.sleep(4)    
    pg.click()
    time.sleep(1)    

    # Click on new map | In case of new map
    pg.moveTo(790, 640)
    time.sleep(5)
    pg.click()

def refresh():

    # Click on Back 1
    pg.moveTo(52, 65)
    time.sleep(3)
    pg.click()
    time.sleep(1)

    # Click on Teasure Hunt 1
    pg.moveTo(270, 200)
    time.sleep(4)    
    pg.click()
    time.sleep(1)  

    # Click on Back 2
    pg.moveTo(52, 450)
    time.sleep(3)
    pg.click()
    time.sleep(1) 

    # Click on Teasure Hunt 2
    pg.moveTo(270, 580)
    time.sleep(4)    
    pg.click()
    time.sleep(1)    

    # Click on Back 3
    pg.moveTo(575, 65)
    time.sleep(3)
    pg.click()
    time.sleep(1)

    # Click on Teasure Hunt 3
    pg.moveTo(790, 200)
    time.sleep(4)    
    pg.click()
    time.sleep(1)  

    # Click on Back 4
    pg.moveTo(575, 450)
    time.sleep(3)
    pg.click()
    time.sleep(1)    

    # Click on Teasure Hunt 4
    pg.moveTo(790, 580)
    time.sleep(4)    
    pg.click()
    time.sleep(1)   

loop = 1

print("Please set the screen to default position")
time.sleep(1)
print("..10")
time.sleep(1)
print("..9")
time.sleep(1)
print("..8")
time.sleep(1)
print("..7")
time.sleep(1)
print("..6")
time.sleep(1)
print("..5")
time.sleep(1)
print("..4")
time.sleep(1)
print("..3")
time.sleep(1)
print("..2")
time.sleep(1)
print("..1")
time.sleep(1)
print("\n=============================================")
time.sleep(1)


while True:
    print("\nBombCrypto Automation Start")
    cycletime = random.randint(15, 40)
    print("The automation will activate again in "+str(cycletime)+" minutes")
    print("The screen will auto refresh in every "+str(cycletime/5)+" minutes")


    print("Working on screen 1...")
    screen1()
    print("Working on screen 2...")
    screen2()
    print("Working on screen 3...")
    screen3()
    print("Working on screen 4...")
    screen4()

    ct = datetime.datetime.now()
    print("\nAwake: "+str(loop)+" Times on "+str(ct))


    time.sleep((cycletime*60)/5)
    print("The screen is refreshing... (1)")
    refresh()
    print("All screen refreshed")

    time.sleep((cycletime*60)/5)
    print("The screen is refreshing... (2)")
    refresh()
    print("All screen refreshed")

    time.sleep((cycletime*60)/5)
    print("The screen is refreshing... (3)")
    refresh()
    print("All screen refreshed")

    time.sleep((cycletime*60)/5)
    print("The screen is refreshing... (4)")
    refresh()
    print("All screen refreshed")

    time.sleep((cycletime*60)/5)
    print("\nCycle: "+str(loop)+" Done")
    print("\n=============================================")
    loop += 1