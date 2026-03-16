import asyncio
import csv
import threading

from bot import bot



async def main():
    # #hsn = "P250 | X-Ray (Factory New)"
    # hsn = "Sticker | Fluxo (Holo) | Austin 2025"
    #
    # #await parse_price_history(hsn)
    # await parse_item_orders(hsn)
    ...


if __name__ == '__main__':
    threading.Thread(target=bot.run).run()
    asyncio.run(main())