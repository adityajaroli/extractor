from io import BytesIO

import pandas as pd
from azure.storage.blob import BlobClient
from src.config_service import ConfigService
from pg_bulk_loader import PgConnectionDetail, batch_insert_to_postgres


class ExtractionService:

    async def execute(self, order_date):
        data = await self.__extract(order_date)
        await self.__transform(data)
        await self.__load(data)
        return data.shape[0]

    @staticmethod
    async def __extract(order_date):
        abs_info: dict = ConfigService.get_abs_config()

        blob = BlobClient.from_connection_string(
            conn_str=abs_info['conn_str'], container_name=abs_info['container'], blob_name=f"{order_date}/orders.parquet"
        )

        downloaded_blob = blob.download_blob()
        file_in_bytes = BytesIO()
        downloaded_blob.readinto(file_in_bytes)
        blob_df = pd.read_parquet(file_in_bytes, engine="pyarrow")
        blob.close()
        return blob_df

    @staticmethod
    async def __transform(data: pd.DataFrame):
        data.rename(columns={"order_id": "id"}, inplace=True)

    @staticmethod
    async def __load(data: pd.DataFrame):
        db_info: dict = ConfigService.get_db_details()
        pg_conn_details = PgConnectionDetail(**db_info)

        await batch_insert_to_postgres(
            pg_conn_details=pg_conn_details,
            table_name="order_data",
            batch_size=1000,
            input_data=data
        )
