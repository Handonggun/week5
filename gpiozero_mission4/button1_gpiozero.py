#!/usr/bin/env python3
from gpiozero import LED, Button
from signal import pause  # 루프를 대체해서 프로그램이 종료되지 않도록 함

led = LED(8)
button = Button(25)

# 버튼 누름/뗌에 따라 LED 제어
button.when_pressed = led.on
button.when_released = led.off

pause()  # 무한 루프 대신 사용 (이벤트 핸들링을 계속 기다림)
