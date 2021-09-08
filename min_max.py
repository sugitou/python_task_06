from api import get_api


def min_max_param(id, keyword):
    # 6-3
    param = {
        "format" : "json",
        "keyword" : keyword,
        "applicationId" : id,
        "hits" : 30,
        "page" : 1
    }
    return param


def min_max_output(resp):
    for i, prdct in enumerate(resp['Products']):
        print('No.', i+1)
        print('productName :', prdct['Product']['productName'])
        print('minPrice:' + ' ¥' + str(prdct['Product']['salesMinPrice']))
        print('maxPrice:' + ' ¥' + str(prdct['Product']['salesMaxPrice']))


def mm_main():
    keyword = "鬼滅"
    url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
    app_id = 1046134668193624354

    params = min_max_param(app_id, keyword)
    resp = get_api(url, params)

    min_max_output(resp)


mm_main()