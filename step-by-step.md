# Python 3 + FastAPI

## Initialize project
```ch
python3 -m venv vend
```

## activate
```ch
source venv/bin/activate
```

## install fastapi dependency
```ch
pip install fastapi
```

## install uvicorn dependency
```ch
pip install "uvicorn[standard]" gunicorn
```
## create the dependency file for installation
```ch
pip freeze > requirements.txt
```
* include in it the dependencies used in the project
* run the script: pip install -r requirements.txt (when you want to install all dependencies)