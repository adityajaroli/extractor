from fastapi import FastAPI

app = FastAPI()

@app.get("/abs_details")
async def get_abs_details():
    return {
        "conn_str": "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://abs:10000/devstoreaccount1;",
        "container": "testcontainer"
    }

@app.get("/db_details")
async def get_db_details():
    return {
        "user": "root",
        "database": "postgres",
        "password": "berlin",
        "host": "db",
        "schema": "public",
        "port": 5432
    }
