from flask import current_app as app
from flask import request, render_template, jsonify

import requests

@app.get("/")
def show_all():
    headers = request.headers
    # pp(hdrs)
    cookies = request.cookies
    return render_template("check_all.html", headers=headers, cookies=cookies)

@app.get("/v1/get_my_ip_data")
def ip_data():
    ip = request.remote_addr
    print('ip:', ip)
    resp = None
    try:
        resp = requests.get('http://ip-api.com/json/{}'.format(ip), timeout=3)
    except Exception as e:
        print(e)

    country = 'N/A'
    country_code = 'N/A'
    if resp and resp.status_code == 200:
        rjson = resp.json()         
        print(rjson)
        if rjson['status'] == 'success':
            country = rjson['country']
            country_code = rjson['countryCode']

    return jsonify({
        'ip': ip,
        'country': country,
        'country_code': country_code
        }), 200
