import requests
from randommer import Randommer
from pprint import pprint

class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        url=f"{self.get_url()}Misc/Cultures"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        url=f"{self.get_url()}Misc/Random-Address?number=33&culture=en"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()

o=Misc()
pprint(o.get_random_address("64fd8245b648443a9aea0fbd8ce5a9ae",33,"en"))