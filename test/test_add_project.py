from  model.project import Project
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

n = 2
testdata = [
    Project(name=random_string("project", 10))
    for i in range(n)
]

@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):

   app.project.add(project)
