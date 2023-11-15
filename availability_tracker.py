from lxml import html
import requests
from time import sleep
from email_sender import send_email
from MachineLearning.availability_predictor import AvailabilityPredictor
import HistoricalData as historical_data

XPATH_AVAILABILITY = '//span[@class="availability-text"]//text()'

class ProductAvailabilityTracker:
    def __init__(self, url, email):
        self.url = url
        self.email = email
        self.availability.predictor = AvailabilityPredictor(historical_data)

    def check_availability(self):
        print("Processing: ", self.url)
        availability = self.check(self.url, XPATH_AVAILABILITY)
        print(availability)
        if availability :
            self.send_email(availability, self.url, self.email)

    def check(self, url, xpath):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        page = requests.get(url, headers=headers)

        for _ in range(20):
            sleep(3)
            doc = html.fromstring(page.content)
            raw_availability = doc.xpath(xpath)
            availability = ''.join(raw_availability).strip() if raw_availability else None
            return availability

    def extract_features(url):
        # Use web scraping or any other method to extract relevant features from the product's webpage
        # Return a list of features for the given URL
        features = []
        return features


    def check_availability_prediction(self):
        product_features = self.extract_features(self.url)
        prediction = self.check_availability_prediction(product_features)
        return prediction

    def send_email(self, ans, product, recipient_email):
        send_email(product, ans, recipient_email)

    def job(self):
        print("Tracking....")
        self.check_availability()