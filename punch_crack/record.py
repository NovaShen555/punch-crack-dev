import requests
import csv
from .constants import RECORD_URL, HEADERS

def makeRecordPostContent(cardId: str = ""):
    return {
        "cardno": {cardId},
        "startdt": "2022-11-01",  
        "enddt": "2032-12-31",  
        "pageIndex": 1,  
        "pageSize": 14,  
        "sign": f"cardno={cardId}startdt=2022-11-01enddt=2032-12-31pageIndex=1pageSize=14"
    }

def __checkRecord(recordUrl: str = "", recordHeaders: str = "", recordData: dict = {}):
    return requests.post(
        url = recordUrl,
        data = recordData,
        headers = recordHeaders
    ).json()

def checkRecord(recordCardId: str | int = ""):
    recordCardId = str(recordCardId)
    return __checkRecord(RECORD_URL, HEADERS, makeRecordPostContent(recordCardId))

def exportRecordCSV(recordCardId: str | int = "", exportFileName: str = "record.csv"):
    with open(exportFileName, 'w', newline='') as csvfile:
        fieldName = ['Account', 'Terminal', 'RecordState', 'WorkPlaceName', 'DeptName1', 'DeptName2', 'RecordDT', 'UserName']
        writer = csv.DictWriter(csvfile, fieldnames = fieldName)
        writer.writeheader()
        record = checkRecord(recordCardId)
        for row in record['data']:
            writer.writerow(row)