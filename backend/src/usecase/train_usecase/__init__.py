from src.usecase.train_usecase.dtos import ResponseTrain
from src.factory.train import MakeModel

class TrainModel():

    def train() -> ResponseTrain:
        """Realiza o treinamento do modelo

        Returns:
            ResponseTrain: Métricas do modelo treinado
        """
        ress = MakeModel().make_model()
        return ress 