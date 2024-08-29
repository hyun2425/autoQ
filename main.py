import keyboard
import pyautogui
import pyperclip

# 특정 좌표로 이동하여 텍스트 복사
def copy_text_from_cs():
    pyautogui.moveTo(1835, 875)  # 예시 좌표로 이동
    pyautogui.doubleClick()  # 더블 클릭하여 텍스트 전체 선택
    pyautogui.hotkey('ctrl', 'a')  # Ctrl + A 눌러 모든 텍스트 선택
    pyautogui.hotkey('ctrl', 'c')  # 텍스트 복사
    text = pyperclip.paste()  # 클립보드에서 텍스트 가져오기
    return text

# 텍스트를 붙여넣기 위한 함수
def paste_text_to_cs():
    pyautogui.moveTo(1835, 975)  # 텍스트를 붙여넣을 좌표로 이동 (예시 좌표)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')  # 텍스트 붙여넣기

# F1 키가 눌렸을 때 실행할 함수
def on_f1_pressed():
    text = copy_text_from_cs()
    if text:
        print("Text copied to clipboard:", text)
        paste_text_to_cs()

# 메인 프로그램
def main():
    print("Press F1 to copy text and paste it to another location")
    keyboard.add_hotkey('`', on_f1_pressed)
    keyboard.wait('esc')  # 프로그램을 종료하려면 Esc 키를 누릅니다.

if __name__ == "__main__":
    main()
