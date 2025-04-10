import asyncio
from aiohttp import web
from websockets.server import serve

# Sessões válidas
sessions = set()

# Rota HTTP: registra uma sessão
async def register_session(request):
    session_id = request.query.get("id")
    if session_id:
        sessions.add(session_id)
        print(f"ID registrado: {session_id}")
        return web.Response(
            text=f"Sessão {session_id} registrada.",
            headers={"Access-Control-Allow-Origin": "*"}
        )
    return web.Response(status=400, text="ID ausente.")

# WebSocket handler: só aceita conexões com ID válido
async def ws_handler(websocket, path):
    if path.startswith("/ws/"):
        session_id = path[len("/ws/"):]
        if session_id in sessions:
            print(f"Cliente conectado com ID: {session_id}")
            try:
                async for message in websocket:
                    print(f"[{session_id}] Mensagem recebida: {message}")
                    await websocket.send(f"[{session_id}] {message}")
            except Exception as e:
                print(f"Erro com {session_id}: {e}")
        else:
            print(f"ID inválido: {session_id}")
            await websocket.close(code=4000, reason="Sessão inválida.")
    else:
        await websocket.close()

# Inicializa os servidores HTTP e WebSocket
async def main():
    # HTTP
    app = web.Application()
    app.router.add_get("/stream", register_session)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()
    print("Servidor HTTP escutando em http://localhost:8080/stream")

    # WebSocket
    async with serve(ws_handler, "localhost", 8765):
        print("Servidor WebSocket escutando em ws://localhost:8765/ws/")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
