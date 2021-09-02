from api import *

def test_set_param():
    app_id = 1046134668193624354
    res = set_param(app_id)
    assert res

def test_get_api():
    id = 1046134668193624354
    param = {
        "format" : "json",
        "applicationId" : id,
        "hits" : 30,
        "page" : 1,
        "age" : 20,
        "carrier" : 0,
        "sex" : 0
    }
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
    res = get_api(url, param)

    assert len(res['Items']) >= 1
    assert res['Items'][0]['Item']['itemName']

# def test_output_data():
#     id = 1046134668193624354
#     param = {
#         "format" : "json",
#         "applicationId" : id,
#         "hits" : 30,
#         "page" : 1,
#         "age" : 20,
#         "carrier" : 0,
#         "sex" : 0
#     }
#     url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
#     resp = get_api(url, param)
#     res = output_data(resp)

#     assert res