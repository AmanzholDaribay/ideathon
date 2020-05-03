# Korshi Komekshi

Korshi Komekshi is an InDriver for services and goods.

This repository contains instructions for creating Database and some of the Backend functions for Service/Good Insertion and Service/Good Search.  

## Installation
Download repository:
```bash
git clone https://github.com/AmanzholDaribay/ideathon
```
In database directory, Build and Run Database using [Docker](https://www.docker.com/):
```bash
sudo docker-compose up -d
```
Note: the Database will be filled with random samples.

## Usage
In searcher.py, for Service/Good Search run the following:
```python
search = Searcher()

category = 'Выпечка'    # distinct categories
price = 500             # price in kzt
radius = 500            # search diameter 
user_lat = 51.116041    # user latitude
user_lon = 71.433403    # user longitude
res = search.request(category, price, user_lat, user_lon, radius)   # returns available services/goods
```
## Credits
For building Database with Postgis extension this project uses [docker-postgis](https://github.com/kartoza/docker-postgis#docker-postgis).