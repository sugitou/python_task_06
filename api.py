import requests
import urllib
import numpy as np
import pandas as pd
import pprint


def set_param(id, keyword=''):
    param = {
        "format" : "json",
        "keyword" : keyword,
        "applicationId" : id,
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
    
    pprint.pprint(item_list)
    return item_list


def api_main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    app_id = 1046134668193624354

    params = set_param(app_id, keyword)
    resp = get_api(url, params)

    items = output(resp)


api_main()