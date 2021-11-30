# Temperature converter
This temperature converter was written on Python, and it can help you to convert temperature in any scales below.

## Temperature scales list
This converter support conversions to such scales as Celsius (C), Fahrenheit (F), Kelvin (K), Rankin (R), Delisle (De) and Newton (N).

## How to run 
**Run the project:**
1) Clone repository
2) Run service
3) Start working

**Run with Docker:**
1) Clone repository
2) Build docker container with command `docker build -t temperature-converter`
3) Run container with command `docker run -it temperature-converter`
4) Start working

## How to work in the service
You would write three parameters:
1) temperature value
2) its temperature scale
3) which temperature scale you want to convert the temperature to

If you want to shut down in the service, you would write `exit`. 