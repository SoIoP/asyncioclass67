import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = 'C:\\Users\\Lenovo\\Documents\\GitHub\\asyncioclass67\\assignment07\\pokemon\\pokemonapi'
pokemonmove_directory = 'C:\\Users\\Lenovo\\Documents\\GitHub\\asyncioclass67\\assignment07\\pokemon\\pokemonmove'

async def read_write(path):
    async with aiofiles.open(path, mode='r') as f:
        contents = await f.read()

    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = (move['move'] ['name'] for move in pokemon['moves'])

    async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt,', mode='w') as f:
        await f.write('\n'.join(moves))

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')
    # Iterate through all json files in the directory.
    coro = [read_write(path) for path in pathlist]
    await asyncio.gather(*coro)

asyncio.run(main())
