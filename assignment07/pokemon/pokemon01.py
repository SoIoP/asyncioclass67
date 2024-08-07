import aiofiles
import asyncio
import json

pokemonapi_directory = 'C:\\Users\\Lenovo\\Documents\\GitHub\\asyncioclass67\\assignment07\\pokemon\\pokemonapi'
pokemonmove_directory = 'C:\\Users\\Lenovo\\Documents\\GitHub\\asyncioclass67\\assignment07\\pokemon\\pokemonmove'
async def main():
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode='r') as f:
        contents = await f.read()

    pokemon = json.loads(contents)
    print(pokemon['name'])

asyncio.run(main())