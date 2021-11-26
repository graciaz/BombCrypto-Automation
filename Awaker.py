import pyautogui
import time
import datetime

pyautogui.FAILSAFE= True
i = 0
position_green_back_button_x = 0
position_green_back_button_Y = 0
loop = 1
count_hero_start = 0

def clearerror():
    # Clear the error message
    pyautogui.click(950, 660, duration = 1)
    time.sleep(6)

def discard():
    #Click on Metamask@taskbar || Metamask must be at index 10
    pyautogui.click(565, 1050, duration = 2)

    #Click on Cancel
    pyautogui.click(1665, 560, duration = 2)

def relogin():

    # Click on connect wallet
    pyautogui.click(950, 740, duration = 2)
    time.sleep(5)

    # Click on Metamask
    # pyautogui.click(950, 580, duration = 2)

    #Click on Metamask@taskbar || Metamask must be at index 10
    # pyautogui.click(565, 1050, duration = 2)

    # Click on Sign
    pyautogui.moveTo(1830, 560, duration = 3)
    pyautogui.click()

    # Click on Blank
    pyautogui.click(980, 300, duration = 2)
    time.sleep(10)

    # Click on Teasure Hunt 
    pyautogui.click(980, 460, duration = 2)
    time.sleep(10)

def prepare():
    print("\nProcess Starting . . .")
    print("Clear error message")
    clearerror()
    print("Discard old login")
    discard()
    print("Relogin Metamask")
    relogin()

print('''%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%
%%%%%&&&&&&&&&&&&&&&&&&&&(///////////(&&&&&(////////////&&&&&&&&&&&&&&&&&&%%%%%%
%%%%%&&&&&&&&&&&&&&&&(****///////////*******///////////****(&&&&&&&&&&&&&&%%%%%%
&%%%%&&&&&&&&&&&&&&&&/  ./(((((((((((/.    /((((((((((((.  ,&&&&&&&&&&&&&&%%%%%%
&%%%%&&&&&&&&&&&%%%%%/...(((((((((((((...../((((((((((((,..*%%%&&&&&&&&&&&%%%%%%
&%%%%&&&&&&&&&&%.    *((((((((((((((((/////((((((((((((((((/   (&&&&&&&&&&%%%%%%
&%%%%&&&&&&&*  .(((((((((((((((((((((((((((////((((((((((((((((,    ,&&&&&%%%%%%
&%%%%&&&&&&&*  .((((((((((((((((((((((((((((///((((((((((((((((,    .&&&&&%%%%%%
%%%%%&&&#.../(((((((((((#&@@@@@@@@,  ,&@@@@#//(@@@@@@@@&.  ,@@@*    .&&&&&%%%%%%
&%%%%&&&#   /(((((((((((#&@@@@@@@@,  .&&&&&(//(&@@@@@@@@.  ,&&&*    .&&&&&%%&%%%
&%%%%&&&#   /(((((((((((((((#@@@@@,        ,//////#@@@@@.           .&&&&&%%%%%%
&%%%%&&&#   /((((((((((((((((((((((((((((((((((((((((((((((((((,    .&&&&&%%%%%%
&%%%%&&&#   /((((((((((((((((((((((((((((((((((((((((((((((((((,    .&&&&&%%%%%%
&%%%%&&&#   /((((((((((((((((((((((((((((((((((((((((((((((((((,    .&&&&&%%%%%%
&%%%%&&&#.../((((((((((((//////////////////////////////////////,    .&&&&&%%%%%%
&%%%%&&&&&&&*  .((((((((/                                           .&&&&&%%%%%%
&%%%%&&&&&&&&&&%.....*(((//////////////////////////////////////#&&&&&&&&&&%%%%%%
&%%%%&&&&&&&&&&%.    *(((((((((((((((((((((((((((((((((((((((((%&&&&&&&&&&%%%%%%
&%%%%&&&&&&&&&&&#####/..,/((((((((((((((((((((((((((((((,..*%%%&&&&&&&&&&&%%%%%%
&%%%%&&&&&&&&&&&&&&&&/  ./((((((((((((((((((((((((((((((.  ,&&&&&&&&&&&&&&%%%%%%
&&&&&&&&&&&&&&&%.    ,(/////////(//////////////(///////////*   (&&&&&&&&&&%&&&&&
&&&&&&&&&&&&&&&%.    *(/////////(///////////////(//////////*   #&&&&&&&&&&%&&&&&
&&&&&&&&&&&&*  .///////////////////////////////////////////////,    .&&&&&%&&&&&
&&&&&&&&&&&&*  ./////*,,,///////(///////////////////////,,,*///,    .&&&&&%&&&&&
&&&&&&&&&&&&*  ./////,  .///////////////////////////////.  .///.    .&&&&&%&&&&&
&&&&&&&&&&&&*  .(((((*  ./(((((((((((((((((((((((((((((/.  ,(((,    .&&&&&&&&&&&
&&&&&&&&&&&&*  .(((((*  ./(((((((((((((((((((((((((((((/.  ,(((,    .&&&&&%&&&&&
&&&&&&&&&&&&*  .(((((*   ***/(((((((((((((((((((((/*****.  ,(((,    .&&&&&%&&&&&
&&&&&&&&&&&&(****////*,,,,,,*/////*************///*,,,,,,,,**//*****/&&&&&%&&&&&
&&&&&&&&&&&&&&&&/////(%%#////(((#(/////////////(##(/////#%%#///%&&&&&&&&&&%&&&&&
&%%%&%%%&%%%&%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%&%%%&%%%&%%%
&@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,      /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%&&&&&&&&&%%%
@@@@@@@@@@@@@@@@@@@@@@#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%&&&&&&&&&%%%
@@@@@@@@@@@@@@@&&&&&&&,  @@@@@@@@@@@@(########(@@@@@@@@@@@@@@@@@@@@#   ####(&@@@@@@@@@@@@@@@@@@@@&  @   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&%%
@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@&,      #@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%&%%%&%%%&%%%
@@@@@@@@@   .@@    @@,   @@    @@@@@*       ,@@@@    @@@@    @@/   @      @@@@@@@@     #@@@@@(        @@@@.   #@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&%%%
@@@@@@@@@*   @%    #@   #@@    @@@/    *%/    /@@    @@@@    @@(    ,%*    (@,,,*&&#,    @@@    *%#    .@@    %@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&%%%
@@@@@@@@@@   #      #   @@@    @@@    @@@@&    @@    @@@@    @@(   .@@@,   /@@    @@@,   *@/   #%./@    @@    %@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&%%%
@@@@@@@@@@*     %#     #@@@    @@@    /@@@&    @@    &@@&    @@(   .@@@,   *@@@    @&    &@/      *@    @@    (@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&%%%
@@@@@@@@@@@     @@     @@@@,     @@.     @&    @@&           @@(   .@@@,   /@@@@       .@@@(   *@@@@    @@@           @@*    @@    /@,    @@@@@@@@@&&&&&&&&&&&%%%
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&%%%\n''')

