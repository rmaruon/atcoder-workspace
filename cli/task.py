import os


class Task:
    def __init__(self, contest, task_id):
        self._contest = contest
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

    def dirname(self, contests_dir):
        return os.path.join(contests_dir, self.contest.id, self.id)

    def filepath_main(self, contest_dir):
        return os.path.join(self.dirname(contest_dir), "main.py")
