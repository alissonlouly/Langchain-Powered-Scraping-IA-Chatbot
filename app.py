import streamlit as st
from exa_py import Exa
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from agent.summarizer_agent import build_summarizer_agent
from tools.tavily_tool import tavily_search
from tools.exa_tool import get_exa_contents
from tools.itau_scraper import get_itau_link_and_preview

st.title("Chatbot Enciclopédia")

# Função para formatar ou resumir o conteúdo grande
def format_large_content(content: str, question: str, max_length: int = 1500):
    """
    Gera uma resposta concisa para a pergunta do usuário com base no conteúdo fornecido.

    Parameters:
    - content (str): O conteúdo extraído da página da Enciclopédia Itaú Cultural.
    - question (str): A pergunta original do usuário.
    - max_length (int): Comprimento máximo do conteúdo a ser considerado (para evitar textos muito longos).

    Returns:
    - str: Uma resposta gerada com base no conteúdo e na pergunta.
    """
    llm = Ollama(model="llama3:latest")
    # Se o conteúdo for muito grande, pega apenas os primeiros tokens
    if len(content) > max_length:
        content = content[:max_length] + "..."

    prompt = PromptTemplate(
        input_variables=["content", "question"],
        template="""
        **Somente** com base no seguinte conteúdo da Enciclopédia Itaú Cultural:
        {content}

        Responda à seguinte pergunta do usuário da forma mais concisa e relevante possível:
        {question}

        Resposta:
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run({"content": content, "question": question})
    return response.strip()

question = st.chat_input("Faça sua pergunta sobre cultura brasileira:")

if question:
    with st.spinner("Resumindo a pergunta..."):
        summarizer = build_summarizer_agent()
        reduced_query = summarizer.run(question).strip()

    st.markdown(f"### 🔎 Consulta resumida: {reduced_query}")

    with st.spinner("Buscando página principal na Enciclopédia Itaú Cultural..."):
        itau_result = get_itau_link_and_preview(reduced_query)
        itau_link = itau_result["link"]
        preview = itau_result.get("preview")

        if itau_link:
            st.markdown("### 📘 Links da Enciclopédia Itaú Cultural usados")
            st.write(f"**Link:** {itau_link}\n\n{preview}")

            with st.spinner("Consultando a Enciclopédia..."):
                st.markdown("### 🌐 Contexto Externo")
                
                # Consultando Exa.ai
                st.subheader("Exa.ai")
                exa_result = get_exa_contents(itau_link)

                # Formatar a resposta da Exa.ai caso o conteúdo seja grande
                formatted_exa_result = format_large_content(exa_result,question)
                st.write(formatted_exa_result)
        else:
            st.error("Nenhuma página encontrada na Enciclopédia para essa busca.")
