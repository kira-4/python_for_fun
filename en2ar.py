import pyautogui
import pyperclip

letter_dict = {
    "`": "ذ",
    "q": "ض",
    "w": "ص",
    "e": "ث",
    "r": "ق",
    "t": "ف",
    "y": "غ",
    "u": "ع",
    "i": "ه",
    "o": "خ",
    "p": "ح",
    "[": "ج",
    "]": "د",
    "a": "ش",
    "s": "س",
    "d": "ي",
    "f": "ب",
    "g": "ل",
    "h": "ا",
    "j": "ت",
    "k": "ن",
    "l": "م",
    ";": "ك",
    "'": "ط",
    "z": "ئ",
    "x": "ء",
    "c": "ؤ",
    "v": "ر",
    "b": "لا",
    "n": "ى",
    "m": "ة",
    ",": "و",
    ".": "ز",
    "/": "ظ",
}

# time.sleep(1)

pyautogui.hotkey('alt', 'tab')

# hgsghl ugd;l
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

clip = pyperclip.paste()

clip_lst = list(clip)

output_lst = []

for letter in clip_lst:
    if letter in letter_dict:
        output_lst.append(letter_dict.get(letter))
    else:
        output_lst.append(letter)

output = "".join(output_lst)

pyperclip.copy(output)

pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("alt", "shift")

