# Goal: Implement a Timer in which depending on which of 3 buttons is pressed and allows to define 3 different pump profiles
# btn_manual_control - Just turns on the LED / relay
# btn_profile_1 - pre-infuses for 10 seconds, runs for 30 seconds, turns off
# btn_profile_2 - pre-infuses for 30 seconds, runs for 30 seconds, turns off
import time
import board
import digitalio
import pwmio

# Setup the led in Off Mode - changing it to a relay is a matter of change the bord.port assignment
led = pwmio.PWMOut(board.LED, frequency=5000, duty_cycle=0)

# Turns on the device in Manual Mode
btn_manual_control = digitalio.DigitalInOut(board.GP13)
btn_manual_control.direction = digitalio.Direction.INPUT
btn_manual_control.pull = digitalio.Pull.DOWN

# Profile 1 Button - 
btn_profile_1 = digitalio.DigitalInOut(board.GP12)
btn_profile_1.direction = digitalio.Direction.INPUT
btn_profile_1.pull = digitalio.Pull.DOWN

# Profile 2 button
btn_profile_2 = digitalio.DigitalInOut(board.GP11)
btn_profile_2.direction = digitalio.Direction.INPUT
btn_profile_2.pull = digitalio.Pull.DOWN

# Profile 1
profile_1 = [{"seconds": 5,"duty_cycle": 25},{"seconds": 5,"duty_cycle": 50},{"seconds": 30,"duty_cycle": 100}]


# Profile 2
profile_1 = [{"seconds": 5,"duty_cycle": 25},{"seconds": 5,"duty_cycle": 50},{"seconds": 20,"duty_cycle": 100}]

btn_profile_1.value = '1'

while True:
    if btn_manual_control.value:
        led.duty_cycle = int(1 * 65535)
        print('Manual Mode is Activated')
    else:
        led.duty_cycle = int(0)
    if btn_profile_1.value:
        for profile in profile_1:
            seconds = profile['seconds']
            duty_cycle = profile['duty_cycle']
            print("Seconds: " + str(seconds))
            led.duty_cycle = int(duty_cycle/100 * 65535)
            print("Duty Cycle: " + str(duty_cycle))
            print('-------------------------')
            time.sleep(seconds)
        led.duty_cycle = int(0)
    else:
        led.duty_cycle = int(0)
    if btn_profile_2.value:
        for profile in profile_2:
            seconds = profile['seconds']
            duty_cycle = profile['duty_cycle']
            print("Seconds: " + str(seconds))
            led.duty_cycle = int(duty_cycle/100 * 65535)
            print("Duty Cycle: " + str(duty_cycle))
            print('-------------------------')
            time.sleep(seconds)
        led.duty_cycle = int(0)
    else:
        led.duty_cycle = int(0)
        

