import requests
import multiprocessing
import time
import os


def get_image(url):
    dt = time.time()
    response = requests.get(url)
    if response.status_code == 200:
        image = response.content
        file_name = url.rsplit('/', 1)[-1]
        file_name = os.path.join('task_9\\task_9_2', file_name)
        with open(file_name, 'wb') as f:
            f.write(image)
        print(f'Время загрузки файла {file_name}: {time.time() - dt: .3f} секунд')  
    else:
        print(f'Ошибка загрузки изображения {url}')      


def main_m(urls):
    processes = []
    for url in urls:
        p = multiprocessing.Process(target=get_image, args=(url, ))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    urls = [
        'https://img.freepik.com/free-photo/modern-sports-car-speeds-through-dark-curve-generative-ai_188544-9136.jpg',
        'https://img.freepik.com/free-photo/luxury-car-interior_146671-19729.jpg',
        'https://img.freepik.com/free-photo/a-grey-metallic-jeep-with-blue-stripe-on-it_114579-4080.jpg',
        'https://img.freepik.com/free-photo/a-green-and-black-bugatti-veyron-with-a-black-and-yellow-paint_1340-23339.jpg',
        'https://img.freepik.com/free-photo/luxury-car-speeds-by-modern-building-at-dusk-generative-ai_188544-8048.jpg'
    ]
    start_time = time.time()
    main_m(urls)
    print()
    print(f'Общее время загрузки: {time.time() - start_time: .3f} секунд')    