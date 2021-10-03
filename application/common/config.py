'''
 config.py는 환경별 변수
 운영 서버, 개발 서버, QA를 수행하는 스테이징 서버, 로컬 서버 등.
 그때 그때 다른 방법으로 설정파일을 넣는 것을 config.py 에 작업

 todo : AWS Elastic Beanstalk 로 함께 배포할때 사용 (확인)
'''

from dataclasses import dataclass, asdict
from os import path, environ


base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir  # '/Users/kogayoung/company'

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True
    # DB_URLL: str = 'postgresql://127.0.0.1:5432/postgres'
    user = environ.get('DB_USER', 'user')
    password = environ.get('DB_PASSWORD', 'password')
    address = environ.get('DB_ADDR', '0.0.0.0')
    port = environ.get('DB_PORT', '')
    name = environ.get('DB_NAME', '')

    DB_URL: str = 'postgresql://{username}:{password}@{host}:{port}/{db_name}'.format(
        username='postgres', password='postgres', host='127.0.0.1', port='5432', db_name='company'
    )

@dataclass
class LocalConfig(Config):  # Config 상속받음
    PROJ_RELOAD: bool = True


@dataclass
class ProdConfig(Config):  # Config 상속받음
    PROJ_RELOAD: bool = False


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    # "API_ENV"가 없으니 당연히 LocalConfig 리턴
    return config.get(environ.get("API_ENV", "local"))