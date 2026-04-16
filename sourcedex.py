#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urljoin

# Definindo cores
PURPLE = "\033[35m"
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"

# Cabeçalhos mais completos para simular um navegador real
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}

def print_banner():
    banner = f"""
{PURPLE}
   ____                     
  / __/__  __ _____________ 
 _\\ \\/ _ \\/ // / __/ __/ -_)
/___/\\___/\\_,_/_/  \\__/\\__/ 
    / _ \\_____ __           
   / // / -_) \\ /           
  /____/\\__/_\\_\\            
      By: Dexter
      Version: 1.1 
      Xabaluba!!
{RESET}
"""
    print(banner)

def extract_params_from_urls(urls):
    """Extrai e exibe os parâmetros de cada URL encontrada"""
    print("\nParâmetros encontrados nas URLs:")
    found_params = False
    for url in urls:
        parsed_url = urlparse(url)
        if parsed_url.query:
            print(f"{GREEN}URL: {url}{RESET}")  # URL em verde
            params = parse_qs(parsed_url.query)
            for key, value in params.items():
                print(f"  {RED}{key}: {value}{RESET}")  # Parâmetros em vermelho
            found_params = True
    if not found_params:
        print(f"{PURPLE}Nenhuma URL com parâmetros foi encontrada.{RESET}")

def main():
    print_banner()  # Exibir o banner

    # Solicitar a URL ao usuário
    user_input = input("Insira o Alvo (ex: www.exemplo.com): ")
    
    # Adicionar o prefixo 'https://' automaticamente, se necessário
    if not user_input.startswith("http://") and not user_input.startswith("https://"):
        url = f"https://{user_input}"
    else:
        url = user_input

    try:
        # Realiza o request com cabeçalhos
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Lança uma exceção para erros HTTP

        # Usa BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Coletar todas as URLs
        urls = set()
        tags_with_urls = ["a", "script", "img", "iframe", "link", "source"]

        for tag in tags_with_urls:
            for element in soup.find_all(tag, href=True):  # Procura atributos 'href'
                full_url = urljoin(url, element["href"])
                urls.add(full_url)
            for element in soup.find_all(tag, src=True):  # Procura atributos 'src'
                full_url = urljoin(url, element["src"])
                urls.add(full_url)

        # Exibir todas as URLs encontradas
        print("\nURLs encontradas:")
        for u in urls:
            print(f"{GREEN}{u}{RESET}")  # URLs em verde

        # Extrair e exibir os parâmetros das URLs encontradas
        extract_params_from_urls(urls)

    except requests.exceptions.RequestException as e:
        print(f"{PURPLE}Erro ao acessar a URL: {e}{RESET}")

if __name__ == "__main__":
    main()
