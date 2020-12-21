from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SCRAPE_MANAGER():
    def __init__(self, wait_time, driver_path, headless):
        """
        Initialisere variabler for objektet

        Args:
            wait_time (int): Hvor lang selenium maksimum skal vente på, at hjemmesiden indlæser.
            driver_path (String): Angivelse af, hvor driveren ligger på computeren.
            headless (bool): Skal browseren åbnes - så man kan følge med, når websiden scrapes.
        """
        self.WEBSITE = "https://www.nummerplade.net/"
        self.WAIT_TIME = wait_time
        self.DRIVER_PATH = driver_path
        self.options = Options()
        self.options.headless = headless
        self.driver = webdriver.Chrome(options=self.options, executable_path=self.DRIVER_PATH)

    def load_page(self):
        """
        Indlæser siden
        """
        self.driver.get(self.WEBSITE)

    def search_plate(self, reg_nr):
        """
        Søger efter nummerplade

        Args:
            reg_nr (String): Nummerpladen som man søger efter
        """
        try:
            WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.presence_of_element_located((By.ID, "search_regnr"))
            )
            self.driver.find_element_by_id("search_regnr").send_keys(reg_nr)
            self.driver.find_element_by_id("search_regnr_button").click()

        except:
            print("fejl")

    def get_basic_car_info(self):
        """
        Retunerer, hvilken bil der er tale om, ud fra nummerpladen

        Returns:
            Dictionary: Mærke - model - variant
        """

        try:
            WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.presence_of_element_located((By.ID, "maerke"))
            )
            return {
                "brand": self.driver.find_element_by_id("maerke").text,
                "model": self.driver.find_element_by_id("model").text,
                "variant": self.driver.find_element_by_id("variant").text
            }
        except:
            print("Fejl")

    def get_debt_info(self):
        """
        Tjekker om der er gæld i bilen, og hvis dette er tilfældet,
        finder den ud af hvor stor det oprindelige lån var, og hvornår lånet blev optaget.

        Returns:
            Dictionary: Er der gæld - oprindelige beløb - dato
        """

        self.driver.find_element_by_id("btn-bilbogen").click()

        try:
            WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.presence_of_element_located((By.ID, "result-bilbogen-head"))
            )
            
            debt = self.driver.find_element_by_id("result-bilbogen-head").text

            if "Ingen"  in debt:
                return {
                    "debt": False,
                    "value": "-", 
                    "date": "-"
                }
            else:
                return {
                    "debt": True, 
                    "value": self.driver.find_element_by_id("hovedstol").text, 
                    "date": self.driver.find_element_by_id("dokument_dato").text
                    }
        except:
            print("Fejl")
            
            

    def end_session(self):
        """
        Afslutter
        """
        self.driver.quit()
