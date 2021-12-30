from subprocess import run
async def exec(ctx, args):
    try:
        output = run(args, capture_output=True, text=True).stdout
        await ctx.send(output)
    except Exception as e:
        await ctx.send(e)
    