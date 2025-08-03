# 📱 CodeGen (Code Generator) - Ollama

Projeto FastAPI para gerar **códigos de telas mobile** usando modelos de linguagem (LLMs) locais via **[Ollama](https://ollama.com/)**. A API permite descrever uma tela e obter múltiplas versões de código gerado automaticamente — que são salvas como arquivos `.md`.

---

## 🚀 Tecnologias usadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Ollama](https://ollama.com/) (modelos LLM locais como `codellama`, `llama3`, `mistral`, etc.)
- Python 3.9+
- httpx

---

## 📂 Estrutura do projeto

```bash
mobile-codegen/
├── app/
│   ├── main.py       # API FastAPI
│   ├── schemas.py    # Modelos Pydantic (request/response)
│   ├── generator.py  # Comunicação com Ollama
├── outputs/          # Códigos gerados em .md
├── requirements.txt  # Dependências
├── .env              # (opcional) configurações
└── README.md         # Este arquivo
```

---

## ⚙️ Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/mobile-codegen.git
cd mobile-codegen
```

2. **Crie e ative um ambiente virtual (recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Certifique-se de que o Ollama esteja instalado e rodando:**

```bash
ollama run codellama
```

> ⚠️ O modelo deve estar disponível localmente. Substitua por outro se preferir: ``llama3``, ``mistral``, etc.

---

## ▶️ Execução

Rode o servidor FastAPI com:

```bash
uvicorn app.main:app --reload
```

Acesse a interface Swagger:

```bash
http://localhost:8000/docs
```

---

## 📥 Exemplo de requisição

```json
POST /gerar-tela
Content-Type: application/json

{
  "descricao": "Tela de login com e-mail e senha",
  "framework": "Flutter",
  "linguagem": "Dart",
  "modelo": "codellama",
  "repeticoes": 2
}
```

---

## 📤 O que a API retorna

```json
{
  "codigos": [
    "...código 1...",
    "...código 2..."
  ]
}
```

Além disso, os códigos são salvos automaticamente em arquivos `.md` na pasta `outputs/`, com nomes baseados em data e hash da descrição.

Exemplo:

```bash
outputs/
├── 20250803-153210_ab12cd_1.md
├── 20250803-153210_ab12cd_2.md
```

---

## 📌 Modelos suportados

Você pode usar qualquer modelo suportado pelo Ollama, incluindo:
- codellama
- llama3
- mistral
- phi3
- gemma
- e outros...

Verifique os modelos instalados com:

```bash
ollama list
```

---

## ✅ To-do (ideias futuras)
✅ Escolha do modelo LLM por requisição

✅ Suporte a múltiplas repetições

✅ Geração de arquivos .md com cada variação

⏳ Integração com frontend de visualização

⏳ Suporte a geração por lote de telas

---

## 🧠 Requisitos
- Python 3.9+
- Ollama instalado e funcional
- Modelos carregados localmente (ollama run <modelo>)

---

## 📃 Licença
Este projeto está sob a licença MIT.