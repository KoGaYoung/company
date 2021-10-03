from dataclasses import asdict
from typing import Optional
import uvicorn
from fastapi import FastAPI
from application.database.conn import db
from application.common.config import conf

'''
남은 작업
- 로컬 DB연결 연결후 create_company_schema 실행
--test_app 돌아가도록 app api 추가
'''

def create_app():
    """
    앱 함수 실행

    c : 런타임 환경 DB
    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)  # dictionary로 언팩킹
    db.init_app(app, **conf_dict)  # DB연결오류 미해결

    ''' 
    추후 확장 리스트
    # from app.routes import index, auth
    # 데이터 베이스 이니셜라이즈
    # 레디스 이니셜라이즈
    # 미들웨어 정의
    # 라우터 정의
    # app.include_router(index.router)
    '''

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)