from django.contrib.sitemaps import Sitemap

class AbstractSitemapClass():
    changefreq = 'daily'
    url = None
    def get_absolute_url(self):
        return self.url
    
class StaticSitemap(Sitemap):
    
    def __init__(self, pages, priority=1.0, changefreq='monthly'):
        self._pages = pages
        self.priority = priority
        self.changefreq = changefreq
    
        self._main_sitemaps = []
        
        for page in self._pages:
            sitemap_class = AbstractSitemapClass()
            sitemap_class.url = page        
            self._main_sitemaps.append(sitemap_class)

    def items(self):
        return self._main_sitemaps