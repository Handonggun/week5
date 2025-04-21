#!/usr/bin/env python3
from gpiozero import LED, Button
from signal import pause

led = LED(8)
button = Button(25, bounce_time=0.2)  # 200ms로 디바운스 시간 설정

# 상태 토글 함수
def toggle_led():
    led.toggle()  # LED 상태를 토글 (켜지면 끄고, 꺼지면 킴)

# 버튼이 눌릴 때마다 LED 상태 토글
button.when_pressed = toggle_led

pause()  # 무한 루프 대신 사용 (이벤트 핸들링을 계속 기다림)
