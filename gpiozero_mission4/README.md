
# Mission2 - Raspberry Pi GPIO & Python

## 1. 📜 개요

Python을 활용한 라즈베리 파이의 GPIO 제어를 GPIOZERO를 활용하여 미션을 수행합니다.

1. 버튼이 눌린 동안만 LED 켜기
2. 버튼이 눌릴 때마다 LED 토글 시키기
3. 버튼이 눌리면 `domino4` 1회 실행하기
4. 버튼이 눌릴 때마다 4-bit 카운터 값 증가시키기

## 2. 🎥 동작 영상

[동작영상](https://youtu.be/MWbMh9LEpto)  

## 3. 🔌 핀 구성

- **LED 핀**: 4개의 LED가 연결된 GPIO 핀
  - LED 1: GPIO 8
  - LED 2: GPIO 7
  - LED 3: GPIO 16
  - LED 4: GPIO 20
- **Button 핀**: 버튼은 GPIO 25에 연결되어 있습니다.

### 연결 설명:
- 각 LED는 Raspberry Pi의 GPIO 핀에 연결되어 있으며, 각 핀의 상태를 제어하여 LED가 켜지거나 꺼지도록 합니다.
- 버튼은 GPIO 25 핀에 연결되어 있으며, 버튼을 눌렀을 때 발생하는 신호를 이용해 LED의 상태를 토글하거나 다른 동작을 실행합니다.

## 4. 💻 코드 구성

### Mission2_1: 버튼이 눌린 동안만 LED 켜기

```python
#!/usr/bin/env python3
from gpiozero import LED, Button
from signal import pause  # 루프를 대체해서 프로그램이 종료되지 않도록 함

led = LED(8)
button = Button(25)

# 버튼 누름/뗌에 따라 LED 제어
button.when_pressed = led.on
button.when_released = led.off

pause()  # 무한 루프 대신 사용 (이벤트 핸들링을 계속 기다림)
```

### Mission2_2: 버튼이 눌릴 때마다 LED 토글 시키기

```python
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
```

### Mission2_3: 버튼이 눌리면 `domino4` 1회 실행하기

```python
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
```

### Mission2_4: 버튼이 눌릴 때마다 4-bit 카운터 값 증가시키기

```python
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
```
