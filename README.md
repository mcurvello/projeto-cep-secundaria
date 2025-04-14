# API Secundária - Cálculo de Distância

## ✨ Descrição
API para cálculo da distância entre dois CEPs, usada pela API principal.
Usa fórmula de Haversine para estimar a distância geográfica.

## ⚙️ Instalação

### ✅ Requisitos
- Python 3.9 ou superior
- Docker e Docker Compose (opcional)

### 💻 Rodar localmente (sem Docker)

```bash
cd mvp1-backend/api-distancia
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install -r requirements.txt
flask run --host 0.0.0.0 --port 5002
```

### 🐳 Rodar com Docker

```bash
docker compose up --build
```

## 💡 Uso

- Swagger: [http://localhost:5002/openapi](http://localhost:5002/openapi)

### Requisição `curl`

```bash
curl -X POST http://localhost:5002/calcular \
  -H "Content-Type: application/json" \
  -d '{"origem": "01153000", "destino": "05407002"}'
```

## 📦 Funcionalidades
- Recebe dois CEPs e retorna a distância entre eles
- Documentação interativa com OpenAPI

## 🚀 Contribuição
Faça um fork, crie uma branch e envie um Pull Request.

---

> Desenvolvido por Marcio Curvello
