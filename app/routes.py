from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def healthcheck():
    return {"status": "healthy"}

'''main.py = CEO

routes.py = Department that handles endpoints

We separated them to keep the system scalable and professional.
'''