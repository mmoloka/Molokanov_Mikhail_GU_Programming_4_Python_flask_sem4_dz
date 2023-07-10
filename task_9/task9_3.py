import asyncio
import aiohttp
import aiofiles
import time
import os


async def get_image(url):
    dt = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image = await response.read()
                file_name = url.rsplit('/', 1)[-1]
                file_name = os.path.join('task_9\\task_9_3', file_name)
                async with aiofiles.open(file_name, 'wb') as f:
                    await f.write(image)
                print(f'Время загрузки файла {file_name}: {time.time() - dt: .3f} секунд')  
            else:
                print(f'Ошибка загрузки изображения {url}')      


async def main_a(urls):
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_image(url)))
    await asyncio.gather(*tasks)    


if __name__ == '__main__':
    urls = [
        'https://img.freepik.com/free-photo/modern-sports-car-speeds-through-dark-curve-generative-ai_188544-9136.jpg',
        'https://img.freepik.com/free-photo/luxury-car-interior_146671-19729.jpg',
        'https://img.freepik.com/free-photo/a-grey-metallic-jeep-with-blue-stripe-on-it_114579-4080.jpg',
        'https://img.freepik.com/free-photo/a-green-and-black-bugatti-veyron-with-a-black-and-yellow-paint_1340-23339.jpg',
        'https://img.freepik.com/free-photo/luxury-car-speeds-by-modern-building-at-dusk-generative-ai_188544-8048.jpg'
    ]
    start_time = time.time()
    asyncio.run(main_a(urls))
    print()
    print(f'Общее время загрузки: {time.time() - start_time: .3f} секунд') 