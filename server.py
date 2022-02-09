from archive import Archive

from discord.ext import tasks
import discord
import re


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.archive = Archive()

    async def on_ready(self):
        print(f"Logged in as {self.user.name} {self.user.id}")

    async def on_message(self, message):
        author = message.author.id
        if author == self.user.id:
            return

        if message.content.startswith("$help"):
            await message.channel.send(
                """Notifies you about changes to specific website content. Give me the website url and the CSS selector for the content and I will ping you when that content is changed.

**Usage**:
```
$notify [url] [selector]
```
**Example** notifying when item goes in or out of stock:
```
$notify https://sim-lab.eu/shop/product/slc001-gt1-evo-sim-racing-cockpit-446#attr= #\\31 897
```
**Finding CSS selector in chrome**:
> 1)  Hover the cursor over the image and right click mouse.
> 2)  Select Inspect.
> 3)  See the highlighted image code.
> 4)  Right click on the highlighted code.
> 5)  Select Copy > Copy selector."""
            )

        elif message.content.startswith("$notify"):
            try:
                _, url, *rest = message.content.split(" ")
                selector = " ".join(rest)

                self.archive.add(url, selector, author)

                await message.channel.send(
                    f"{url} is now being tracked. You will get notified when the content at {selector} changes."
                )
            except:
                await message.channel.send(
                    "Invalid usage of $notify, use $help for usage syntax."
                )

    @tasks.loop(seconds=1800)
    async def check_tickets(self):
        channel = self.get_channel(365305729848180738)

        print("Checking for changes")

        for url, _, author, _ in self.archive.update():
            print(
                f"Notified {author} about {url}, now tracking {len(self.delta.tickets)} tickets"
            )
            message = f"Hi <@{author}>, the content at {url} has changed!"
            await channel.send(message)

    @check_tickets.before_loop
    async def before_task(self):
        await self.wait_until_ready()
