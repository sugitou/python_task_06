from api import get_api
import numpy as np
import pandas as pd


def ranking_param(id):
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


def ranking_output(resp):
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
    # print(item_list)
    items_df = pd.DataFrame(item_list)
    # ヘッダー変更
    # items_df.columns = ['ランキング', '商品名', '商品価格', '説明文', '商品URL', 'ジャンルID']
    # csvに出力
    items_df = items_df.to_csv('./rakuten_ranking.csv',
                                columns=['rank', 'itemName', 'itemPrice', 'itemCaption', 'itemUrl', 'genreId'])

def rank_main():
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
    app_id = 1046134668193624354

    params = ranking_param(app_id)
    resp = get_api(url, params)

    ranking_output(resp)


rank_main()