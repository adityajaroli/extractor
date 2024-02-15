from fastapi import FastAPI
from src.extraction_service import ExtractionService

app = FastAPI()


@app.get("/health")
async def get_health():
    return True


@app.post("/extract")
async def extract_data(order_date: str):
    extraction_service = ExtractionService()
    total_records = await extraction_service.execute(order_date)
    return {
        'extract_date': order_date,
        'total_records': total_records,
        'status': 'successful'
    }

