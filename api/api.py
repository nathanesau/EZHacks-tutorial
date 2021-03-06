import asyncio
import os
import pandas as pd
import requests
from dataprep.connector import connect
from dataprep.eda import plot
from datetime import datetime

BASEDIR = os.path.dirname(os.path.realpath(__file__))

def requests_example():
    # requests syntax
    response = requests.get((
        f"https://finnhub.io/api/v1/calendar/earnings?from={datetime(2011,1,1)}"
        f"&to={datetime.now()}&symbol=TSLA&token=c11tv0v48v6p2grlkudg"
    ))
    print(response.json())

@asyncio.coroutine
async def dataprep_example():
    """
    creating the json for dataprep:

    - each endpoint (/calendar/earnings, etc.) has its own json file
    - 
    """
    # dataprep syntax
    conn = connect(f"{BASEDIR}/finnhub", _auth={"access_token": "c11tv0v48v6p2grlkudg"})
    response = await conn.query('earnings_calendar', symbol='TSLA', from_=datetime(2011,1,1), to=datetime.now())
    print(response)

def plot_example():
    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    plot(iris).save("figure.html")

if __name__ == "__main__":
    #print("\nrequests example:")
    #requests_example()

    #print("\ndataprep example:")
    #asyncio.run(dataprep_example())

    print("\nplot example:")
    plot_example()
