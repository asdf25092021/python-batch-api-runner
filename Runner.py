import concurrent.futures
import requests
import time

# Список сайтов для проверки
ENDPOINTS = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/photos",
    "https://jsonplaceholder.typicode.com/todos"
]

def check_url(url):
    try:
        # Устанавливаем таймаут 5 секунд
        response = requests.get(url, timeout=5)
        return f"{url} | Status: {response.status_code} | OK"
    except requests.exceptions.RequestException as e:
        return f"{url} | Error: {e}"

def run_batch():
    print(f"Starting batch process for {len(ENDPOINTS)} endpoints...")
    start = time.time()

    # Запускаем параллельно (Multithreading)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(check_url, ENDPOINTS))

    for res in results:
        print(res)

    end = time.time()
    print(f"Finished in {round(end - start, 2)} seconds.")

if __name__ == "__main__":
    run_batch()
