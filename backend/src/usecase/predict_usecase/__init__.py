from src.usecase.predict_usecase.dtos import PredictionRequest, PredictionResponse
from src.factory.preditc import MakePrediction


class PredictModel():
    """Classe responsável por realizar a predição
    """
    def __init__(self, request: PredictionRequest) -> None:
        self.request = request
    
    def predict(self) -> PredictionResponse:
        """Realiza a predição

        Returns:
            PredictionResponse: Resultado da Predição
        """
        ress = MakePrediction().predict(self.request)
        return ress