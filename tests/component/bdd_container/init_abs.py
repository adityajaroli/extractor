from azure.storage.blob import BlobServiceClient


class InitABS:

    __ACCOUNT_URL = "http://abs:10000/devstoreaccount1"
    __ACCOUNT_NAME = "devstoreaccount1"
    __ACCOUNT_KEY = "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw=="

    def __init__(self):
        creds = {
          "account_name": self.__ACCOUNT_NAME,
          "account_key": self.__ACCOUNT_KEY
        }
        self.blob_service_client = BlobServiceClient(account_url=self.__ACCOUNT_URL, credential=creds)

    def create_container(self, container_name="testcontainer"):
        try:
            container_client = self.blob_service_client.get_container_client(container_name)
            container_client.create_container()
            return container_client
        except Exception as e:
            print(e)

    def upload_parquet(self, container_client, parquet_read_loc, parquet_write_loc):
        try:
            with open(parquet_read_loc, "rb") as data:
                container_client.upload_blob(data=data, name=parquet_write_loc)
        except Exception as e:
            print(e)


setup_abs = InitABS()
container_client = setup_abs.create_container()
setup_abs.upload_parquet(
    container_client=container_client,
    parquet_read_loc="./component/bdd_container/data/orders.parquet",
    parquet_write_loc="2021-01-01/orders.parquet"
)
