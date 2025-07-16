FROM bentoml/model-server:latest

COPY . /bento
WORKDIR /bento

RUN bentoml build
RUN bentoml containerize energy_prediction_service:latest