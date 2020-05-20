import os
import shutil
import tempfile
import urllib.error
import urllib.request
import webbrowser

from bs4 import BeautifulSoup
import invoke

ROOT_DIR = os.path.dirname(__file__)
CONFIG_DIR = os.path.join(ROOT_DIR, 'config')
CONTESTS_DIR = os.path.join(ROOT_DIR, 'contests')
TOML_PATH = os.path.join(CONFIG_DIR, 'atcodertools.toml')
TEMPLATE_PATH = os.path.join(CONFIG_DIR, 'template.py')


class Contest:
    def __init__(self, contest_id):
        self._id = contest_id

        url = f'https://atcoder.jp/contests/{contest_id.lower()}/tasks'
        if not url_exists(url):
            self._url = ''
        else:
            self._url = url

    @property
    def id(self):
        return self._id

    @property
    def url(self):
        return self._url

    def get_tasks(self):
        # task_urlが contest_id + task_idでは決まらないことがあるため、HTMLをparseする
        html = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html, 'html.parser')
        tr_list = soup.select('#main-div .row table > tbody > tr')

        tasks = {}
        for tr in tr_list:
            td_list = tr.find_all('td')

            href = td_list[0].a.get('href')
            task_url = f'https://atcoder.jp{href}'
            task_id = td_list[0].a.string.upper()
            task_title = td_list[1].a.string

            tasks[task_id] = Task(self, task_id, task_title, task_url)

        return tasks

    def is_invalid(self):
        return not self.url


class Task:
    def __init__(self, contest, task_id, title, url):
        self._contest = contest
        self._id = task_id
        self._title = title
        self._url = url

    @property
    def contest(self):
        return self._contest

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url


def url_exists(url):
    try:
        response = urllib.request.urlopen(url)
        response.close()
        return True
    except urllib.error.HTTPError as e:
        print(f'{e.reason}: {url}')
        return False
    except urllib.error.URLError:
        print('URLError')
        return False


def download_all(contest):
    command = ("atcoder-tools gen "
               f"--config {TOML_PATH} "
               f"--workspace {CONTESTS_DIR} "
               f"--template {TEMPLATE_PATH} "
               f"{contest.id}")
    invoke.run(command, hide=True)

    print(f'{contest.id} {contest.url}')


def download(task):
    contest = task.contest

    with tempfile.TemporaryDirectory() as temp_dir:
        # atcoder-toolsはtaskごとにダウンロードできない (contestで一括)
        # OPTIMIZE:
        command = ("atcoder-tools gen "
                   f"--config {TOML_PATH} "
                   f"--workspace {temp_dir} "
                   f"--template {TEMPLATE_PATH} "
                   f"{contest.id}")
        invoke.run(command, hide=True)

        src_path = os.path.join(temp_dir, contest.id, task.id)
        dest_path = os.path.join(CONTESTS_DIR, contest.id, task.id)
        shutil.copytree(src_path, dest_path)

    print(f'{contest.id}: {task.id} {task.title} {task.url}')
    print(f'Saved to {dest_path}')
    print(f'Edit: {os.path.join(dest_path, "main.py")}')


@invoke.task
def new(c, contest_id, task_id=''):
    """
    コンテスト環境を用意する
    """
    task_id = task_id.upper()
    dest_path = os.path.join(CONTESTS_DIR, contest_id, task_id)
    if os.path.exists(dest_path):
        print(f'{contest_id}/{task_id}: directory exists')
        return

    contest = Contest(contest_id)
    if contest.is_invalid():
        return

    if not task_id:
        download_all(contest)
        return

    tasks = contest.get_tasks()
    task = tasks.get(task_id)
    if not task:
        print(f'{contest.id} {task_id}: not found')
        return

    download(task)


@invoke.task
def open(c, contest_id, task_id=''):
    """
    Webブラウザーで問題を開く
    """
    task_id = task_id.upper()
    contest = Contest(contest_id)

    if not task_id:
        webbrowser.open(contest.url)
        return

    tasks = contest.get_tasks()
    task = tasks.get(task_id)
    if not task:
        return

    webbrowser.open(task.url)


@invoke.task
def test(c):
    """
    ローカルテストを実行する
    """
    command = "atcoder-tools test"
    c.run(command, pty=True)


@invoke.task(help={'update': '再提出する', 'force': 'テスト結果に関係なく提出する'})
def submit(c, update=False, force=False):
    """
    ソースコードを提出する
    """
    command = "atcoder-tools submit"
    if update:
        command += " -u"
    if force:
        command += ' -f'

    c.run(command, pty=True)


@invoke.task
def commit(c):
    """
    カレントディレクトリの変更分をコミットする
    """
    curdir = os.path.abspath(os.path.curdir)

    two_up = curdir.split('/')[-3]
    if two_up != 'contests':
        return

    contest_id = curdir.split('/')[-2]
    task_id = curdir.split('/')[-1]
    message = f'solve: {contest_id} {task_id}'

    c.run('git add .', pty=True)
    c.run(f'git commit -m "{message}"', pty=True)
