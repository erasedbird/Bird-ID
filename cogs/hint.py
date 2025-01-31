# hint.py | commands for giving hints
# Copyright (C) 2019  EraserBird, person_v1.32, hmmm

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from discord.ext import commands

from data.data import database, logger
from functions import channel_setup, user_setup

class Hint(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # give hint
    @commands.command(help="- Gives first letter of current bird", aliases=["h"])
    @commands.cooldown(1, 3.0, type=commands.BucketType.channel)
    async def hint(self, ctx):
        logger.info("command: hint")

        await channel_setup(ctx)
        await user_setup(ctx)

        currentBird = str(database.hget(f"channel:{str(ctx.channel.id)}", "bird"))[2:-1]
        if currentBird != "":  # check if there is bird
            await ctx.send(f"The first letter is {currentBird[0]}")
        else:
            await ctx.send("You need to ask for a bird first!")

    # give hint for goat
    @commands.command(help="- Gives first letter of current goatsucker", aliases=["goathint", "hg", "gh"])
    @commands.cooldown(1, 3.0, type=commands.BucketType.channel)
    async def hintgoat(self, ctx):
        logger.info("command: hintgoat")

        await channel_setup(ctx)
        await user_setup(ctx)

        currentBird = str(database.hget(f"channel:{str(ctx.channel.id)}", "goatsucker"))[2:-1]
        if currentBird != "":  # check if there is bird
            await ctx.send(f"The first letter is {currentBird[0]}")
        else:
            await ctx.send("You need to ask for a bird first!")

    # give hint for song
    @commands.command(help="- Gives first letter of current bird call", aliases=["songhint", "hs", "sh"])
    @commands.cooldown(1, 3.0, type=commands.BucketType.channel)
    async def hintsong(self, ctx):
        logger.info("command: hintsong")

        await channel_setup(ctx)
        await user_setup(ctx)

        currentSongBird = str(database.hget(f"channel:{str(ctx.channel.id)}", "sBird"))[2:-1]
        if currentSongBird != "":  # check if there is bird
            await ctx.send(f"The first letter is {currentSongBird[0]}")
        else:
            await ctx.send("You need to ask for a bird first!")

def setup(bot):
    bot.add_cog(Hint(bot))
