import requests


def makePunchPostContent(cardId: str, deviceId: str):
    return {
        "CardNo": cardId,
        "DeviceId": deviceId,
        "sign": f"CardNo={cardId}DeviceId={deviceId}",
    }


def __punchCard(punchUrl: str, punchHeaders: str, punchData: dict):
    return requests.post(
        url = punchUrl, 
        headers = punchHeaders, 
        data = punchData).json()

from .constants import *

def punchCard(punchCardId: str | int, punchDeviceId: str | int):
    punchCardId = str(punchCardId)
    punchDeviceId = str(punchDeviceId)
    return __punchCard(HIT_CARD_URL, HEADERS, makePunchPostContent(punchCardId, punchDeviceId))