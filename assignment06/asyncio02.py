#example of an aysnchronous iterator with aysnc for loop
import asyncio

#define an aysnchronous iterator
class AsyncIterator():
    #constructor, define some state
    def __init__(self) :
        self.counter = 0
        
    #create an instance of the iterator
    def __aiter__(self):
        return self
    
    #return the next awitable
    async def __anext__(self):
        #check for no further item
        if self.counter >= 10:
            raise StopAsyncIteration
        #increment the counter
        self.counter+=1
        #simulate work
        await asyncio.sleep(1)
        #return the counter value
        return self.counter
    
#main coroutine
async def main():
    # loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(item)

#execute the asyncio program
asyncio.run(main())