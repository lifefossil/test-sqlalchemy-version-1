from pydantic import BaseSettings

from src.core.constants import PROJECT_ROOT_DIR


class MysqlConfig(BaseSettings):
    host: str = 'localhost'
    port: int = 3306
    username: str = 'root'
    password: str = ''
    database: str = ''
    timezone: str = 'Asia/Shanghai'

    class Config:
        # 设置.env中配置参数的前置(如.env中是MYSQL_USERNAME
        # 添加env_prefix后会去掉MYSQL_后和上面username对应.
        env_prefix = 'mysql_'
        env_file = PROJECT_ROOT_DIR / '.env'
        env_file_encoding = 'utf-8'


mysql_config: MysqlConfig = MysqlConfig()

if __name__ == '__main__':
    config = MysqlConfig()
    print(config.dict())
    print(PROJECT_ROOT_DIR / '.env')
