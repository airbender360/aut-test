from tasks import Tasks
import asyncio

tasks = Tasks()

class Steps:
    async def main():
        await tasks.abrirPagina("https://www.youtube.com/watch?v=dWxbX827Klc&list=PLAKTtN7vEpniX15TkDhNkhTaJFpdpBSm_&ab_channel=CentrodeInnovaci%C3%B3nYDesarrollo")
        await tasks.getUploadDate()
        await tasks.cerrarPagina()
        
    asyncio.run(main())