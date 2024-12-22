import json

import boto3
from botocore.exceptions import ClientError
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Callable
from sentence_transformers import SentenceTransformer

# class AWSSecrets(BaseSettings):
#     aws_secret_name: str = Field(env="AWS_SECRET_NAME")
#     aws_region: str = Field("us-west-2", env="AWS_REGION")


class PostgresSettings(BaseSettings):
    postgres_user: str = Field(env="POSTGRES_USER")
    postgres_password: str = Field(env="POSTGRES_PASSWORD")
    postgres_host: str = Field(env="POSTGRES_HOST")
    postgres_port: str = Field(env="POSTGRES_PORT")
    postgres_database: str = Field(env="POSTGRES_DB")

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_database}"


# class MLModelSettings(BaseSettings):
#     MODEL_LOCAL_PATH: str = Field(..., env="MODEL_LOCAL_PATH")
#     MODEL_TYPE: Callable = SentenceTransformer


# def get_secrets_dict(aws_config: AWSSecrets) -> dict:
#     session = boto3.session.Session()
#     client = session.client(
#         service_name="secretsmanager", region_name=aws_config.aws_region
#     )
#     try:
#         secret_value_response = client.get_secret_value(
#             SecretId=aws_config.aws_secret_name
#         )
#         return json.loads(secret_value_response["SecretString"])
#     except ClientError as e:
#         raise e


# aws_config = AWSSecrets()

# secrets_dict = get_secrets_dict(aws_config)

postgres_settings = PostgresSettings(
    postgres_user=secrets_dict["postgres_user"],
    postgres_password=secrets_dict["postgres_password"],
    postgres_host=secrets_dict["postgres_host"],
    port=secrets_dict["PORT"],
    database=secrets_dict["DATABASE"],
)

ml_model_settings = MLModelSettings()