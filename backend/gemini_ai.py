import os
from dotenv import load_dotenv
from google import genai
from utils.response_parser import response_parser  # import do parser

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def classify_and_respond(email_text: str) -> dict:
    prompt = f""" 
    Analise o seguinte email de um cliente e siga as instruções:

    - A sua tarefa é classificar o email como 'Produtivo' ou 'Improdutivo'.
    - Um email só deve ser classificado como 'Produtivo' se ele representar uma solicitação clara e específica de um cliente que precisa de uma ação ou resposta de suporte.
    - Classifique o email como 'Improdutivo' se ele for uma mensagem que não necessita de uma ação imediata.
    - Classifique o email como 'Possível Spam' caso ele for uma mensagem genérica ou um texto que não seja um email real de um cliente.
    - Depois da classificação, justifique brevemente sua decisão e sugira uma resposta automática curta e adequada.

    Formato de Saída (use este formato exatamente como está, sem texto adicional):
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
