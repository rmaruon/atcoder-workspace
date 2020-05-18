import invoke


@invoke.task
def t(c):
    invoke.run('oj t -c "python main.py"')
