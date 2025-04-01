import asyncio

async def async_function(string):
    print(f"Hello {string}")
    await asyncio.sleep(1)
    print(f"{string}'s function complete")

async def main_async():
    tasks = [async_function("Shrimat"), async_function("Kapoor"), async_function("Python")]
    await asyncio.gather(*tasks)

asyncio.run(main_async())