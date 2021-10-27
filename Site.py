from SiteService import SiteService
from flask import abort
class Site:

    listSites = []
    siteService = ''

    def __init__(self):
        siteService = SiteService()
        self.listSites = siteService.getSites().json()

    def getSites(self):
        return self.listSites
    
    def getSitesCount(self):
        return len(self.getSites())
    

    def getImageURLById(self,id):
        rowId = list(filter(lambda x: x["id"] == id,self.listSites))
        return rowId[0]['imageUrl']
    
    def getSiteById(self,id):
        rowId = list(filter(lambda x: x["id"] == int(id),self.listSites))
        return rowId[0]
    
    def getSiteByNameContains(self,text):
       rowId = list(filter(lambda x: x["name"].find(text) != -1,self.listSites))
       if rowId == [] :
           abort(404)
       return rowId