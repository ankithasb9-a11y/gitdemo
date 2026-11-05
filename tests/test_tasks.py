import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from task import Task


def test_create_task():
    task = Task(1, "Learn Python")

    assert task.task_id == 1
    assert task.title == "Learn Python"
    assert task.completed is False


def test_complete_task():
    task = Task(1, "Learn Git")
    task.mark_completed()

    assert task.completed is True