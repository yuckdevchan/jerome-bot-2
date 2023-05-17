import discord, subprocess, wget, requests, pyrfc6266 as rfc, shutil

bot = discord.Bot()

@bot.event
async def on_ready():
    bot_presence = await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="neovim", url="https://ligmaspoons.tk"))

@bot.command(description="edit latest pic")
async def edit(ctx, input_image_link: str):
    reply_loading = await ctx.respond("editing...")
    downloaded_input_image = requests.get(str(input_image_link))
    input_image = rfc.requests_response_to_filename(downloaded_input_image)
    with open(input_image, 'wb') as input_image_file:
        input_image_file.write(requests.get(input_image_link).content)
    convert_command = "convert -background none " + input_image + " images/jerome_head_small.png -layers flatten output.png"
    convert_shell_process = subprocess.run(convert_command, shell=True)
    send_image_file = await ctx.send(file=discord.File("output.png"))
    delete_downloaded_image = subprocess.run("rm -fr " + input_image, shell=True)
    delete_output_image = subprocess.run("rm -fr output.png", shell=True)

@bot.command(description="run commands")
async def cmd(ctx, command: str):
    cmd_output = subprocess.run(command, shell=True, capture_output=True)
    split_lines_cmd_output = cmd_output.stdout.splitlines()
    await ctx.respond("```" + str(split_lines_cmd_output) + "```")

@bot.command(description="post output image")
async def post(ctx):
    await ctx.respond(file=discord.File("output.png"))

bot.run("TOKEN GOES HERE")
