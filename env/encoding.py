import base64
import shlex
async def base64ToAscii(ctx, ct):
    try:
        for cts in ct:
            await ctx.send(f"{cts}: {base64.b64decode(cts).decode('utf-8')}")
    except Exception as e:
        await ctx.send(e)

async def hexToAscii(ctx, ct):
    try:
        for cts in ct:
            await ctx.send(f"{cts}: {bytes.fromhex(cts).decode('utf-8')}")
    except Exception as e:
        await ctx.send(e)

async def binaryToAscii(ctx,ct):
    try:
        for cts in ct:
            binary_int = int(cts, 2)
            byte_number = binary_int.bit_length() + 7 // 8
            binary_array = binary_int.to_bytes(byte_number, "big")
            ascii_text = binary_array.decode()
            await ctx.send(f"{cts}: {str(ascii_text)}")
    except Exception as e:
        await ctx.send(e)