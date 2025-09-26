import os
from dotenv import load_dotenv
from google import genai
from utils.response_parser import response_parser 

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def classify_and_respond(email_text: str) -> dict:
    prompt = f""" 
    Analise o seguinte email de um cliente e siga as instruções:

    - Classifique o email em uma única categoria: 'Produtivo', 'Improdutivo' ou 'Possível Spam'.
    - Produtivo: Emails que representam uma solicitação clara e específica de suporte, produtos ou serviços que exigem uma ação ou resposta.
    - Improdutivo: Emails legítimos de clientes que não necessitam de ação imediata (ex.: agradecimentos, felicitações).
    - Possível Spam: Emails que não são solicitações de clientes reais, mensagens genéricas, perguntas de conhecimento geral, propagandas ou textos fora do contexto de suporte.

    - Depois da classificação, justifique brevemente sua decisão e sugira uma resposta automática curta e adequada apenas para emails de clientes reais. Para emails classificados como "Possível Spam", a resposta deve apenas indicar educadamente que o canal é apenas para suporte de produtos/serviços.

    Formato de Saída (use exatamente este formato, sem texto adicional):
    Categoria: <categoria_aqui>
    Justificativa: <justificativa_aqui>
    Resposta sugerida: <resposta_aqui>

    Email: 
    {email_text}
    """


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    if response.text is None:
        raise ValueError("Algo deu errado. Tente novamente mais tarde.")

    return response_parser(response.text)
