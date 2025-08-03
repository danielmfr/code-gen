from fastapi import FastAPI
from app.schemas import TelaRequest, TelaResponse
from app.generator import gerar_codigo, descricao
import os
from datetime import datetime
import hashlib

app = FastAPI()

os.makedirs("outputs", exist_ok=True)

@app.post("/gerar-tela", response_model=TelaResponse)
def gerar_tela(req: TelaRequest):
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    descricao_hash = hashlib.md5(descricao.encode()).hexdigest()[:6]

    codigos = []
    for i in range(req.repeticoes):
        codigo = gerar_codigo(req.framework, req.linguagem, req.modelo)
        codigos.append(codigo)

        filename = f"outputs/{timestamp}_{descricao_hash}_{i+1}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Tela gerada ({i+1}/{req.repeticoes})\n\n")
            f.write(f"**Descrição:** {descricao}\n\n")
            f.write(codigo)

    return TelaResponse(codigos=codigos)
