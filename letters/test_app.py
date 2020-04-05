import pytest
import app
   
def test_rand_int1():
    assert len(app.rand_int())==16 

def test_rand_int2():
    assert type(app.rand_int())==str
