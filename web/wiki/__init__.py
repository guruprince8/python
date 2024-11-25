import requests
from flask import jsonify, request
from flask_restful import Resource
from bs4 import BeautifulSoup

__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"

class WikiRouter(Resource):
    def fetchisocurrencies(self, url):
        url = "https://en.wikipedia.org/wiki/ISO_4217"
        data = ""
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                data = response.text
                soup = BeautifulSoup(data, "html.parser")
                #print(soup.)
                for content in soup(['style', 'script']):
                    #print(content)
                    content.decompose()
                data = ' '.join(soup.stripped_strings)

        except requests.exceptions.RequestException as e:
            print('Error', e)
        return {'message': data}

    def get(self):
        return self.fetchisocurrencies(self)

    def post(self, url):
        self.fetchisocurrencies(self, url=url)
