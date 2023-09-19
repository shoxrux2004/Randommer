import requests
from randommer import Randommer
from pprint import pprint

class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url=f"{self.get_url()}Phone/Generate?CountryCode=uz&Quantity=1"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url=f"{self.get_url()}Phone/IMEI?Quantity=1"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        url=f"{self.get_url()}Phone/Validate?telephone=931166974&CountryCode=uz"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        url=f"{self.get_url()}Phone/Countries"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()
    

o=Phone()
pprint(o.get_countries("64fd8245b648443a9aea0fbd8ce5a9ae"))