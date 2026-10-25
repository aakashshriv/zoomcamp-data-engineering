# Module 1 Homework: Docker & SQL

Solutions for the Docker & SQL homework (Data Engineering Zoomcamp, Module 1).

## Question 1: Understanding Docker images

* Docker run command: docker run -it --rm  --entrypoint=bash python:3.13
* pip version check: -  pip --version
                      version - 26.2.2  

Answer: `26.2.2`

> The version differs from the options listed in the homework because the image has been updated since the live cohort.


## Question 2: Docker networking and docker-compose

Answers:
* postgres:5432
* db:5432

## Preparing the data for SQL

* Use ingest_data.py and nytaxi_zones.py under pipeline folder to ingest and load the data int postgress contianer.
* I'm going to download both of them on my local then givig them to Python through the script.

## Question 3: Counting short trips

```sql
SELECT COUNT(*)
FROM green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime <  '2025-12-01'
  AND trip_distance <= 1;
```
Answer: `8,007`

## Question 4: Longest trip for each day

```sql
SELECT CAST(lpep_pickup_datetime AS DATE)
FROM green_taxi_trips
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;
```
Answer: `2025-11-14`

## Question 5: Biggest pickup zone

Pickup zone with the largest total `total_amount` on 2025-11-18.

```sql
SELECT zones."Zone"
FROM green_taxi_trips g
JOIN zones ON g."PULocationID" = zones."LocationID"
WHERE CAST(g.lpep_pickup_datetime AS DATE) = '2025-11-18'
GROUP BY zones."Zone"
ORDER BY SUM(g.total_amount) DESC
LIMIT 1;
```
Answer: `East Harlem North`

## Question 6: Largest tip

For passengers picked up in **East Harlem North** in November 2025, which drop-off zone had the largest tip?

```sql
SELECT zdu."Zone", g.tip_amount
FROM green_taxi_trips g
JOIN zones AS zpu ON g."PULocationID" = zpu."LocationID"
JOIN zones AS zdu ON g. "DOLocationID"= zdu."LocationID"
WHERE TO_CHAR(g.lpep_pickup_datetime, 'YYYY-MM') = '2025-11'
AND zpu."Zone" = 'East Harlem North'
ORDER BY g.tip_amount DESC
LIMIT 1;
```
Answer: `Yorkville West`

## Terraform
* The exercise is inside the "terraform" folder under "01-docker-terraform"

## Question 7. Terraform Workflow

Answer: `terraform init, terraform apply -auto-approve, terraform destroy`