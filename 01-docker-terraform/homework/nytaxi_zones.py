#!/usr/bin/env python
# coding: utf-8

#import required liabraries
import pandas as pd
from sqlalchemy import create_engine


# define data types of the columns on Pyhton side
dtype = {
    "LocationID": "Int64",
    "Borough": "string",
    "Zone": "string",
    "service_zone": "string"
}

def main():

    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

    df_zones = pd.read_csv(url, dtype=dtype)

    engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

    df_zones.head(n=0).to_sql(name="zones", con=engine, if_exists="replace")

    df_zones.to_sql(name="zones", con=engine, if_exists="append")


if __name__ == "__main__":
    main()  