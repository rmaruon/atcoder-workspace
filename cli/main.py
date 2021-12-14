import os
import pathlib
import subprocess
import webbrowser

import fire

from contest import Contest
from task import Task

ROOT_DIR = os.path.dirname(pathlib.Path(__file__).parent)
CONTESTS_DIR = os.path.join(ROOT_DIR, "contests")
TOML_PATH = os.path.join(ROOT_DIR, "cli", "atcodertools.toml")


def new(contest_id):
    """
    コンテスト環境を用意する
    """
    contest = Contest(contest_id)
    command = (
        "atcoder-tools gen "
        f"--config {TOML_PATH} "
        f"--workspace {CONTESTS_DIR} "
        f"{contest.id} "
    )
    subprocess.run(command, shell=True)


def code(contest_id, task_id):
    """
    指定したコンテストの問題をVSCodeで開く
    """
    task = Task(Contest(contest_id), task_id)
    subprocess.run(["code", task.filepath_main(CONTESTS_DIR)])


def web(contest_id, task_id):
    """
    Webブラウザーで問題を開く
    """
    task = Task(Contest(contest_id), task_id)
    webbrowser.open(task.url)


def solve(contest_id, task_id):
    """
    code && open
    """
    code(contest_id, task_id)
    web(contest_id, task_id)


def test(contest_id, task_id, num=None):
    """
    ローカルテストを実行する
    {"num": "テストケースを指定する"}
    """
    task = Task(Contest(contest_id), task_id)

    command = f"cd {task.dirname(CONTESTS_DIR)} && atcoder-tools test"
    if num is not None:
        command += f" -n {num}"

    subprocess.run(command, shell=True)


def submit(contest_id, task_id, update=False, force=False):
    """
    ソースコードを提出する
    {"update": "再提出する", "force": "テスト結果に関係なく提出する"}
    """
    task = Task(Contest(contest_id), task_id)

    command = f"cd {task.dirname(CONTESTS_DIR)} && atcoder-tools submit"
    if update:
        command += " -u"
    if force:
        command += " -f"

    subprocess.run(command, shell=True)


def commit(contest_id, task_id):
    """
    変更分をコミットする
    """
    task = Task(Contest(contest_id), task_id)

    message = f"solve: {task.contest.id} {task.id}"
    command = (
        f'cd {task.dirname(CONTESTS_DIR)} && git add . && git commit -m "{message}"'
    )

    subprocess.run(command, shell=True)


if __name__ == "__main__":
    fire.Fire(
        {
            "new": new,
            "code": code,
            "web": web,
            "solve": solve,
            "test": test,
            "submit": submit,
            "commit": commit,
        }
    )
