from flask import current_app as app
from flask import request, render_template

@app.get("/")
def show_all():
    headers = request.headers
    # pp(hdrs)
    cookies = request.cookies
    return render_template("check_all.html", headers=headers, cookies=cookies)