import numpy as np
from app.util import get_logger
from app.config import ml_model_settings, MLModelSettings
from sentence_transformers import SentenceTransformer

logger = get_logger(__name__)

class MLService:
    def __init__(self, ml_model_settings: MLModelSettings):
        self._model = None
        self.ml_model_settings = ml_model_settings

    def load_model(self) -> None:
        if self._model is None:
            logger.info(f"Initializing ml model: {self.ml_model_settings}")
            self._model: SentenceTransformer = self.ml_model_settings.MODEL_TYPE(self.ml_model_settings.MODEL_LOCAL_PATH)
            logger.info("Model initialized")

    def predict(self, input: str) -> np.ndarray:
        if self._model is None:
            raise ValueError("Model not initialized")
        return self._model.encode(input)

ml_service = MLService(ml_model_settings) # global ml_service instance for model access
