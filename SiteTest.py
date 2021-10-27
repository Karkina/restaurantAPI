import unittest
from Site import Site
class SiteTest(unittest.TestCase):
    
    def test_getSites(self):
        
        result = 1106
        site = Site()
        
        assert(site.getSitesCount() == result)


    def test_getImageURLById(self):

        result = "https://whc.unesco.org/uploads/sites/site_1068.jpg"
        id = 1068
        site = Site()
        imageURL = site.getImageURLById(id)

        assert(imageURL == result)
        
        
    def test_searchAPI(self):

        result = [{
        "id": 1068,
        "name": "<I>Sacri Monti</I> of Piedmont and Lombardy",
        "yearInscribed": 2003,
        "url": "https://whc.unesco.org/en/list/1068",
        "imageUrl": "https://whc.unesco.org/uploads/sites/site_1068.jpg",
        "descriptionMarkup": "<p>The nine <em>Sacri Monti</em> (Sacred Mountains) of northern Italy are groups of chapels and other architectural features created in the late 16th and 17th centuries and dedicated to different aspects of the Christian faith. In addition to their symbolic spiritual meaning, they are of great beauty by virtue of the skill with which they have been integrated into the surrounding natural landscape of hills, forests and lakes. They also house much important artistic material in the form of wall paintings and statuary.</p>",
        "states": "Italy",
        "location": {
            "name": "Regions of Lombardy and Piedmont",
            "longitude": 9.169555556,
            "latitude": 9.169555556
        },
        "categoryName": "Cultural",
        "regionName": "North America"
    }]

        site = Site()
        imageURL = site.getSiteByNameContains("Sacri Monti")

        assert(imageURL == result)

if __name__ == '__main__':
    unittest.main()