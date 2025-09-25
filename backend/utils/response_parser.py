def response_parser(output: str) -> dict:
    lines = output.splitlines()
    category, justificativa, resposta = "", "", ""

    for line in lines:
        line = line.strip()
        if line.startswith("Categoria:"):
            category = line.replace("Categoria:", "").strip()
        elif line.startswith("Justificativa:"):
            justificativa = line.replace("Justificativa:", "").strip()
        elif line.startswith("Resposta sugerida:"):
            resposta = line.replace("Resposta sugerida:", "").strip()

    return {
        "categoria": category,
        "justificativa": justificativa,
        "resposta_sugerida": resposta
    }
