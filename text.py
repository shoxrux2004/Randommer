import requests
from randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        url=f"{self.get_url()}Text/LoremIpsum?loremType=normal&type=paragraphs&number=123"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()
    
    def generate_password(self, api_key: str, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        url=f"{self.get_url()}Text/Password?length=10&hasDigits=true&hasUppercase=true&hasSpecial=true"
        headers={
            "X-Api-Key":api_key
        }
        response=requests.get(url,headers=headers)
        return response.json()
    
o=Text()
print(o.generate_password("64fd8245b648443a9aea0fbd8ce5a9ae",12,"true","true","true"))
