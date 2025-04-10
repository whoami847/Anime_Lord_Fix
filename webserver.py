from aiohttp import web
import asyncio

routes = web.RouteTableDef()

@routes.get("/")
async def root(request):
    return web.Response(text="Anime Lord Bot is Alive!", status=200)

async def run():
    app = web.Application()
    app.add_routes(routes)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
