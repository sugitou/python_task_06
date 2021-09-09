import requests
import urllib
import numpy as np
import os
import pandas as pd
import pprint

from spreadsheet_manager import SpreadsheetManager
from dotenv import load_dotenv
# .envファイルの内容を読み込みます
load_dotenv()

RAKUTEN_API_ID = os.environ["RAKUTEN_API_ID"]
SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]

def set_param(keyword):
    param = {
        "format" : "json",
        "keyword" : keyword,
        "applicationId" : int(RAKUTEN_API_ID),
        # "availability" : 0,
        # "hits" : 30,
        # "page" : 1,
        # "sort" : "-updateTimestamp"
    }
    return param


def get_api(url, params):
    result = requests.get(url, params)
    return result.json()


def output(resp):
    # for文を回してdictを作る
    item_key = ['itemName', 'itemPrice', 'itemCaption', 'itemUrl', 'genreId']
    item_list = []
    for i in range(0, len(resp['Items'])):
        tmp_item = {}
        item = resp['Items'][i]['Item']
        for key, value in item.items():
            if key in item_key:
                tmp_item[key] = value
        item_list.append(tmp_item.copy())
    
    print(item_list)
    return item_list


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"

    params = set_param(keyword)
    resp = get_api(url, params)

    items = output(resp)
    ss = SpreadsheetManager()
    ss.connect_by_sheetname(SPREADSHEET_ID, "item_list")
    ss.bulk_insert(items)


if __name__ == "__main__":
   main()