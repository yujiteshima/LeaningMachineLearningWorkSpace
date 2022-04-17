FROM continuumio/anaconda3

RUN python -m pip install -U flake8 autopep8 ipykernel
