"""Отправка клиенту уведомления о готовности заказа.

Изолирует конкретный сервис доставки (iDigital или SMSPilot) от остального
кода: вызывающая сторона сама решает, каким сервисом отправлять (обычно -
читая настройку через QSettings), и передаёт этот признак в send().
"""

import json
import re
import urllib.parse
import urllib.request

import cascade_idigital

SERVICE_IDIGITAL = "idigital"
SERVICE_SMSPILOT = "smspilot"

SETTINGS_ORG = "ixSoft"
SETTINGS_APP = "ixJournal"
SETTINGS_KEY_SERVICE = "messaging/service"


class MessageSender:
    def send(self, phone, text, textMessager, service=SERVICE_IDIGITAL):
        phone = normalizePhone(phone)
        if service == SERVICE_SMSPILOT:
            return self._sendSmsPilot(phone, text)
        return self._sendIDigital(phone, text, textMessager)

    def _sendIDigital(self, phone, text, textMessager):
        return cascade_idigital.cascade(None, phone, text, textMessager)

    def _sendSmsPilot(self, phone, text):
        sender = 'NFXnet'  # имя отправителя из списка https://smspilot.ru/my-sender.php
        apikey = 'C0C37F90PPSX2QAK8YBSYPPGE8X233741OSB2O306KTSP4TYJCT7VW07828607C7'
        formatapi = 'json'

        url = "http://smspilot.ru/api.php?"
        params = urllib.parse.urlencode({
            'send': text, 'to': phone, 'from': sender,
            'apikey': apikey, 'format': formatapi,
        })
        url = url + params

        return json.loads(urllib.request.urlopen(url.replace(" ", "%20")).read())


def normalizePhone(phone):
    """Приводит номер к формату 7XXXXXXXXXX (11 цифр, без +/пробелов/тире),
    как того требуют и SMSPilot (https://smspilot.ru/apikey.php), и iDigital.

    Поле "Телефон" в форме заказа - обычный текст без маски ввода, поэтому
    в базе номера встречаются как угодно записанные (+7..., 8..., с
    пробелами/тире и т.п.) - отсюда и не уходили уведомления.
    """
    digits = re.sub(r"\D", "", str(phone or ""))
    if len(digits) == 11 and digits[0] == "8":
        digits = "7" + digits[1:]
    elif len(digits) == 10:
        digits = "7" + digits
    return digits
