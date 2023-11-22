from tasks import Tasks
import asyncio

tasks = Tasks()

class Steps:
    async def main():
        await tasks.abrirPagina("https://www.youtube.com/@CierOccidente2014/playlists")
        await tasks.getText()
        await tasks.cerrarPagina()
        
    asyncio.run(main())