import mlflow
import mlflow.pytorch

with mlflow.start_run():
    # Placeholder pour entraînement GAN
    mlflow.log_param("model_type", "GAN")
    mlflow.log_metric("loss", 0.0123)
    mlflow.pytorch.log_model(your_model, "model")
