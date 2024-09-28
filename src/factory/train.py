from sklearn.metrics import mean_absolute_percentage_error
from src.usecase.train_usecase.dtos import ResponseTrain
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
import pandas as pd
import numpy as np
import joblib

class MakeModel():

    def __init__(self) -> None:
        try:
            self.dataset = self.__get_dataset()
        except Exception as ex:
            raise Exception(f"Não foi possível carregar os dados de treinamento: {ex.__annotations__}")

    @classmethod
    def __get_dataset(self):
        return pd.read_csv("src/data/loan_data_test.csv")
    
    def __trata_dataset(self, df: pd.DataFrame) -> pd.DataFrame:
        """Trata o dataset para a criação do modelo

        Args:
            df (pd.DataFrame): Dataset com os dados para o treinamento

        Returns:
            pd.DataFrame: Dataset com os dados tratados
        """
        df = df.drop(columns=['ApplicationDate', 'LoanPurpose', 'MaritalStatus', 'LoanApproved'])
        df = df.dropna()
        df['EducationLevel'] = df['EducationLevel'].astype('category').cat.codes
        df['EmploymentStatus'] = df['EmploymentStatus'].astype('category').cat.codes
        df['HomeOwnershipStatus'] = df['HomeOwnershipStatus'].astype('category').cat.codes
        return df

    def make_model(self) -> ResponseTrain:
        """Cria o modelo que será usado para as predições
        """
        df_tratado = self.__trata_dataset(self.dataset)

        X = df_tratado.drop(columns=['RiskScore'])
        y = df_tratado['RiskScore']

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        joblib.dump(scaler, 'src/factory/models/scaler_model.pkl')

        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

        xgboost_model = XGBRegressor()
        xgboost_model.fit(X_train, y_train)
        y_pred = xgboost_model.predict(X_test)
        
        joblib.dump(xgboost_model, 'src/factory/models/xgboost_model.pkl')

        mse = mean_squared_error(y_test, y_pred, squared=True)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        mape = mean_absolute_percentage_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        return ResponseTrain(mse=mse, rmse=rmse, mae=mae, mape=mape, r2=r2)
