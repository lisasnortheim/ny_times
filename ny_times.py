import requests
import json
import pandas as pd
import datetime as dt


def get_todays_articles():
    today = dt.date.today()
    year = today.year
    month = today.month
    mykey = 'WDi0mXuIcl8iuL6Dxj4YsC7segqNd7i1'

    years = [year-x for x in [25,50,100,150]]
    multi_yr_df = pd.DataFrame()
    for yr in years:
        articles = nyt_archive_api(yr,month,mykey)
        df = pd.json_normalize(articles['response'], record_path = 'docs')
        multi_yr_df = pd.concat([multi_yr_df,df])

    multi_yr_df['pub_date'] = pd.to_datetime(multi_yr_df['pub_date'])
    multi_yr_df = multi_yr_df[multi_yr_df['pub_date'].dt.day == today.day]

def nyt_archive_api(year, month, mykey):
  requestUrl = f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={mykey}'
  requestHeaders = {
    "Accept": "application/json"
  }

  response = requests.get(requestUrl, headers=requestHeaders)
  return response.json()

