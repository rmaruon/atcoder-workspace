import os
import urllib.request


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

    def dirname(self, contests_dir):
        return os.path.join(contests_dir, self.id)
