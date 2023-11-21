
import asyncio
from locatorsPage import LocatorsPage

class Tasks(LocatorsPage):

    async def abrirPagina(self, url):
        super().open(url)
        elemento = self.getElement(self.selector)
        # Extrae la información del elemento
        informacion = elemento.text
        print('Información extraída:', informacion)

        # Cierra el navegador
        quit()

tasks = Tasks()
asyncio.run(tasks.abrirPagina("https://www.youtube.com/@CierOccidente2014/playlists"))