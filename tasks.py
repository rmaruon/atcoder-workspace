import os
import invoke

ROOT = os.path.dirname(__file__)


@invoke.task
def new(c, contest_id):
    """
    コンテスト環境を用意する
    """
    toml_path = os.path.join(ROOT, 'config', 'atcodertools.toml')
    workspace_path = os.path.join(ROOT, 'contests')
    template_path = os.path.join(ROOT, 'config', 'template.py')

    command = ("atcoder-tools gen "
               f"--config {toml_path} "
               f"--workspace {workspace_path}  "
               f"--template {template_path} "
               f"{contest_id}")
    invoke.run(command, pty=True)


@invoke.task
def test(c):
    """
    ローカルテストを実行する
    """
    command = "atcoder-tools test"
    c.run(command, pty=True)


@invoke.task(help={'update': '再提出する'})
def submit(c, update=False):
    """
    ソースコードを提出する
    """
    command = "atcoder-tools submit"
    if update:
        command += " -u"
    c.run(command, pty=True)
