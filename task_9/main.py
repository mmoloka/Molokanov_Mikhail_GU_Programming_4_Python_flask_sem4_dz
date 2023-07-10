import time
import asyncio
import argparse
from pathlib import Path

from task9_1 import main_t
from task9_2 import main_m
from task9_3 import main_a


def read_urls_from_file(file_path):
    global urls
    urls = []
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            urls.append(line.strip())
        return urls    

def main():
    parser = argparse.ArgumentParser(description='Загрузкаа файлов с заданных URL')
    parser.add_argument('-f', '--file', default='urls.txt', type=str, help='Путь к файлу с URL')
    parser.add_argument('-m', '--mode', choices=['a', 't', 'm'], default='t', help='Режим выполнения (async, threading, multiprocessing)')
    args = parser.parse_args()

    if not args.file:
        print('Не указан файл с URL')
        return
    file_path = Path(args.file)
    if not file_path.exists():
        print(f'Файл не найден: {file_path}')
        return
    
    urls = read_urls_from_file(file_path)
    if args.mode == 'a':
        asyncio.run(main_a(urls))
    elif args.mode == 'm':
        main_m(urls)
    elif args.mode == 't':
        main_t(urls)
    else:
        print('Введен некорректный режим выполнения')    


if __name__ == '__main__':
    start_time = time.time()
    main()
    print()
    print(f'Общее время загрузки: {time.time() - start_time: .3f} секунд')