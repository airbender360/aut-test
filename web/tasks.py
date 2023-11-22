from locators import Locators

class Tasks(Locators):

    async def abrirPagina(self, url):
        super().open(url)

    async def getText(self):
        info = await self.selector1()
        text = info.text
        print('Información extraída:', text)
        
    async def cerrarPagina(self):
        super().quit()