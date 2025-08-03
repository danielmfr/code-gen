import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"
descricao = """
Tela de login simples com campos para e-mail e senha, botão de login, e validação básica dos campos.
A tela deve ser responsiva e amigável para dispositivos mobile.
"""

def gerar_codigo(framework: str, linguagem: str, modelo: str) -> str:
    prompt = f"""
    Quero que você atue como um desenvolvedor mobile. 
    Gere o código completo, com todos os imports e funções necessárias, para a seguinte interface de usuário:

    {descricao}

    Use o framework {framework}, escreva o código em {linguagem}. 
    O código deve estar pronto para ser usado como componente ou tela.

    Inclua comentários explicando o que cada parte faz.
    """

    try:
        response = httpx.post(
            OLLAMA_URL,
            json={
                "model": modelo,
                "prompt": prompt,
                "stream": False
            },
            timeout=60.0  # AUMENTADO de padrão (~5s) para 60s
        )
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()

    except httpx.RequestError as e:
        raise Exception(f"Erro ao se conectar ao Ollama: {e}")
    except httpx.HTTPStatusError as e:
        raise Exception(f"Ollama retornou erro HTTP: {e.response.text}")
