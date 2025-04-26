import os
from exa_py import Exa
from langchain.tools import Tool
from langchain.prompts import PromptTemplate

def get_exa_contents(urls: list) -> str:
    """
    Função para buscar conteúdos de uma lista de URLs utilizando a Exa API.
    Retorna o conteúdo das URLs.

    Parameters:
    - urls (list): Lista de URLs para buscar conteúdo.

    Returns:
    - str: Conteúdo das URLs solicitadas.
    """
    # Obtenha a chave da variável de ambiente
    exa_key = os.getenv('EXA_API_KEY')

    # Verifique se a chave de API foi carregada corretamente
    if exa_key is None:
        return "Erro: A chave de API Exa não foi definida."

    try:
        # Inicialize o cliente Exa com a chave de API
        exa = Exa(api_key=exa_key)

        # Obter conteúdos das URLs passadas
        results = exa.get_contents(urls)

        # Retornar os resultados em formato de string
        return str(results)

    except Exception as e:
        # Em caso de erro, retornar mensagem de erro
        return f"Erro ao obter conteúdos: {str(e)}"

# Tool pronta para ser usada no LangChain
get_exa_tool = Tool(
    name="get_exa_contents",
    func=get_exa_contents,
    description="Busca conteúdos de uma lista de URLs usando a Exa API. Use quando quiser obter o texto completo de uma ou mais páginas da web. Input esperado: lista de URLs."
)
