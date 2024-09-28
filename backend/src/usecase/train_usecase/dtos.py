
from pydantic import BaseModel


class ResponseTrain(BaseModel):
    """Modelo de resposta da rota api/train com as métricas no modelo treinado
    """
    mse: float
    rmse: float
    mae: float
    mape: float
    r2: float