from fastapi import Depends, FastAPI
from common.convertDB import to_list
from fastapi.middleware.cors import CORSMiddleware
from init import Base, engine, SessionLocal
import uvicorn

Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(testcase.router)

# app.mount("/static", StaticFiles(directory="client/static"), name="static")




if __name__ == '__main__':
    uvicorn.run('run:app', host= '0.0.0.0', port=8088, workers=3, reload=True)
