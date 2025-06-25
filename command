uvicorn app.main:app --reload
uvicorn app.main:app --host 0.0.0.0 --port 8000

docker build -t hello_agent:v1.0.0 .
docker run -d -p 8000:8000 hello_agent:v1.0.0


lsof -i :8000

kill -9 
