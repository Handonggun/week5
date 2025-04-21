#!/usr/bin/env python3
from gpiozero import LED, Button
from signal import pause
from time import sleep

leds = [LED(8), LED(7), LED(16), LED(20)]
button = Button(25)

def domino4():
    for led in leds:
        led.on()
        sleep(1)
        led.off()

# 버튼이 눌리면 domino4 실행
button.when_pressed = domino4

pause()  # 이벤트 핸들링 대기
