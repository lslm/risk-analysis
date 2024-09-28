from src.usecase.predict_usecase.dtos import PredictionRequest, PredictionResponse
import pandas as pd
import joblib

class MakePrediction():
    def __init__(self) -> None:
        try: 
            self.model, self.scaler = self.__load_models()
        except Exception as ex:
            raise Exception(f"Não foi possível carregar o Modelo: {ex.__str__()}")
        
    @classmethod
    def __load_models(self):
        """Carrega os modelos
        """
        model = joblib.load('src/factory/models/xgboost_model.pkl')
        scaler = joblib.load('src/factory/models/scaler_model.pkl')
        return model, scaler
    
    def predict(self, response: PredictionRequest) -> PredictionResponse:
        """Realiza a predição com base nas informações da request

        Args:
            response (PredictionRequest): Modelo de request com os dados para a predição

        Returns:
            PredictionResponse: Modelo de resposta
        """
        dataset = pd.DataFrame([response.dict()])
        X_data = self.scaler.transform(dataset)
        y_pred = self.model.predict(X_data)

        return PredictionResponse(result=round(float(y_pred[0]), 4))