import asyncio
import websockets
from typing import TYPE_CHECKING

from MultiServer import on_client_connected, Endpoint
from NetUtils import decode, encode

DEBUG = True

if TYPE_CHECKING:
    from worlds.deltarune.DeltaruneClient import DeltaruneContext


async def proxy_loop(ctx: "DeltaruneContext"):
    try:
        while not ctx.exit_event.is_set():
            if not ctx.is_connected():
                ctx.connected = False
            if len(ctx.proxy_server_msgs) > 0:
                for msg in ctx.proxy_server_msgs:
                    await ctx.send_msgs_proxy(msg)

                ctx.proxy_server_msgs.clear()
            await asyncio.sleep(0.1)
    except Exception as e:
        logger.exception(e)
        logger.info("Aborting DELTARUNE Proxy Client due to errors")


async def proxy(websocket, path: str = "/", ctx: "DeltaruneContext" = None):
    ctx.proxy_endpoint = Endpoint(websocket)
    try:
        await on_client_connected(ctx)
        if ctx.is_proxy_connected():
            async for data in websocket:
                if DEBUG:
                    logger.info(f"Incoming message: {data}")
                if not ctx.is_connected() and ctx.authenticated:
                    text = encode([{"cmd": "ProxyDisconnect"}])
                    await ctx.send_msgs_proxy(text)
                    ctx.authenticated = False
                await parse_game_packets(ctx, data)
    except Exception as e:
        if not isinstance(e, websockets.WebSocketException):
            logger.exception(e)
    finally:
        await ctx.disconnect_proxy()


async def parse_game_packets(ctx: "DeltaruneContext", data):
    for msg in decode(data):
        # connection with server is handled by proxy client already, just send back the important data
        if msg["cmd"] == "Connect":
            # Proxy is connecting, make sure it is valid
            if msg["game"] != "DELTARUNE":
                logger.info("Aborting proxy connection: game is not Pizza Tower")
                await ctx.disconnect_proxy()
                break
            # send over connection data and receiveditems if valid
            if ctx.connected_msg and ctx.is_connected():
                await ctx.send_msgs_proxy(ctx.connected_msg)
                # send tags to proxy when connected
                await ctx.send_msgs_proxy(encode([{"cmd": "UpdateTags", "tags": ctx.tags}]))
                ctx.update_items()
        elif not ctx.is_proxy_connected():
            break
        # send over any packets received from the game client to the server
        else:
            await ctx.send_msgs([msg])
