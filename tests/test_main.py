
from fastapi.testclient import TestClient
from app.main import app 

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello there"}


client = TestClient(app)

def test_send():
    response = client.post("/send",json={"message": "Hello there"})
    assert response.status_code == 201
    assert response.json() == {"msg": "Hello there"}
