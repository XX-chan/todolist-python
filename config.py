import os
from dotenv import load_dotenv

# 项目根目录（config.py所在的目录）
BASE_DIR=os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config:
    # 从环境中获得密钥or开发中使用的密钥。
    SECRET_KEY=os.environ.get("SECRET_KEY") 

    DEBUG=False

    #配置SQL数据库
    USER_DB_PATH=os.path.join(BASE_DIR,"data","users.db")
    TODOS_DB_PATH=os.path.join(BASE_DIR,"data","todos.db")


class DevelopmentConfig(Config):
    # 开发环境,继承Config默认配置。

    DEBUG=True


class ProductionConfig(Config):
    # 生产环境,继承Config默认配置。

    DEBUG=False

    # 生产环境如果没有SECRET_KEY，启动时报错，不使用默认密钥。
    SECRET_KEY=os.environ.get("SECRET_KEY")


# 用环境变量名配置类
config_by_name={
    "develope":DevelopmentConfig,
    "production":ProductionConfig,
    "defalut":DevelopmentConfig
}

# 根据FLASK_CONFIG返回配置类，不是实例。
def get_config():

    #从环境中获取FALSK_CONFIG的配置类名称，如果为None，返回默认值"default"
    name=os.environ.get("FLASK_CONFIG","default")

    return config_by_name.get(name,DevelopmentConfig)

