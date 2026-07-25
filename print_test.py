#!/usr/bin/env python3
"""Диагностика печати на Niimbot: печатает максимально простой тестовый
узор (сплошной чёрный прямоугольник с рамкой) и включает подробный лог
всех пакетов протокола, чтобы было видно, что реально происходит.

Запускать напрямую на машине с Bluetooth и включённым принтером:

    python3 print_test.py AA:BB:CC:DD:EE:FF

(MAC-адрес - тот же, что в Настройках приложения. Если не знаете - можно
взять оттуда, либо через bluetoothctl.)

Если после этого лента всё равно чистая - скопируйте весь вывод (включая
DEBUG-строки) для дальнейшей диагностики.
"""
import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s | %(funcName)s:%(lineno)d - %(message)s",
)

from PIL import Image, ImageDraw

from niimprint import BluetoothTransport, PrinterClient


def main():
    if len(sys.argv) < 2:
        print("Использование: python3 print_test.py AA:BB:CC:DD:EE:FF")
        sys.exit(1)
    address = sys.argv[1]

    # Картинка уже в "печатной" (узкой) ориентации - ширина 96 точек,
    # под физическую ширину головки D11/D110. Внутри - сплошная чёрная
    # заливка с белой рамкой: если хоть что-то печатается, это будет видно
    # сразу, без всякого текста и шрифтов.
    image = Image.new("RGB", (96, 240), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([4, 4, 91, 235], outline="black", width=4)
    draw.rectangle([20, 20, 75, 219], fill="black")
    image.save("print_test_pattern.png")
    print("Тестовый узор сохранён в print_test_pattern.png (для сверки)")

    print(f"Подключаюсь к {address}...")
    transport = BluetoothTransport(address)
    print("Подключено. Печатаю тестовый узор (density=3)...")

    client = PrinterClient(transport)
    client.print_image(image, density=3)

    print("Готово. Если лента всё равно чистая - смотрите DEBUG-лог выше:")
    print("  - если там видно 'Ignoring ... failure' на heartbeat/get_info -")
    print("    принтер не отвечает на прогрев (проблема с самим соединением)")
    print("  - если видно 'Timed out waiting for print completion' -")
    print("    принтер не подтверждает прогресс печати")
    print("  - если ошибок не видно вообще, но лента чистая -")
    print("    возможно проблема на уровне прошивки/модели принтера")


if __name__ == "__main__":
    main()
