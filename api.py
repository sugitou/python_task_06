import requests
import urllib
import numpy as np
import pandas as pd

def set_param(id, keyword):
    # 6-2
    # param = {
    #     "format" : "json",
    #     "keyword" : keyword,
    #     "applicationId" : id,
    #     "availability" : 0,
    #     "hits" : 30,
    #     "page" : 1,
    #     "sort" : "-updateTimestamp"
    # }

    # 6-3
    # param = {
    #     "format" : "json",
    #     "keyword" : keyword,
    #     "applicationId" : id,
    #     "hits" : 30,
    #     "page" : 1
    # }
    # return param

    # 6-4
    param = {
        "format" : "json",
        "applicationId" : id,
        "hits" : 30,
        "page" : 1,
        "age" : 20,
        "carrier" : 0,
        "sex" : 0
        # 指定するとエラー？
        # "genreId" : "100316"
        # "period" : "realtime"
    }
    return param

def get_api(url, params):
    result = requests.get(url, params)
    return result.json()

def output_data(resp):
    # 6-2
    # for i, item in enumerate(resp['Items']):
    #     print('No.', i+1)
    #     print('itemName :', item['Item']['itemName'])
    #     print('itemPrice:' + ' ￥' + str(item['Item']['itemPrice']))

    # 6-3
    # for i, prdct in enumerate(resp['Products']):
    #     print('No.', i+1)
    #     print('productName :', prdct['Product']['productName'])
    #     print('minPrice:' + ' ¥' + str(prdct['Product']['salesMinPrice']))
    #     print('maxPrice:' + ' ¥' + str(prdct['Product']['salesMaxPrice']))

    # 6-4
    # for文を回してdictを作る
    item_key = ['rank', 'itemName', 'itemPrice', 'itemCaption', 'itemUrl', 'genreId']
    item_list = []
    for i in range(0, len(resp['Items'])):
        tmp_item = {}
        item = resp['Items'][i]['Item']
        for key, value in item.items():
            if key in item_key:
                tmp_item[key] = value
        item_list.append(tmp_item.copy())

    # データフレームを作成
    items_df = pd.DataFrame(item_list)
    # 列の順番を入れ替える
    items_df = items_df.to_csv('./rakuten_ranking.csv',
    columns=['rank', 'itemName', 'itemPrice', 'itemCaption', 'itemUrl', 'genreId'])


def main():
    keyword = "鬼滅"
    # 6-2 商品名と価格
    # url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    # 6-3 最安値と最高値
    # url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
    # 6-4 ランキング
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
    app_id = 1046134668193624354

    params = set_param(app_id, keyword)
    resp = get_api(url, params)

    output_data(resp)


main()