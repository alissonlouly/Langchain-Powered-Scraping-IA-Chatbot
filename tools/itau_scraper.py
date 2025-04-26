import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def get_itau_link_and_preview(query: str) -> dict:
    """
    Busca na Enciclopédia Itaú Cultural por uma determinada consulta e retorna o link
    da primeira entrada encontrada e uma breve descrição (preview).

    Args:
        query (str): O termo de busca a ser pesquisado na Enciclopédia Itaú Cultural.

    Returns:
        dict: Um dicionário contendo as seguintes chaves:
            - 'link' (str ou None): O link completo para a página principal da primeira
              entrada encontrada na Enciclopédia. Retorna None se nenhum link for
              encontrado ou se ocorrer algum erro.
            - 'preview' (str): Uma breve descrição da entrada encontrada, geralmente
              extraída do subtítulo da página. Se nenhum subtítulo estiver disponível
              ou ocorrer algum erro, retorna uma mensagem informativa.
    """
    base_url = "https://enciclopedia.itaucultural.org.br"
    search_url = f"{base_url}/busca?q={quote_plus(query)}"

    print(f"[DEBUG] URL usada: {search_url}")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(search_url, headers=headers)

        print(f"[DEBUG] Status Code: {response.status_code}")

        if response.status_code != 200:
            return {"link": None, "preview": f"Erro ao acessar a Enciclopédia (status {response.status_code})."}

        soup = BeautifulSoup(response.text, "html.parser")
        article = soup.find("article", class_="row no-gutters")

        if not article:
            return {"link": None, "preview": "Nenhuma entrada encontrada."}

        a_tag = article.find("a", href=True)
        subtitle_div = article.find("div", class_="subtitle")

        if a_tag:
            href = a_tag["href"]
            full_link = f"{base_url}{href}"
            preview_text = subtitle_div.text.strip() if subtitle_div else "Nenhum subtítulo disponível."
            return {"link": full_link, "preview": preview_text}

        return {"link": None, "preview": "Não foi possível encontrar o link principal."}

    except Exception as e:
        return {"link": None, "preview": f"Erro na requisição: {str(e)}"}