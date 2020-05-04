import psycopg2


class ManagingDatabase:
    def __init__(self):
        # connect to Database
        connection_string = "host='localhost' dbname='gis' user='docker' password='docker' port=35432"
        try:
            self.connection = psycopg2.connect(connection_string)
            self.connection.autocommit = True
            print('connected to Database!')
        except Exception as ex:
            print('could not connect to database!', {"exception": ex})

    def sql_execution(self, command, to_fetch=True):
        try:
            # based on best practices, it is decided to create and close cursor after every execution
            cursor = self.connection.cursor()
            cursor.execute(command)
            if to_fetch:
                output = cursor.fetchall()
                cursor.close()
                return output
            else:
                cursor.close()
        except (psycopg2.OperationalError, psycopg2.InterfaceError) as ex:
            print("connection to Database is not alive!", {"exception": ex})
            self.connection_checker_var = False
            return False
        except Exception as ex:
            # for the case when previous execution failed rollback function is used
            self.connection.rollback()
            print("something went wrong in SQL", {"exception": ex, "SQL command": command})
            return False

    def insert_data(self, name, category, price, lat, lon):
        sql = """
        INSERT INTO services(ts, name, category, price, location)
        VALUES (NOW(), '{}', '{}', {}, {});
        """
        data = (name, category, price, "ST_GeomFromText('POINT({} {})', 4326)".format(lon, lat))
        # print(sql.format(*data))
        self.sql_execution(sql.format(*data), to_fetch=False)

    def request(self, category, price, user_lat, user_lon, radius=500):
        sql = """
        SELECT "name", price, ST_AsText("location") FROM services
        WHERE ST_DWithin(
          location::geography,
          ST_GeomFromText('POINT({user_lon} {user_lat})',4326)::geography,
          {radius} -- DISTANCE IN METERS
        ) AND category='{category}'
        AND price<={price};
        """.format(category=category, price=price, radius=radius, user_lat=user_lat, user_lon=user_lon)
        return self.sql_execution(sql)


if __name__ == '__main__':
    search = ManagingDatabase()
    # search.insert_data('Синнабоны', 'Выпечка', 500, 51.116041, 71.433403)
    category = 'Выпечка'
    price = 500
    radius = 500
    user_lat = 51.115990
    user_lon = 71.431238
    res = search.request(category, price, user_lat, user_lon, radius)
    print(res)
