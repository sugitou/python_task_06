import requests
import urllib


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
        "keyword" : keyword,
        "applicationId" : id,
        "hits" : 30,
        "page" : 1
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
    print()

def main():
    keyword = "鬼滅"
    # 6-2 商品名と価格
    # url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    # 6-3 最安値と最高値
    # url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
    # 6-4 ランキング
    url = ''
    app_id = 1046134668193624354

    params = set_param(app_id, keyword)
    resp = get_api(url, params)

    output_data(resp)


main()