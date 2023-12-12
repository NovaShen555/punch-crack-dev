# `punch-crack-dev`

Crack the punch-card system via http post.

## Installation

1. Install `Python 3` (and `Git`).

2. Clone this repository, or download the source code.

3. Install `requests==2.28.1` and `urllib3==1.26.13`.
Here is a possible way:
```
pip install requests==2.28.1
pip install urllib3==1.26.13
```
## Usage

### Punch Card 

Definition: `punchCard(CardId: str | int, DeviceId: str | int)`.

Create a `example.py` like this:

```python
from punch_crack import *
CardId = ""
DeviceId = ""
punchCard(CardId, DeviceId)
```

* The `cardId` is the **RFID** of your current school card. You can get your RFID by placing your school card on the hot water machine in your dormitory.

* The `DeviceId` is the **MAC address** of your class computer. You can find it by call `checkRecord()` method. **Notice that the MAC address letters are capitalized.**

### Check Record and Export it to a CSV file

Definition: `exportRecordCSV(CardId: str | int, exportFileName: str)`.

Create a `example.py` like this:

```python
from punch_crack import *
CardId = ""
exportRecordCSV(CardId, "record.csv")
```

* The `cardId` is the **RFID** of your current school card. You can get your RFID by placing your school card on the hot water machine in your dormitory.

* The `exportFileName` is the csv file name to generate. After proceed this method, you can find your recent `DeviceId`.
