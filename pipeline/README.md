# Pipeline

Run the taxi data ingestion script with its default settings:

```bash
uv run python ingest_data.py
```

Override any setting with a Click option, for example:

```bash
uv run python ingest_data.py --year 2021 --month 1 --pg-host localhost --target-table yellow_taxi_data
```

Run `uv run python ingest_data.py --help` to see all options and defaults.