import os
import requests
from langchain.tools import Tool

def tavily_search(query: dict) -> str:
    """
    Busca informações usando Tavily dado um tema ou nome, podendo filtrar por domínio específico.
    
    Espera um dicionário com:
      - 'query': string de busca
      - 'url': (opcional) URL base para filtrar por domínio (via include_domains)

    Retorna os principais resultados em texto.
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return "Erro: A chave de API Tavily não foi definida."

    query_str = query.get("query")
    if not query_str:
        return "Erro: A consulta de busca não foi fornecida."

    url_base = query.get("url")
    include_domains = [url_base] if url_base else []

    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {
        "query": query_str,
        "include_domains": include_domains,
        "max_results": 5,
        "include_raw_content": True
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return f"Erro ao buscar na Tavily: {response.text}"

    data = response.json()
    results = data.get("results", [])

    if not results:
        return "Nenhum resultado relevante encontrado na Tavily."

    # Monta uma resposta simples com até 2 resultados
    resposta = ""
    for res in results[:2]:
        resposta += f"🔗 **{res['title']}**\n{res['url']}\n\n{res['content'][:500]}...\n\n"

    return resposta.strip()

# Tool para LangChain
tavily_tool = Tool(
    name="tavily_search",
    func=tavily_search,
    description=(
        "Busca informações usando Tavily Search com base em um tema ou nome. "
        "Pode receber uma URL base para filtrar resultados. "
        "Input esperado: dicionário com 'query' (string de busca) e 'url' (opcional, para filtrar resultados por domínio)."
    )
)
