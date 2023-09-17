import requests
from randommer import Randommer
from pprint import pprint


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        url=f"{self.get_url()}Card"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()
    

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        url=f"{self.get_url()}Card/Types"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()
        
o=Card()
pprint(o.get_card_types("64fd8245b648443a9aea0fbd8ce5a9ae"))