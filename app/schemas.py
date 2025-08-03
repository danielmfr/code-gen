from pydantic import BaseModel
from typing import List

class TelaRequest(BaseModel):
    framework: str = "Jetpack Compose"
    linguagem: str = "Kotlin"
    repeticoes: int = 3
    modelo: str = "codellama"  # nome do modelo Ollama

class TelaResponse(BaseModel):
    codigos: List[str]
