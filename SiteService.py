import requests
class SiteService:

    def getSites(self):
        return requests.get('http://arest.me/api/sites')