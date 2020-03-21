from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import simplejson as json

SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
SECRETS_FILE = '/home/jack/programs/scheduling/credentials.json'
SPREADSHEET = "Schedule for Fall 1999"

def readForm():
    json_key = json.load(open(SECRETS_FILE))
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE, SCOPE)

    gc = gspread.authorize(credentials)

    workbook = gc.open(SPREADSHEET)
    sheet = workbook.sheet1

    data = pd.DataFrame(sheet.get_all_records())

    column_names = {'Timestamp': 'timestamp',
                    'NetID': 'netid',
                    'Name': 'name',
                    'Week Hours': 'weekhours',
                    'Day Hours': 'dayhours',
                    'Monday Prefer': 'mondaylike',
                    'Monday Cannot': 'mondayno'
                    }
    data.rename(columns=column_names, inplace=True)
    data.timestamp = pd.to_datetime(data.timestamp)
    print(data)
    return(data)
