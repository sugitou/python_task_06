import csv
import gspread, itertools
import pandas as pd

from datetime import datetime as dt
from gspread.models import Worksheet
from oauth2client.service_account import ServiceAccountCredentials


SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

JSONKEY = r'C:\Users\Raito\Documents\GCP\raits-project-a881a2add413.json'

class SpreadsheetManager():

    def __init__(self):
        self.worksheet = None


    def connect_by_sheetname(self, file_id, sheet_name):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(JSONKEY, gspread.auth.DEFAULT_SCOPES)
        gs = gspread.authorize(credentials)
        self.worksheet = gs.open_by_key(file_id).worksheet(sheet_name)

            
    def bulk_insert(self, datas:list):
        '''
        listを指定してスプレッドシートを一括更新
        '''
        begin_row = self.get_last_row() + 1 # 最終行の次の行から始める
        header = self.init_fetch_sheet_header()
        cells = self.worksheet.range(begin_row, 1, len(datas) + begin_row -1 , len(header))
        for row,data in enumerate(datas):
            for k,v in data.items():
                try:
                    col = header.index(k)
                    num = row*(len(header)) + col # 複数行にまたがるデータの場合でも１次元配列に格納されているため２次元→１次元に変換する
                    cells[num].value = v
                except Exception as e:
                    print(e)
                    pass

        self.worksheet.update_cells(cells)
        return True


    def init_fetch_sheet_header(self, header_row: int=1):
        df = pd.DataFrame(self.worksheet.get_all_values())
        return list(df.loc[header_row-1,:]) 


    def get_last_row(self):
        '''
        最終行の取得
        '''
        return len(self.worksheet.get_all_values())
            
