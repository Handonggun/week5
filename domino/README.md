# 임베디드통신시스템 - LED 도미노

본 프로젝트는 **Raspberry Pi 5**를 활용하여 **GPIO 핀을 제어**하고, **브레드보드 위의 LED 회로를 구현**한 프로젝트입니다. LED 점멸 및 패턴 출력 스크립트를 작성하고, 회로 구성은 실제 사진과 유튜브영상으로 확인할 수 있습니다.

---
## 유튜브영상

구현 및 회로코드 설명 영상은 아래 링크에서 확인하실 수 있습니다:

[YouTube - Domino](https://youtu.be/ntcSlIiXxRw)

---

## 프로젝트 사진

실제 구성된 하드웨어:

![real](https://github.com/Handonggun/week5/blob/main/image/domino.jpg)

---

## 회로 설명

- GPIO 연결:

| GPIO 핀 번호 | 역할    | 연결 부품 |
|--------------|---------|------------|
| GPIO 06      | LED 제어 | 노란색 LED |
| GPIO 13      | LED 제어 | 빨간색 LED |
| GPIO 19      | LED 제어 | 초록색 LED |
| GPIO 26      | LED 제어 | 노란색 LED |
| GND          | 접지     | LED 공통 GND |

## 구현 방식

### **LED Domino (`domino`)**
- 4개의 LED 중 1개씩 순서대로 1초 간격으로 켜짐
- 다음 LED로 넘어가면서 이전 LED는 꺼짐
- 무한 반복

---

## 실제 코드 및 설명

![real](https://github.com/Handonggun/week5/blob/main/image/domino_code.PNG)

---

## 실행 방법

```bash
# 스크립트 실행 전 권한 부여
chmod +x domino4.sh

# 실행
domino     # 도미노 LED 점등
