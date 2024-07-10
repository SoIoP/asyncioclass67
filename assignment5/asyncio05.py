from random import random
import asyncio
from time import time

async def rice():
    print("Rice: preparing ingredients")
    value = 1 + random()  
    print("Rice: frying...")
    await asyncio.sleep(value)
    print(f'rice cooking {value:.2f} sec')
    await asyncio.sleep(1)
    print("Rice: ready")
    

async def noodle():
    print("Noodle: preparing ingredients")
    value = 1 + random()  
    print("Noodle: frying...")
    await asyncio.sleep(value)
    print(f'noodle cooking {value:.2f} sec')
    await asyncio.sleep(1)
    print("Noodle: ready")

async def curry():
    print("Curry: preparing ingredients")
    value = 1 + random()  
    print("Curry: frying...")
    await asyncio.sleep(value)
    print(f'curry cooking {value:.2f} sec')
    await asyncio.sleep(1)
    print("Curry: ready")
    

async def main():
    rice_task = asyncio.create_task(rice(), name ="rice")    
    noodle_task = asyncio.create_task(noodle(), name ="noodle")    
    curry_task = asyncio.create_task(curry(),name = "curry") 
    done,pending = await asyncio.wait([rice_task,noodle_task,curry_task], return_when=asyncio.FIRST_COMPLETED)
    first = done.pop()
    print(first.get_name())

asyncio.run(main())
