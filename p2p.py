import pyric
import pyric.pyw as pyw
import time
#import subprocess
#from gpiozero import LED, Button
#from signal import pause

def p2p_interface():
    #get all wirless interfaces
    Ifaces = pyw.winterfaces()
    print(Ifaces)

    if len(Ifaces)>0:
        # get current wireless card
        Wcard = pyw.getcard(Ifaces[0])
        #get card phy info
        iinfo = pyw.phyinfo(Wcard)
        if 'p2p_device' in iinfo['modes']:
            #shutdown interface
            pyw.down(Wcard)
            time.sleep(3)
            #create virtual interface
            w1= pyw.devset(Wcard, 'vcard')
            #set interafce mode
            pyw.modeset(w1, 'p2p_device')
            pyw.up(w1)
            print('virtual interface mode',pyw.modeget(w1))
        else:
            print("WiFi interface does't support p2p_device mode")
    else:
        print("device doesn't have wireless interface")

#def p2p_activate():
#    p2p_interface()
#    led.blin(0.5,0.5)

#set led
#led = LED(19)
#set button
#button = Button(26)

try:
    #button.when_pressed = p2p_activate()
    #pause()
    p2p_interface()
finally:
    pass