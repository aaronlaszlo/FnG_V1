import requests, csv, json, urllib
import time
from fake_useragent import UserAgent
from datetime import datetime, date
from dateutil import parser
import schedule

def get_fng():
    
    #FNG API URL
    URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata/" 
    
    #SET DATE
    todayDATE = str(date.today())
    #DEFINE USER AGENT
    ua = UserAgent()

    #RANDOM USER AGENT TO CONTINUE REQUESTS WITHOUT BLOCKING 
    headers = {
       'User-Agent': ua.random,
       }

    #REQUEST URL
    r = requests.get(URL + todayDATE, headers = headers)
    #READ AS JSON DATA
    data = r.json()

    #GET TIME & DATE (ISO 8601)
    stringtime =(data['fear_and_greed']['timestamp'])

    #PRINT SCORE
    print("Score: ", data['fear_and_greed']['score'])
    #PRINT RATING
    print("Rating: ", data['fear_and_greed']['rating'])
    #PRINT DATE
    print("Date: ",datetime.fromisoformat(stringtime).strftime('%Y-%m-%d'))
    #PRINT TIME
    print("Time: ",datetime.fromisoformat(stringtime).strftime('%H:%M:%S'))


#SCHEDULER
schedule.every(30).minutes.do(get_fng)
#RUN SCHEDULE
while(True):
    schedule.run_pending()
    time.sleep(10)

