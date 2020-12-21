from Scrape import SCRAPE_MANAGER
DRIVER_PATH = '/Users/niklas/Documents/Projekter/python_filer/chromedriver'
WAIT_TIME = 5

car = SCRAPE_MANAGER(WAIT_TIME, DRIVER_PATH, True)

car.load_page()

car.search_plate("CF32784")

print(car.get_basic_car_info())

print(car.get_debt_info())

car.end_session()