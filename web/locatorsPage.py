from page import Page



class LocatorsPage(Page):
    #Si el parámetro es 0 recibe un css selector, sino recibe un xpath
    async def selector1(self):
        selector = super().getElement(1,'//div[contains(text(),"Sort by")]')
        return selector
    