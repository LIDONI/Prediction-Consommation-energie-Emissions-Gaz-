import bentoml
from bentoml.io import JSON as LegacyJSON
from pydantic import BaseModel
import pandas as pd

# Chargement du modèle BentoML
model_ref = bentoml.sklearn.get("gb_multioutput_model:latest")
gb_runner = model_ref.to_runner()

# Service
energy_prediction_service = bentoml.Service("energy_prediction_service", runners=[gb_runner])

# Schéma d'entrée
class InputData(BaseModel):
    SiteEnergyUseWN: list[float]
    PropertyGFATotal: list[float]
    NumberofBuildings: list[float]
    NaturalGas: list[float]
    YearBuilt: list[int]

@energy_prediction_service.api(input=LegacyJSON(pydantic_model=InputData), output=LegacyJSON())
def predict(input_data: InputData):
    df = pd.DataFrame(input_data.dict())
    preds = gb_runner.predict.run(df)
    return {
        "TotalGHGEmissions": preds[:, 0].tolist(),
        "SiteEnergyUseWN": preds[:, 1].tolist()
    }
