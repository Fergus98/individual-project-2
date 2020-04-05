mport pytest
import app

def test_rand_str():
    assert len(app.rand_str())==16 

def test_rand_str22():
    assert type(app.rand_str())==str
