import hashlib
import datetime
import requests
from error_codes import error_dict


def createSignature(api_key, api_secret):
    m = hashlib.md5()
    APIKEY = api_key
    APISECRET = api_secret
    TimeStampNow = str(int(datetime.datetime.now().timestamp()))
    params = {'symbol': 'usdt_btc', 'type': 'kline_1m', 'timestamp': TimeStampNow, 'apiKey': APIKEY,
              'apiSecret': APISECRET}
    sorted_params = sorted(params.items(), key=lambda element: element[0])
    newstr = ''.join(element[1] for element in sorted_params)
    m.update(newstr.encode())
    signature = m.hexdigest()
    return signature


def limit_price_order(symbol, price, amount, order_type, apiKey, req_timestamp, sign):
    url = "https://openapi.digifinex.com/v2/trade"
    payload = "\"symbol\": \"{}\",\"price\": {},\"amount\": {},\"type\": \"{}\",\"apiKey\": \"{}\"," \
              "\"timestamp\": {},\"sign\": \"{}\"".format(symbol, price, amount, order_type, apiKey, req_timestamp,
                                                          sign)
    payload = "{"+payload+"}"
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    resp = response.json()
    if resp['code'] > 0:
        return {"code": resp["code"], "message": error_dict[resp["code"]]}
    else:
        return resp

