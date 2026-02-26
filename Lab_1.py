plain_text = input("Введите открытый текст \nОткрытый текст: ")

while True:
    try:
        shift = int(input("Введите желаемый сдвиг: "))
        break
    except ValueError:
        print("Ошибка! Введите ЧИСЛО равное желаемому сдвигу")

unicode_list = [ord(ch) for ch in plain_text]

for i in range(len(unicode_list)):
    code = unicode_list[i]

    # Английский строчный a-z
    if 97 <= code <= 122:
        k = shift % 26
        unicode_list[i] = (code - 97 + k) % 26 + 97

    # Английский заглавный A-Z
    elif 65 <= code <= 90:
        k = shift % 26
        unicode_list[i] = (code - 65 + k) % 26 + 65

    # Русский строчный а-я (без ё)
    elif 1072 <= code <= 1103:
        k = shift % 32
        unicode_list[i] = (code - 1072 + k) % 32 + 1072

    # Русский заглавный А-Я (без Ё)
    elif 1040 <= code <= 1071:
        k = shift % 32
        unicode_list[i] = (code - 1040 + k) % 32 + 1040

    # ё -> е
    elif code == 1105:  # ё
        code = 1077      # е
        k = shift % 32
        unicode_list[i] = (code - 1072 + k) % 32 + 1072

#  Ё -> Е
    elif code == 1025:  # Ё
        code = 1045      # Е
        k = shift % 32
        unicode_list[i] = (code - 1040 + k) % 32 + 1040

out_txt = ''.join(chr(code) for code in unicode_list)
print(f"\n{unicode_list}")
print(f"\n{out_txt}")