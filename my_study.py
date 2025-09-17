# 우왕 나혼자서 오늘꺼 복습이당~!
# 1~100 사이의 숫자를 맞추는 게임
import random

def play():
    secret = random.randint(1, 100)
    tries = 0
    print("1~100 사이 숫자를 맞춰보세요!")
    while True:
        try:
            guess = int(input("입력: "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue
        tries += 1
        if guess < secret:
            print("업 ↑")
        elif guess > secret:
            print("다운 ↓")
        else:
            print(f"정답! {tries}번 만에 맞췄습니다 🎉")
            break

if __name__ == "__main__":
    play()