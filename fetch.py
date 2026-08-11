import requests, time

def fetch_page(url, retries=3, delay=1):
    for i in range(retries):
        try:
            r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                return r.text
        except Exception:
            time.sleep(delay * (i + 1))
    return None
