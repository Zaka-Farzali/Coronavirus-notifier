import datetime #for reading present date
import time 
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC
# Create your views here.

def api_view():
    url = "https://corona.lmao.ninja/v2/countries/Hungary?yesterday&strict&query%20"
    r = requests.get(url).json()
    while(True):
        notification.notify(
            #title of the notification,
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            #the body of the notification
            message = "Country : {country}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nToday recovered :{todayrecovered}\nTotal cases :{cases}\nTotal recovered:{totalrecovered}".format(
                        country = r['country'],
                        todaycases = r['todayCases'],
                        todaydeaths = r['todayDeaths'],
                        todayrecovered = r['todayRecovered'],
                        cases = r['cases'],
                        totalrecovered = r['recovered']),
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = "Paomedia-Small-N-Flat-Bell.ico",
            # the notification stays for 50sec
            timeout  = 15
        )
        #sleep for 4 hrs => 60*60*4 sec
        #notification repeats after every 4hrs
        time.sleep(60*60*4)
api_view()
