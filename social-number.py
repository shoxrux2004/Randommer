import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        url=f"{self.get_url()}SocialNumber"
        headers={
            "X-Api-Key":api_key
        }
        
        response=requests.get(url,headers=headers)
        return response.json()
o=SocialNumber()
print(o.get_SocialNumber("64fd8245b648443a9aea0fbd8ce5a9ae"))