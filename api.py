import requests
import urllib
import numpy as np
import pandas as pd


def set_param(id, keyword=''):
    param = {
        "format" : "json",
        "keyword" : keyword,
        "applicationId" : id,
        "availability" : 0,
        "hits" : 30,
        "page" : 1,
        "sort" : "-updateTimestamp"
    }

    return param


def get_api(url, params):
    result = requests.get(url, params)
    return result.json()


def output(resp):
    for i, item in enumerate(resp['Items']):
        print('No.', i+1)
        print('itemName :', item['Item']['itemName'])
        print('itemPrice:' + ' ￥' + str(item['Item']['itemPrice']))


def api_main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    app_id = 1046134668193624354

    params = set_param(app_id, keyword)
    resp = get_api(url, params)

    output(resp)


api_main()