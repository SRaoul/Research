# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:42:00 2020

@author: sraoul
"""
# pi WEB 

import pandas as pd
import os
import function
from datetime import datetime, timedelta

username = os.environ.get('sraoul')
password = os.environ.get('AnnMarLou.2021.')
ts_name = "EG_27FI5860B.Y"
# Input time in your local time
startDate = datetime(2020, 2, 25, 0, 0, 0)
endDate = startDate + timedelta(hours=10)

date = function.pi_formatting_time()
firstDate = date.convert_to_CET(startDate)
firstDate = date.utc_format(firstDate)
lastDate = date.utc_format(endDate)
lastDate = date.convert_to_CET(lastDate)

pi_values = []
timestamps = []
pi = function.pi_web_api(username, password)

date_iterate = firstDate
while date_iterate <= lastDate:
    ts = pi.get_ts_json(ts_name, date_iterate)
    pi_values = pi_values + function.extract_values(ts, 'Value')
    timestamps = timestamps + function.extract_values(ts, 'Timestamp')
    date_iterate = str(timestamps[-1:]).strip('[]')
    date_iterate = date.convert_to_CET(pd.to_datetime(date_iterate))
    date_iterate = date.utc_format(date_iterate)

timestamps = [w.replace('T', ' ') for w in timestamps]
timestamps = [w.replace('Z', '') for w in timestamps]
timestamps = pd.to_datetime(timestamps)

pi_df = pd.DataFrame({"PI_{}".format(ts_name): pi_values, 'Date': timestamps})
pi_df.set_index('Date', inplace=True)
pi_df = pi_df[pi_df.index < endDate]

del (username, password, date_iterate, pi_values, firstDate, lastDate, timestamps)
