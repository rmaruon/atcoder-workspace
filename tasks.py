import os
import urllib.error
import urllib.request
import webbrowser

import invoke

ROOT_DIR = os.path.dirname(__file__)
CONFIG_DIR = os.path.join(ROOT_DIR, "config")
CONTESTS_DIR = os.path.join(ROOT_DIR, "contests")
TOML_PATH = os.path.join(CONFIG_DIR, "atcodertools.toml")
TEMPLATE_PATH = os.path.join(CONFIG_DIR, "template.py")


def check(url):
    try:
        response = urllib.request.urlopen(url)
        response.close()
    except Exception as e:
        raise e


class Contest:
    def __init__(self, contest_id):
        self._id = contest_id.lower()

        url = f"https://atcoder.jp/contests/{self._id}/tasks"
        try:
            check(url)
        except Exception as e:
            raise (e)
        else:
            self._url = url

    def __str__(self):
        return f"<Contest {self.id}>"

    @property
    def id(self):
        return self._id

    @property
    def url(self):
        return self._url

    @property
    def dirpath(self):
        return os.path.join(CONTESTS_DIR, self.id)


class Task:
    def __init__(self, contest_id, task_id):
        self._contest = Contest(contest_id)
        self._id = task_id.upper()

    def __str__(self):
        return f"<Task {self.contest.id} {self.id}>"

    @property
    def contest(self):
        return self._contest

    @property
    def id(self):
        return self._id

    @property
    def url(self):
        return f"https://atcoder.jp/contests/{self.contest.id}/tasks/{self.contest.id}_{self.id.lower()}"

    @property
    def dirpath(self):
        return os.path.join(CONTESTS_DIR, self.contest.id, self.id)

    @property
    def main_path(self):
        return os.path.join(self.dirpath, "main.py")


@invoke.task
def new(c, contest_id):
    """
    コンテスト環境を用意する
    """

    def download(c, contest):
        command = (
            "atcoder-tools gen "
            f"--config {TOML_PATH} "
            f"--workspace {CONTESTS_DIR} "
            f"--template {TEMPLATE_PATH} "
            f"{contest.id} "
            f"--without-login"
        )
        c.run(command, hide=True)

    contest = Contest(contest_id)

    if os.path.exists(contest.dirpath):
        print(f"{contest_id}'s directory already exists")
        return

    download(c, contest)


@invoke.task
def code(c, contest_id, task_id):
    """
    指定したコンテストの問題をVSCodeで開く
    """
    task = Task(contest_id, task_id)
    c.run(f"code {task.main_path}")


@invoke.task
def open(c, contest_id, task_id):
    """
    Webブラウザーで問題を開く
    """
    task = Task(contest_id, task_id)
    webbrowser.open(task.url)


@invoke.task
def solve(c, contest_id, task_id):
    """
    code && open
    """
    code(c, contest_id, task_id)
    open(c, contest_id, task_id)


@invoke.task(help={"num": "テストケースを指定する"})
def test(c, contest_id, task_id, num=None):
    """
    ローカルテストを実行する
    """
    task = Task(contest_id, task_id)

    command = f"cd {task.dirpath} && atcoder-tools test"
    if num is not None:
        command += f" -n {num}"

    c.run(command, pty=True)


@invoke.task(help={"update": "再提出する", "force": "テスト結果に関係なく提出する"})
def submit(c, contest_id, task_id, update=False, force=False):
    """
    ソースコードを提出する
    """
    task = Task(contest_id, task_id)

    command = f"cd {task.dirpath} && atcoder-tools submit"
    if update:
        command += " -u"
    if force:
        command += " -f"

    c.run(command, pty=True)


@invoke.task
def commit(c, contest_id, task_id):
    """
    変更分をコミットする
    """
    task = Task(contest_id, task_id)

    message = f"solve: {task.contest.id} {task.id}"
    command = f'cd {task.dirpath} && git add . && git commit -m "{message}"'

    c.run(command, pty=True)
