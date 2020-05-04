from main import ManagingDatabase

manager = ManagingDatabase()

service = 'Синнабоны'
category = 'Выпечка'
price = 500
service_lat = 51.116041
service_lon = 71.433403
manager.insert_data(service, category, price, service_lat, service_lon)



