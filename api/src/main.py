from fastapi import FastAPI, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from src.config import engine, SessionLocal
from src.models import Base, Item

app = FastAPI()

# Create tables
@app.on_event("startup")
def startup():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print("Database not ready yet:", e)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: dict):
    db = SessionLocal()
    try:
        new_item = Item(
            name=item["name"],
            description=item.get("description")
        )
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        db.close()

@app.get("/items")
def get_items():
    db = SessionLocal()
    try:
        items = db.query(Item).all()
        return items
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        db.close()
