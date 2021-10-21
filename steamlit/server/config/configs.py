from common.bcolor import BCOLOR
from common.minio import MinioModel
from database.redis import redis_connect, _connect
from fastapi_redis_cache.enums import RedisStatus
import os
import yaml


class configModel():
    def __init__(self):
        self.config_source_envirment = self.load_file_config()


    def load_file_config(self):
        #auto load config from file config
        with open("config/configEnviroment.yml") as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            config = yaml.load(file, Loader=yaml.FullLoader)
            print(config)
            self.redis_url = config['redis_url']
            self.database_url = config['postgres_url']
            return config


    def load_minio(self):
        Host = self.config_source_envirment['minio_address']
        access_key = self.config_source_envirment['access_key']
        secret_key = self.config_source_envirment['minioPass']
        secure = self.config_source_envirment['minioSecure']
        self.minio = MinioModel(Host, access_key, secret_key, secure)
        return self.minio


    def check_server_local(self):
        if os.getcwd() == self.config_source_envirment['local']:
            return 1
        elif os.getcwd() == self.config_source_envirment['server']:
            return 2
        else:
            return 3


    def validation_file_path(self):
        try:
            return self.config_source_enviroment["validation"]
        except:
            raise Exception("Don't find config path.")


    def load_redis(self):
        redis_status, redis_client = _connect(self.redis_url)
        if redis_status == RedisStatus.NONE:
            redis_client =  redis_connect(self.redis_url)
        elif redis_status != RedisStatus.NONE and redis_status != RedisStatus.CONNECTED:
            BCOLOR.warning("")
        return redis_client


config_model = configModel()
Host = config_model.config_source_envirment['minio_address']
access_key = config_model.config_source_envirment['access_key']
secret_key = config_model.config_source_envirment['minioPass']
secure = config_model.config_source_envirment['minioSecure']
minio = MinioModel(Host, access_key, secret_key, secure)
redis = config_model.load_redis()
