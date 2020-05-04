from main import ManagingDatabase

samples = [
    ('Торты', 'Выпечка', 700, 51.116312, 71.429046),
    ('Блины', 'Выпечка', 200, 51.116041, 71.433403),
    ('Синнабоны', 'Выпечка', 500, 51.114282, 71.421859),
    ('Пирожки', 'Выпечка', 200, 51.116821, 71.430187),
]

manager = ManagingDatabase()
for sample in samples:
    manager.insert_data(sample[0], sample[1], sample[2], sample[3], sample[4])
print("Initial Data Added!")
