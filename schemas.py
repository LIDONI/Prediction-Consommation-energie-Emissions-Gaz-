from pydantic import BaseModel, conint, confloat

class InputData(BaseModel):
    SiteEnergyUseWN: conint(ge=0)
    PropertyGFATotal: conint(ge=1)
    NumberofBuildings: conint(ge=1)
    NaturalGas: confloat(ge=0)
    YearBuilt: conint(ge=1800, le=2025)
