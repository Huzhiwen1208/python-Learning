# 文件：backend/main.py
# 这是课堂演示代码。真正启动服务时，请把它保存到 main.py，
# 然后在 Terminal 中运行：fastapi dev main.py

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(
    title="学习任务 API",
    description="Python 3.14 + FastAPI 课堂演示",
    version="1.0.0",
)


# React 和 FastAPI 端口不同，浏览器会把它们视为不同 Origin。
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["Content-Type"],
)


# 前端创建任务时提交的数据格式
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=50)


# 后端返回给前端的数据格式
class Task(TaskCreate):
    id: int


# 课堂演示暂时用列表保存数据；后端重启后会恢复初始值。
tasks: list[dict] = [
    {"id": 1, "title": "学习 Python 基础"},
    {"id": 2, "title": "认识 FastAPI 接口"},
]

next_id = 3


@app.get("/")
def home():
    return {"message": "学习任务 API 正在运行"}


@app.get("/api/tasks", response_model=list[Task])
def get_tasks():
    # 返回全部任务
    return tasks


@app.post(
    "/api/tasks",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task: TaskCreate):
    # 创建一个新任务
    global next_id

    clean_title = task.title.strip()
    if not clean_title:
        raise HTTPException(
            status_code=422,
            detail="任务内容不能为空",
        )

    new_task = {
        "id": next_id,
        "title": clean_title,
    }
    tasks.append(new_task)
    next_id += 1
    return new_task


@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    # 根据 ID 删除一个任务
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return Response(
                status_code=status.HTTP_204_NO_CONTENT
            )

    raise HTTPException(
        status_code=404,
        detail="没有找到这个任务",
    )
