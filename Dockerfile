FROM python:3.8
WORKDIR temperature_converter
ADD getting_parameters.py .
ADD conversions.py .
ADD main.py .
ENTRYPOINT ["python", "./main.py"]