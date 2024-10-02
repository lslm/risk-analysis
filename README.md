# Projeto de Análise de Risco de Crédito

Este repositório contém o código e os recursos para o projeto de **Análise de Risco de Crédito** (Tech Challenge 3). O objetivo deste projeto é construir um modelo de machine learning que avalie o risco de crédito e integre-o em uma aplicação funcional.

## Visão Geral do Projeto

Neste projeto, nosso objetivo foi criar um pipeline de ponta a ponta que envolvesse:

- Utilização de um dataset relevante para treinar o modelo.
- Treinamento de modelo usando técnicas de machine learning para prever o risco de crédito.
- Implantação do modelo através de uma API ou dashboard para servir previsões em um ambiente de produção.

## Estrutura de Pastas

```bash
backend/                  # Contém os arquivos para criação da API
data/raw/                 # Contém os datasets brutos utilizados para o treinamento do modelo
notebooks/
├── dataset_creation.ipynb   # Notebook para a criação e processamento do dataset
├── loan_data files         # Dataset criado para análise de risco de crédito
├── Experiments.ipynb       # Notebook contendo a análise exploratória de dados e experimentação com vários modelos
└── XGBoostExperiment.ipynb # Notebook onde o modelo XGBoost, identificado como o mais adequado, foi ajustado 
```


## Etapas Realizadas

1. Dados: https://www.kaggle.com/datasets/lorenzozoppelletto/financial-risk-for-loan-approval
2. Criação do Dataset: Preparamos o dataset para os experimentos de machine learning. As etapas incluíram limpeza de dados e divisão em conjuntos de treino e teste.
3. Análise Exploratória de Dados (EDA): Realizamos uma análise detalhada do dataset no notebook Experiments.ipynb para entender as relações entre as variáveis e avaliar potenciais modelos.
4. Seleção e Ajuste de Modelo: O algoritmo XGBoost foi selecionado como o modelo de melhor desempenho após experimentações no Experiments.ipynb. O ajuste fino dos hiperparâmetros foi feito no XGBoostExperiment.ipynb.
5. Desenvolvimento da API: O modelo foi disponibilizado via uma API localizada na pasta backend, permitindo que a aplicação faça previsões de risco de crédito em tempo real.


## Desempenho do Modelo

O modelo XGBoost apresentou os seguintes resultados:

- MSE: 5.525745966072004
- RMSE: 2.3506905296257106
- MAE: 1.6182307867262096
- MAPE: 0.03398557930384665
- R2 Score: 0.9070434276594164

Mais detalhes podem ser encontrados no notebook XGBoostExperiment.ipynb.

