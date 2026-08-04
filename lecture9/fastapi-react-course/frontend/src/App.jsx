import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000/api/tasks";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    loadTasks();
  }, []);

  async function loadTasks() {
    try {
      setError("");
      const response = await fetch(API_URL);

      if (!response.ok) {
        throw new Error("获取任务失败");
      }

      const data = await response.json();
      setTasks(data);
    } catch (err) {
      setError("无法连接后端，请检查 FastAPI 是否已启动。");
    } finally {
      setLoading(false);
    }
  }

  async function addTask(event) {
    event.preventDefault();
    const cleanTitle = title.trim();

    if (!cleanTitle) {
      setError("请先输入任务内容。");
      return;
    }

    try {
      setError("");
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title: cleanTitle }),
      });

      if (!response.ok) {
        throw new Error("添加任务失败");
      }

      const newTask = await response.json();
      setTasks((current) => [...current, newTask]);
      setTitle("");
    } catch (err) {
      setError("添加失败，请稍后重试。");
    }
  }

  async function deleteTask(taskId) {
    try {
      setError("");
      const response = await fetch(`${API_URL}/${taskId}`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("删除任务失败");
      }

      setTasks((current) =>
        current.filter((task) => task.id !== taskId)
      );
    } catch (err) {
      setError("删除失败，请稍后重试。");
    }
  }

  return (
    <main className="page">
      <section className="task-card">
        <header className="page-header">
          <p className="eyebrow">FASTAPI + REACT</p>
          <h1>我的学习任务</h1>
          <p className="subtitle">记录今天最重要的学习目标</p>
        </header>

        <form className="task-form" onSubmit={addTask}>
          <input
            type="text"
            value={title}
            maxLength={50}
            placeholder="例如：练习 FastAPI GET 接口"
            onChange={(event) => setTitle(event.target.value)}
          />
          <button type="submit">添加任务</button>
        </form>

        {error && <p className="error-message">{error}</p>}

        {loading ? (
          <p className="status-message">正在读取任务……</p>
        ) : (
          <ul className="task-list">
            {tasks.map((task) => (
              <li className="task-item" key={task.id}>
                <span className="task-number">#{task.id}</span>
                <span className="task-title">{task.title}</span>
                <button
                  className="delete-button"
                  type="button"
                  onClick={() => deleteTask(task.id)}
                >
                  删除
                </button>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  );
}

export default App;