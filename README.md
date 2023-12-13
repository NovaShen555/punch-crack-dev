# Punch - Crack DEV

Crack the punch-card system via http post.

## Installation

1. Install `Python 3` (and `Git`).

2. Clone this repository, or download the source code.

3. Install `requests==2.28.1` and `urllib3==1.26.13`.
Here is a possible way:
```
pip install -r requirements.txt
```
## Usage

### Get Your `CardId`

Use your phone's NFC function to get your `cardId`.

#### CardId Calculation Method

When you get your real card ID, you can calculate your `cardId` (in system) by the following method:
- Divide each 2 hex digits into a group, and reverse the order of each group.
- Change it into Decimal.

#### Example

* CardId: `07D72B1C`
* Reverse each group: `1C2BD707`
* Change it into Decimal: `472635143`

So, cardId (in system) is `472635143`.

### Punch Card 

Definition: `punchCard(CardId: str | int, DeviceId: str | int)`.

Create a `example.py` like this:

```python
from punch_crack import *
CardId = ""
DeviceId = ""
punchCard(CardId, DeviceId)
```

* The `cardId` get it with the above.

* The `DeviceId` is the **MAC address** of your class computer. You can find it by call `checkRecord()` method. **Notice that the MAC address letters are capitalized.**

### Check Record and Export it to a CSV file

Definition: `exportRecordCSV(CardId: str | int, exportFileName: str)`.

Create a `example.py` like this:

```python
from punch_crack import *
CardId = ""
exportRecordCSV(CardId, "record.csv")
```

* The `cardId` get it with the above.

* The `exportFileName` is the csv file name to generate. After proceed this method, you can find your recent `DeviceId`.
