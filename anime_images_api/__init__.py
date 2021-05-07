import requests
import json
import os
try:
    from download import download
except:
    os.system('pip install download')
finally:
    from download import download

try:
    from rich.console import Console
    console = Console()
    log = console.log
except:
    log = print


class Anime_Images:
    """gets images from the anime image api


    # Endpoints:
    ```
        sfw:
            hug
            kiss
            slap
            wink
            kill
            pat
            cuddle
        nsfw:
            boobs
            hentai
    ```

    # Methods:
    ```
        get_sfw()
        get_nsfw()
    ```
    """

    def __init__(self):

        self.base_url = 'https://anime-api.hisoka17.repl.co/'
        self.endpoints = {
            'sfw': {
                'hug': 'img/hug',
                'kiss': 'img/kiss',
                'slap': 'img/slap',
                'wink': 'img/wink',
                'pat': 'img/pat',
                'kill': 'img/kill',
                'cuddle': 'img/cuddle'
            },
            'nsfw': {
                'boobs': 'img/nsfw/boobs',
                'hentai': 'img/nsfw/hentai'
            }
        }

    def __request(self, path=''):
        return json.loads(requests.get(f'{self.base_url}{path}').content)

    def get_sfw(self, option):
        """get a sfw image

        Args:
            option (str): what image url do you want to return?('hug', 'kiss', 'cuddle', 'pat', 'kill', slap', 'wink')
        """
        if self.endpoints['sfw'].get(option, None) != None:
            return self.__request(self.endpoints['sfw'][option])['url']
        else:
            print(
                "you must choose one of these options.\n'hug', 'kiss', 'cuddle', 'pat', 'kill', slap', 'wink'")

    def get_nsfw(self, option):
        """get a nsfw image

        Args:
            option (str): what image url do you want to return?('boobs', 'hentai')
        """
        if self.endpoints['nsfw'].get(option, None) != None:
            return self.__request(self.endpoints['nsfw'][option])['url']
        else:
            print(
                "you must choose one of these options.\n'boobs', 'hentai'")

    def help(self):
        return log(self.endpoints)

    def download(self, url, path):
        return download(url, path)
