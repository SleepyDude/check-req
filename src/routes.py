from flask import current_app as app
from flask import request

@app.get("/")
def show_all():
    return "Showing all info"