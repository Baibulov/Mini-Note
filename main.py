from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4, UUID

app = FastAPI(
    title="Mini-Note API",
    description="API-сервис для управления заметками с полным CRUD-функционалом",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory хранилище заметок (в реальном проекте здесь была бы база данных)
notes_db: dict[UUID, dict] = {}


# Pydantic модели
class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Заголовок заметки")
    content: str = Field(..., min_length=1, description="Содержимое заметки")
    tags: Optional[List[str]] = Field(default=[], description="Теги заметки")


class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Заголовок заметки")
    content: Optional[str] = Field(None, min_length=1, description="Содержимое заметки")
    tags: Optional[List[str]] = Field(default=None, description="Теги заметки")


class NoteResponse(BaseModel):
    id: UUID
    title: str
    content: str
    tags: List[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# CRUD операции

@app.post("/notes", response_model=NoteResponse, status_code=201)
async def create_note(note: NoteCreate):
    """Создать новую заметку"""
    note_id = uuid4()
    now = datetime.now()
    
    new_note = {
        "id": note_id,
        "title": note.title,
        "content": note.content,
        "tags": note.tags or [],
        "created_at": now,
        "updated_at": now
    }
    
    notes_db[note_id] = new_note
    return NoteResponse(**new_note)


@app.get("/notes", response_model=List[NoteResponse])
async def get_all_notes():
    """Получить все заметки"""
    return [NoteResponse(**note) for note in notes_db.values()]


@app.get("/notes/{note_id}", response_model=NoteResponse)
async def get_note(note_id: UUID):
    """Получить заметку по ID"""
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    
    return NoteResponse(**notes_db[note_id])


@app.put("/notes/{note_id}", response_model=NoteResponse)
async def update_note(note_id: UUID, note_update: NoteUpdate):
    """Обновить заметку"""
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    
    existing_note = notes_db[note_id]
    
    # Обновляем только переданные поля
    if note_update.title is not None:
        existing_note["title"] = note_update.title
    if note_update.content is not None:
        existing_note["content"] = note_update.content
    if note_update.tags is not None:
        existing_note["tags"] = note_update.tags
    
    existing_note["updated_at"] = datetime.now()
    
    return NoteResponse(**existing_note)


@app.delete("/notes/{note_id}", status_code=204)
async def delete_note(note_id: UUID):
    """Удалить заметку"""
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    
    del notes_db[note_id]
    return None


@app.get("/", tags=["Root"])
async def root():
    """Корневой endpoint"""
    return {
        "message": "Mini-Note API",
        "version": "1.0.0",
        "docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

