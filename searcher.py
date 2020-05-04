from main import ManagingDatabase

manager = ManagingDatabase()

category = 'Выпечка'
price = 1000
radius = 500
user_lat = 51.115990
user_lon = 71.431238
Output = manager.request(category, price, user_lat, user_lon, radius)
print(Output)