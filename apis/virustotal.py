import requests
from config import VIRUSTOTAL_API_KEY

BASE_URL = "https://www.virustotal.com/api/v3/"

HEADERS = {
    "x-apikey": VIRUSTOTAL_API_KEY
}

def enrich_ip(ip):
    url = f"{BASE_URL}ip_addresses/{ip}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição para o IP: {e}")
        return {}


def enrich_domain(domain):
    url = f"{BASE_URL}domains/{domain}"
    try:
        response = requests.get(url, headers=HEADERS)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição para o Dominio: {e}")
        return {}

def enrich_hash(file_hash):
    url = f"{BASE_URL}files/{file_hash}"
    try:
        response = requests.get(url, headers=HEADERS)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição para o hash: {e}")
        return {}
    
def enrich_url(url):
    import base64
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    full_url = f"{BASE_URL}urls/{url_id}"
    try:
        response = requests.get(full_url, headers=HEADERS)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição para a URL: {e}")
        return {}
