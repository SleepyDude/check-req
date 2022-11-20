from flask import current_app as app
from flask import request, render_template

@app.get("/")
def show_all():
    headers = [
        {
            'name': 'accept',
            'value': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        },
        {
            'name': 'accept-encoding',
            'value': 'gzip, deflate, br'
        },
        {
            'name': 'accept-language',
            'value': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
        }
    ]
    return render_template("check_all.html", headers=headers)