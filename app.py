from flask_openapi3 import OpenAPI, Info, Tag
from flask import request, jsonify
from flask_cors import CORS
from service.distancia_service import calcular_distancia
from schemas.distancia_schema import DistanciaInput, DistanciaOutput, ErrorSchema

info = Info(title="API de Cálculo de Distância", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

dist_tag = Tag(name="Distância", description="Serviço de cálculo de distância entre dois CEPs")

@app.post('/calcular', tags=[dist_tag], responses={"200": DistanciaOutput, "400": ErrorSchema, "500": ErrorSchema})
def calcular(body: DistanciaInput):
    try:
        distancia = calcular_distancia(body.origem, body.destino)
        return {"distancia_km": distancia}, 200
    except ValueError as e:
        return {"message": str(e)}, 400
    except Exception as e:
        return {"message": f"Erro interno: {str(e)}"}, 500


@app.get('/', tags=[dist_tag])
def home():
    return jsonify({"message": "API de distância disponível em /openapi"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
