# 가위 바위 보 게임 (3판 2선승제)
import random

# 번호와 손 저장한 딕셔너리
HANDS = {1:"가위", 2:"바위", 3:"보"}

# 게임 타이틀 출력
def show_title():
    print("="*40)
    print("가위/바위/보 게임")
    print("="*40)

# 플레이어 이름 입력
def ask_name():
    name = input("플레이어 이름을 입력하세요. ").strip()
    if name == "":
        name = "게스트"

    return name

# 플레이어 번호 입력
def ask_number():
    while True:
        print("1. 가위 / 2. 바위 / 3. 보")
        answer = input("번호를 선택하세요. : ").strip()

        if answer in ("1", "2", "3"):
            return int(answer)

        print("1, 2, 3 중에서 입력하세요.")

# 승패 판정
# 1 - 1 / 2 - 2 / 3 - 3 무승부 조건
# 1 - 3 / 2 - 1 / 3 - 2 플레이어 승리 조건
# 반환값 : 무승부 / 승리 / 패배
def check_result(user_number, computer_number):
    # 무승부 조건
    if user_number == computer_number:
        return "무승부"

    # 플레이어 승리 조건
    if user_number == 1 and computer_number == 3: return "승리" # 가위 / 보
    if user_number == 2 and computer_number == 1: return "승리" # 바위 / 가위
    if user_number == 3 and computer_number == 2: return "승리" # 보 / 바위

    return "패배"

# 한 판의 게임 결과 출력
def show_result(name, user_number, computer_number, result):
    print("\n[게임 결과]")
    print(f"{name}: {HANDS[user_number]} vs 컴퓨터: {HANDS[computer_number]}")
    print(f"=> {result}")

# 게임의 전체 루프
def main():
    show_title()
    name = ask_name()

    user_number = ask_number()
    computer_number = random.randint(1, 3) # 1, 2, 3

    # 승패 판정
    result = check_result(user_number, computer_number)
    show_result(name, user_number, computer_number, result)

# 게임 시작
main()