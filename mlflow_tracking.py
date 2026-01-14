#MLflow model tracking - Logging parameters, metrics, and output models during runs for experiment tracking.

import mlflow  

with mlflow.start_run():
    mlflow.log_metric("auc", 0.91)  
    mlflow.log_params(best_params)

    mlflow.xgboost.log_model(model, "xgb_model")