# -*- enconding:etf-8 -*-

import requests
import sqlite3

# using for mysql
# mysql_url = "127.0.0.1"
# username = "root"
# password = "123456"
# data_base = "covid19"


# get connection
def get_conn():
    return sqlite3.connect('covid-19.db3')


# get country
def get_country():
    country_data = requests.get("https://api.covid19api.com/countries").json()
    print("get country data is", country_data)
    return country_data


def create_table(need_import):
    try:
        conn = get_conn()
        conn.execute("select 1 from data")
    except sqlite3.OperationalError:
        file = open('sqllite.sql')
        content = file.read()
        conn = get_conn()
        conn.execute(content)
        conn.commit()
        if need_import == 'true':
            dataFile = open('data_sqllite.sql')
            conn = get_conn()
            while True:
                data = dataFile.readline()
                if data:
                    print(data)
                    conn.execute(data)
                    conn.commit()
                else:
                    break


# init data
def insertData():
    country_data = get_country()
    conn = get_conn()
    conn.cursor().execute("delete from data");
    conn.commit()
    for cus in country_data:
        try:
            getDataByCountry(cus['Slug'])
        except BaseException as e:
            print(e)
            print("connect error ")


def getDataByCountry(country,start,end):
        url = "https://api.covid19api.com/country/" + country + "?from="+start+"T00:00:00Z&to="+end+"T00:00:00Z"
        print(url)
        cusRes = requests.get(url).json()
        # insert data to
        if len(cusRes) > 0:
            for data in cusRes:
                conn = get_conn()
                sql = "insert into data(country,country_code,province,city,city_code,lat,lon,stat_date,active,Recovered,Deaths,Confirmed) values ('%s','%s','%s','%s','%s','%s','%s','%s',%d,%d,%d,%d)" % (
                    data["Country"],
                    data["CountryCode"],
                    data["Province"],
                    data["City"],
                    data["CityCode"],
                    data["Lat"],
                    data["Lon"],
                    data["Date"],
                    data["Active"],
                    data["Recovered"],
                    data["Deaths"],
                    data["Confirmed"],
                )
                print(sql)
                conn.cursor().execute(sql)
                conn.commit()
                conn.close()
