import logging
from src.usecase.predict_usecase import PredictionRequest, PredictModel
from src.usecase.train_usecase import ResponseTrain, TrainModel
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from src.api.core.dtos import ErrorModel
from fastapi import APIRouter
from http import HTTPStatus

# Configuração básica do logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]  # Você pode adicionar um arquivo, se necessário
)

logger = logging.getLogger(__name__)

router = APIRouter(tags=['Financial Risk'])

@router.post("/predict")
async def make_prediction(request: PredictionRequest):
    """Realiza a predição do modelo com os dados informados

    Args:
        request (PredictionRequest): Request com os dados para a fazer a predição

    """
    try:
        logger.info(f"Requisição recebida: {request}")
        predict_model = PredictModel(request=request)
        res = predict_model.predict()
        return JSONResponse(content=jsonable_encoder(res), status_code=HTTPStatus.OK)
    except Exception as ex:
        ex.with_traceback
        error = ErrorModel.from_exception(ex)
        return JSONResponse(content=jsonable_encoder(error), status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

@router.post("/train")
async def make_model():
    """Realiza o treinamento do modelo
    """
    try:
        res = TrainModel.train()
        return JSONResponse(content=jsonable_encoder(res), status_code=HTTPStatus.OK)
    except Exception as ex:
        ex.with_traceback
        error = ErrorModel.from_exception(ex)
        return JSONResponse(content=jsonable_encoder(error), status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

@router.get("/health")
async def health_check():
    """Verifica o Status da Aplicação
    """
    return {"status": "API is up and running"}
