from main import ManagingDatabase

manager = ManagingDatabase(searcher=True)

category = 'Выпечка'
price = 500
radius = 500
user_lat = 51.116041
user_lon = 71.433403
output = manager.request(category, price, user_lat, user_lon, radius)
print(output)