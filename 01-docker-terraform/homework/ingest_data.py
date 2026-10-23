#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine


def ingest_data(filename:str, engine, target_table:str) -> None:

    df = pd.read_parquet(filename)

    df.head(n=0).to_sql(name=target_table, con=engine, if_exists="replace", index=False)
    
    df.to_sql(name=target_table, con=engine, if_exists="append", index=False, chunksize=100_000)    

@click.command()
@click.option("--year", type=int, default=2025, show_default=True)
@click.option("--month", type=int, default=11, show_default=True)
@click.option("--pg-user", default="postgres", show_default=True)
@click.option("--pg-pass", default="postgres", show_default=True)
@click.option("--pg-host", default="localhost", show_default=True)
@click.option("--pg-port", type=int, default=5433, show_default=True)
@click.option("--pg-db", default="ny_taxi", show_default=True)
@click.option("--target-table", default="green_taxi_trips", show_default=True)
def main(
        year: int,
        month: int,
        pg_user: str,
        pg_pass: str,
        pg_host: str,
        pg_port: int,
        pg_db: str,
        target_table: str,
) -> None:
    filename = f"green_tripdata_{year}-{month:02d}.parquet"
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    ingest_data(
        filename=filename,
        engine=engine,
        target_table=target_table,
    )


if __name__ == "__main__":
    main()
