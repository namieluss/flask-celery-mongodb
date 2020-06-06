__author__ = "Suleiman"

from datetime import datetime

from flask import request
from requests import get as http_getter

from . import app, db, celery


@celery.task
def check_who_and_where(page):
    with app.app_context():
        # get ip address of the visitor
        ip = request.access_route[0]

        d = http_getter("https://ipapi.co/{}/json/".format(ip)).json()
        if d and not d.get('reserved'):
            store = {
                "ip": d.get('ip', ''),
                "city": d.get("city", ''),
                "region": d.get("region"),
                "org": d.get('org', ''),
                "country_code": d.get("country_code", ''),
                "country_name": d.get('country_name', ''),
                "latitude": d.get('latitude', ''),
                "longitude": d.get('longitude', ''),
                "browser": request.user_agent.browser,
                "platform": request.user_agent.platform,
                "date": datetime.today(),
                "page": page
            }
            db.page_access_log.insert(store)
