import pickle
import hashlib

def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)
 
    
def test1():
    t = get_pickle('q1.pickle')
    assert 'eccbc87e4b5ce2fe28308fd9f2a7baf3'==t
    
    
def test2():
    t = get_pickle('q2.pickle')
    assert 'd328466f731cff1114dad3049b1363b6'==t
    

def test3():
    t = get_pickle('q3.pickle')
    assert 'fb7fa22ede616c04c68a7663d0f81e92'==t
    


def test4():
    t = get_pickle('q4.pickle')
    assert '30fdb63195331e96390bc1ecee0f2950'==t
    


def test5():
    t = get_pickle('q5.pickle')
    assert 'bfb411effcea9edccb9f79402d1a21bd'==t

def test6():
    t=get_pickle('q6.pickle')
    assert 'a67778b3dcc82bfaace0f8bc0061f20e'==t
