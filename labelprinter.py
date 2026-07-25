"""Печать этикеток с номером заказа на Bluetooth-принтере Niimbot.

Изолирует конкретную модель/транспорт принтера от остального кода, по
аналогии с messagesender.py: LabelPrinter собирает картинку этикетки и
отправляет её на принтер, адрес и параметры которого читаются из
QSettings (настраиваются в SettingsDialog).
"""

import os

from PIL import Image, ImageDraw, ImageFont

from niimprint import BluetoothTransport, PrinterClient

SETTINGS_ORG = "ixSoft"
SETTINGS_APP = "ixJournal"
SETTINGS_KEY_ADDRESS = "printer/address"
SETTINGS_KEY_DENSITY = "printer/density"
SETTINGS_KEY_LENGTH_MM = "printer/label_length_mm"

DEFAULT_DENSITY = 3
DEFAULT_LENGTH_MM = 30
MAX_DENSITY = 3  # D11/D110/B18 официально не поддерживают выше 3; выше не даёт эффекта

# Каждая собранная этикетка сохраняется сюда перед отправкой на принтер -
# чтобы можно было проверить, что реально рисуется, независимо от того,
# печатает ли сам принтер (открыть файл и посмотреть глазами).
DEBUG_LAST_LABEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "last_label.png")

# Этикетка Niimbot: ~8 пикселей на мм. Ширина ленты у D11/D110 физически
# фиксирована - 96 точек (~12мм), а длина настраивается (30/40мм и т.п.).
# Рисуем в удобной для чтения "альбомной" ориентации (длина шире высоты), а
# перед самой печатью поворачиваем на 90° - именно ШИРИНА картинки (после
# поворота) должна укладываться в 96 точек головки. Раньше отправляли без
# поворота, ширина намного превышала физические 96 точек, принтер не мог
# это напечатать и просто отбрасывал задание - отсюда пустые этикетки.
PX_PER_MM = 8
LABEL_HEIGHT_PX = 96  # ширина ленты, точек - фиксирована железом
MAX_WIDTH_PX = 96  # ограничение печатающей головки D11/D110

_FONT_CANDIDATES_REGULAR = ["arial.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf"]
_FONT_CANDIDATES_BOLD = ["arialbd.ttf", "DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf"]


def _loadFont(bold, size):
    for name in (_FONT_CANDIDATES_BOLD if bold else _FONT_CANDIDATES_REGULAR):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default(size)


class LabelPrinter:
    def buildOrderLabel(self, numZak, phone="", date="", company="Инфоникс", length_mm=None):
        """Собирает изображение этикетки: название - номер заказа (крупно) -
        телефон - дата, как в прежних набросках (text_to_png.py)."""
        if length_mm is None:
            length_mm = int(self._settingValue(SETTINGS_KEY_LENGTH_MM, DEFAULT_LENGTH_MM))
        width_px = length_mm * PX_PER_MM

        image = Image.new("RGB", (width_px, LABEL_HEIGHT_PX), "white")
        draw = ImageDraw.Draw(image)

        draw.text((5, 15), company, font=_loadFont(False, 20), fill="black")
        draw.text((100, 5), str(numZak), font=_loadFont(True, 40), fill="black")
        if phone:
            draw.text((115, 60), str(phone), font=_loadFont(False, 20), fill="black")
        if date:
            draw.text((5, 60), str(date), font=_loadFont(False, 20), fill="black")

        return image

    def printOrderLabel(self, numZak, phone="", date="", company="Инфоникс",
                         address=None, density=None, length_mm=None):
        image = self.buildOrderLabel(numZak, phone, date, company, length_mm=length_mm)
        return self.printImage(image, address=address, density=density)

    def printImage(self, image, address=None, density=None):
        try:
            image.save(DEBUG_LAST_LABEL_PATH)
        except Exception:
            pass  # диагностика необязательна, не должна мешать печати

        if address is None:
            address = self._settingValue(SETTINGS_KEY_ADDRESS, "")
        if not address:
            raise RuntimeError("Не указан Bluetooth-адрес принтера этикеток (см. Сервис - Настройки)")

        if density is None:
            density = int(self._settingValue(SETTINGS_KEY_DENSITY, DEFAULT_DENSITY))
        density = max(1, min(density, MAX_DENSITY))

        if image.width > MAX_WIDTH_PX:
            # PIL поворачивает против часовой, printer.py ожидает по часовой
            image = image.rotate(-90, expand=True)

        transport = BluetoothTransport(address)
        client = PrinterClient(transport)
        client.print_image(image, density=density)

    def _settingValue(self, key, default):
        from PySide6.QtCore import QSettings
        return QSettings(SETTINGS_ORG, SETTINGS_APP).value(key, default)
