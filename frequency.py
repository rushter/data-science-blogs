# coding: utf-8
from datetime import datetime, timedelta
import feedparser
import re
import time

readme = open('README.md').read()
feeds = re.findall('\[\(RSS\)\] \((.*?)\)', readme)

past_week = datetime.now() - timedelta(days=7)
past_month = datetime.now() - timedelta(days=30)

per_week = 0
per_month = 0

for url in feeds:
    data = feedparser.parse(url)
    for f in data.entries:
        try:
            dt = datetime.fromtimestamp(time.mktime(f.updated_parsed))
        except Exception as err:
            print(err, url)
            break

        if dt >= past_week:
            per_week += 1

        if dt >= past_month:
            per_month += 1

print('Blog post frequency (roughly): {} per week / {} per month.'.format(per_week, per_month))
