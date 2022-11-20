from flask import current_app as app
from flask import request, render_template
from pprint import pprint as pp

@app.get("/")
def show_all():
    headers = request.headers
    # pp(hdrs)
    cookies = request.cookies
    pp(cookies)
    return render_template("check_all.html", headers=headers, cookies=cookies)