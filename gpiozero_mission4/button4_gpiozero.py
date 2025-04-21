#!/usr/bin/env python3
from gpiozero import LED, Button
from signal import pause

leds = [LED(8), LED(7), LED(16), LED(20)]  # 4개의 LED 핀
button = Button(25)  # 버튼 핀 번호

counter = 0  # 4-bit 카운터

def display_counter():
    global counter
    # 카운터 값을 이진수로 변환하여 LED에 출력
    for i in range(4):
        if (counter >> (3 - i)) & 1:
            leds[i].on()
        else:
            leds[i].off()

def increment_counter():
    global counter
    counter = (counter + 1) % 16  # 4-bit 카운터로 0~15 범위 내에서 순환
    display_counter()  # 카운터 값을 LED에 표시

button.when_pressed = increment_counter  # 버튼이 눌리면 카운터 증가

pause()  # 이벤트 처리 대기
