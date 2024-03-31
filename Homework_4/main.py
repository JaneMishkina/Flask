# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.
#

import argparse
import requests
import os
import time
from urllib.parse import urlparse

import concurrent.futures
import asyncio
import aiohttp
import multiprocessing


def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.basename(urlparse(url).path)
            start_time = time.time()
            with open(filename, 'wb') as file:
                file.write(response.content)
            end_time = time.time()
            print(f"Скачан {url} как {filename} за {end_time - start_time:.4f} сек")

        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

async def async_download_image(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                filename = os.path.basename(urlparse(url).path)
                start_time = time.time()
                with open(filename, 'wb') as file:
                    file.write(await response.read())
                end_time = time.time()
                print(f"Скачан {url} как {filename} за {end_time - start_time:.4f} сек")
            else:
                print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def download_images_threaded(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)

async def download_images_async(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [async_download_image(session, url) for url in urls]
        await asyncio.gather(*tasks)

def download_images_multiprocessing(urls):
    with multiprocessing.Pool() as pool:
        pool.map(download_image, urls)

if __name__ == "__main__":
    # urls = [
    #     "https://i.pinimg.com/736x/98/be/79/98be799b20fc500e7c2b31acc354a779.jpg",
    #     "https://galerey-room.ru/images/0_3c7f7_81e3c5ed_orig.png",
    #     "https://i.yapx.cc/MvQ5k.gif"]  # добавьте здесь свои URL-адреса

    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="*", help="List of URL addresses to download images from")
    args = parser.parse_args()
    urls = args.urls

    if not urls:
        print("Добавьте хотя бы одну ссылку")
    start_time = time.time()

    # Многопоточный подход
    download_images_threaded(urls)

    # Асинхронный подход
    asyncio.run(download_images_async(urls))

    # Многопроцессорный подход
    download_images_multiprocessing(urls)

    print(f"Общее время скачивания: {time.time() - start_time} сек")

