#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

def ingest_data(
        url:str,
        engine,
        target_table:str,
        compression:str,
        chunksize:int = 100000) -> None:

    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        compression=compression,
        iterator=True,
        chunksize=chunksize
    )

    first_chunk = True

    for df_chunk in tqdm(df_iter):

        if first_chunk:
            # Create table schema (no data)
            df_chunk.head(n=0).to_sql(name=target_table,
                                    con=engine,
                                    if_exists="replace")
            first_chunk = False

        # Insert chunk
        df_chunk.to_sql(name=target_table,
                            con=engine,
                            if_exists="append")    

@click.command()
@click.option("--year", type=int, default=2021, show_default=True)
@click.option("--month", type=int, default=1, show_default=True)
@click.option("--pg-user", default="root", show_default=True)
@click.option("--pg-pass", default="root", show_default=True)
@click.option("--pg-host", default="localhost", show_default=True)
@click.option("--pg-port", type=int, default=5432, show_default=True)
@click.option("--pg-db", default="ny_taxi", show_default=True)
@click.option("--target-table", default="yellow_taxi_trips", show_default=True)
@click.option("--compression", default="gzip", show_default=True)
@click.option("--chunksize", default=100000, show_default=True)
def main(
        year: int,
        month: int,
        pg_user: str,
        pg_pass: str,
        pg_host: str,
        pg_port: int,
        pg_db: str,
        target_table: str,
        compression: str,
        chunksize:int
) -> None:
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow'
    url = f"{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz"
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    ingest_data(
        url=url,
        engine=engine,
        target_table=target_table,
        compression=compression,
        chunksize=chunksize

    )
if __name__ == "__main__":
    main()
