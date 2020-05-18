import os
import invoke

ROOT = os.path.dirname(__file__)


@invoke.task
def new(c, contest_id):
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
    command = ("atcoder-tools test")
    invoke.run(command, pty=True)
