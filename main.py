import discord, subprocess, wget, requests, pyrfc6266, shutil

bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="neovim", url="https://ligmaspoons.tk"))

@bot.command(description="edit latest pic")
async def edit(ctx, input_image_link: str):
    await ctx.respond("editing...")
    requests_input_image = requests.get(str(input_image_link))
    input_image = pyrfc6266.requests_response_to_filename(requests_input_image)
    with open(input_image, 'wb') as f:
        f.write(requests.get(input_image_link).content)
    convert_command = "convert -background none " + input_image + " images/jerome_head_small.png -layers flatten output.png"
    subprocess.run(convert_command, shell=True)
    await ctx.send(file=discord.File("output.png"))
    subprocess.run("rm -rf " + input_image, shell=True)
    subprocess.run("rm -rf output.png", shell=True)

@bot.command(description="run commands")
async def cmd(ctx, command: str):
    cmd_output = subprocess.run(command, shell=True, capture_output=True)
    split_lines_cmd_output = cmd_output.stdout.splitlines()
    await ctx.respond("```" + str(split_lines_cmd_output) + "```")

@bot.command(description="post output image")
async def post(ctx):
    await ctx.respond(file=discord.File("output.png"))

bot.run("TOKEN GOES HERE")
