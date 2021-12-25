import socket, argparse

async def sendudp(ctx,args):
    if "help" in args:
        await ctx.send("""
```mengirimkan packet UDP berupa ascii kepada host dan port yang ditentukan
usage: 
z-nc sendudp [-ip] <host> [-p] <port> [-m] <message> ```""")
        return
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-ip', action='store', dest='host')
        parser.add_argument('-p', action='store', dest='port',type=int)
        parser.add_argument('-m',  action='store', dest='message')
        parseArgs = parser.parse_args(args)
        ip = parseArgs.host
        port = parseArgs.port
        msg = bytes(parseArgs.message,encoding='utf-8')
        await ctx.send(f"sending UDP packet ({msg}) to {ip}:{port}...")
        sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
        sock.sendto(msg, (ip, port))
        await ctx.send("UDP packet sent")

    except Exception as e:
        await ctx.send(e)

        
    return