print("\nBombCrypto Automation Start")
cycle_time = int(input("Input cycle time (Min.): "))

while True:
    prepare()

    print("Process find green back button")
    result_find_back_button = pyautogui.locateOnScreen('images/btn-back.jpg', confidence=0.8)
    if result_find_back_button is not None:
        print("Found green back button")
        x, y = pyautogui.center(result_find_back_button)
        position_green_back_button_x = x
        position_green_back_button_Y = y
        print("Save position green back button")
        print(x,y)
        pyautogui.click(x, y, duration = 1)
        print("Click green back button")
        print("Find hero list button")
        time.sleep(2)
        result_find_list_hero = pyautogui.locateOnScreen('images/list-hero.jpg', confidence=0.8)
        if result_find_list_hero is not None:
            x, y = pyautogui.center(result_find_list_hero)
            pyautogui.click(x, y, duration = 2)
            time.sleep(10)
            
            print("Awaking hero, please wait . . .")
            # result_click_btn_work = pyautogui.locateOnScreen('images/btn-work.jpg', confidence=0.9)
            # x, y = pyautogui.center(result_click_btn_work)
            # pyautogui.moveTo(x, y)

            pyautogui.moveTo(890, 750, duration = 1)
            for i in range (40):
                pyautogui.scroll(-1)
            # while i <= 5:
            #     result_click_btn_work = pyautogui.locateOnScreen('images/btn-work.jpg', confidence=0.9)
            #     if result_click_btn_work is not None:
            #         x, y = pyautogui.center(result_click_btn_work)
            #         time.sleep(1)
            #         pyautogui.click(x, y)
            #         count_hero_start += 1
            #         print("Click work hero: ",count_hero_start)
            #     i += 1
            #     time.sleep(0.5)
            

            for i in range (15):
                pyautogui.click(890, 750, duration = 1)
                time.sleep(1)
                # Click on close | In case of error
                pyautogui.click(1240, 355, duration = 1)

            print("All hero awake, ready to start")
            print("Find close button")
            time.sleep(0.5)
            result_find_close_button = pyautogui.locateOnScreen('images/btn-close.jpg', confidence=0.8)
            if result_find_close_button is not None:
                x, y = pyautogui.center(result_find_close_button)
                print("Click close button")
                time.sleep(0.5)
                pyautogui.click(x, y, duration = 1)
                time.sleep(1)
                pyautogui.click(x, y, duration = 1)
                print("Find start button")
                time.sleep(1)
                result_find_start_button = pyautogui.locateOnScreen('images/btn-start.jpg', confidence=0.8)
                if result_find_start_button is not None:
                    x, y = pyautogui.center(result_find_start_button)
                    print("Click start button")
                    time.sleep(0.5)
                    pyautogui.click(x, y, duration = 1)
                    time.sleep(1)
                    pyautogui.click(x, y, duration = 1)
                # Click on new map | In case of new map
                pyautogui.click(950, 740, duration = 1)
    ct = datetime.datetime.now()
    print("\nAwake : "+str(loop)+" times\nTimestamp :",ct)
    print("Hero will be awake in next",cycle_time,"Min.\n")
    print("=================================================\n")
    loop += 1
    time.sleep(60*cycle_time)