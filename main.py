import discord, subprocess, wget, requests, pyrfc6266 as rfc, shutil

bot = discord.Bot()

cheese_pictures = (
    "https://media.wired.co.uk/photos/606db5957bdd70ad8525ceea/master/w_1600%2Cc_limit/Cheese_01.jpg",
    "https://static.interfood.com/assets/_1200x630_crop_center-center_82_none/Cheese-3.jpeg?v=1654596221".
    "https://www.usdairy.com/optimize/getmedia/6ab03180-cc90-4a03-a339-13b540ecc8a5/american.jpg.jpg.aspx?format=webp",
    "https://images.theconversation.com/files/316919/original/file-20200224-24701-1lk36vg.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=1200.0&fit=crop",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Swiss_cheese_cubes.jpg/640px-Swiss_cheese_cubes.jpg",
    "https://files.ekmcdn.com/c9d359/images/maasdam-cheese-725-p.jpg?v=30bc0245-5060-467d-9fa0-6b157091163c",
    "https://www.theethicaldairy.co.uk/sites/default/files/product-images/2021-03/cooking-cheese.jpg",
    "https://www.creedfoodservice.co.uk/media/catalog/product/cache/d781aa45b0623b3b1e7a18c482a05dd6/a/8/a8660bcb812826406c8db50a4005f665.jpg",
    "https://www.tirlaningredients.com/sites/default/files/styles/traditional_television/public/media/images/2022-11/cheese.png?itok=_o9WycpM",
    "https://www.creedfoodservice.co.uk/media/catalog/product/cache/d781aa45b0623b3b1e7a18c482a05dd6/c/c/cc4beb2c3d2f01345ed22de497a184b7.jpg",
    "https://lovingitvegan.com/wp-content/uploads/2018/02/Cashew-Cheese-11-500x375.jpg",
    "https://cdn.shopify.com/s/files/1/2836/2982/products/pic10_grande.jpg?v=1529434190",
    "https://cdn.shopify.com/s/files/1/0892/1540/products/IMG_1176_700x700.jpg?v=1561045917",
    "https://images.immediate.co.uk/production/volatile/sites/30/2020/02/cheddar-9fe3705.jpg",
    "https://britishop.com/storage/imgcache/617d669964eda_cheddar-e1593601314740__960x960xsquare.png",
    "https://cdn.shopify.com/s/files/1/0636/6946/9441/products/12b-scaled.jpg?v=1648462943&width=550",
    "https://cdn.shopify.com/s/files/1/0570/3018/0898/products/Italy_Cow_Asiago_Pressato_v.crop_600x.jpg?v=1655453833",
    "https://cdn.shopify.com/s/files/1/0570/3018/0898/products/Britain_Cow_Montgomery_27s_Cheddar_600x600_crop_center.jpg?v=1650976465",
    "https://media.istockphoto.com/id/485982529/zh/%E5%90%91%E9%87%8F/triangular-piece-of-cheese-vector.jpg?s=170667a&w=0&k=20&c=ak64NcLKwYm9glDLJ0geo9_uPwMiOr5GvaeHfMIdz9E=",
    "https://ca-times.brightspotcdn.com/dims4/default/2b7deda/2147483647/strip/true/crop/2048x1280+0+43/resize/1200x750!/quality/80/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2Fb2%2Fa5%2Fd673ffac73e3ff63f2f3c095fde9%2Fhomemade-american-cheese-recipes-db"
)

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

@bot.command(description="post random cheese pic")
async def cheese(ctx):
    random_cheese_pic = random.choice(cheese_pictures)
    await ctx.respond("cheesing using: `" + random_cheese_pic + "`")
    await.ctx.send(file=discord.File(random_cheese_pic))

bot.run("TOKEN GOES HERE")
