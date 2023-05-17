@bot.command(description="run commands")
async def cmd(ctx, command: str):
    cmd_output = subprocess.run(command, shell=True, capture_output=True)
    split_lines_cmd_output = cmd_output.stdout.splitlines()
    await ctx.respond("```" + str(split_lines_cmd_output) + "```")

@bot.command(description="post output image")
async def post(ctx):
    await ctx.respond(file=discord.File("output.png"))
