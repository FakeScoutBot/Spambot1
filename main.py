import glob
from pathlib import Path
from utils import load_plugins
import logging
import asyncio
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "AltronX/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n𝗦𝗛𝗔𝗥𝗔 𝗫 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 𝗗𝗘𝗣𝗟𝗢𝗬𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬☠️😈\nMy Master ---> @𝗦𝗛𝗔𝗥𝗔_𝗫𝗗")


async def main():
    await MK1.run_until_disconnected()
    await MK2.run_until_disconnected()
    await MK3.run_until_disconnected()
    await MK4.run_until_disconnected()
    await MK5.run_until_disconnected()
    await MK6.run_until_disconnected()
    await MK7.run_until_disconnected()
    await MK8.run_until_disconnected()
    await MK9.run_until_disconnected()
    await MK10.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
