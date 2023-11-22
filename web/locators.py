from page import Page

class Locators(Page):
    #Si el parámetro es 0 recibe un css selector, sino recibe un xpath
    async def testSelector(self):
        selector = super().getElement(1,'//div[contains(text(),"Sort by")]')
        return selector
    
    async def uploadDate(self):
        selector = super().getElement(0,'yt-formatted-string#info span+span+span')
        return selector
    
    async def showMore(self):
        selector = super().getElement(0,'#snippet')
        return selector
    
    # yt-formatted-string#info span+span+span