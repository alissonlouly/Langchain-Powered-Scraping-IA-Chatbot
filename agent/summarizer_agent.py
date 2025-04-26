from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama


def build_summarizer_agent():
    """
    Cria e retorna um agente (LLMChain) configurado para extrair o substantivo
    principal (nome de pessoa, obra ou evento) de uma pergunta em português.

    O agente utiliza um modelo de linguagem Ollama para analisar a pergunta
    e identificar o foco central, retornando apenas esse nome de forma concisa.

    Returns:
        LLMChain: Uma instância da LLMChain configurada com um modelo Ollama
                  e um prompt específico para a tarefa de sumarização focada
                  na identificação do substantivo principal.
    """
    
    llm = Ollama(model="llama3:latest")  # ou outro modelo, se necessário

    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        Dada a pergunta abaixo, identifique o **principal nome da pessoa, obra ou evento** que é o foco central da questão. Forneça **apenas esse nome**, sem qualquer outra parte da pergunta, detalhes adicionais ou outros nomes relacionados.

        Pergunta: {question}

        Resposta direta:
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain


