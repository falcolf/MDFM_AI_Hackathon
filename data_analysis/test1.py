import pickle
import hashlib
import numpy as np

def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)
def test1():
    t =get_pickle('q1.pickle')
    s= get_pickle('pick/a1.pickle')
    assert type(s)==type(t)
def test2():
    t =get_pickle('q2.pickle')
    s= get_pickle('pick/a2.pickle')
    if((type(t)==type(s)) or (type(5.4))==type(t)):
        res=True
    else:
        res=False
    assert res
def test3():
    t =get_pickle('q3.pickle')
    s= get_pickle('pick/a3.pickle')
    assert type(s)==type(t)
def test4():
    t =get_pickle('q4.pickle')
    s= get_pickle('pick/a4.pickle')
    # d=abs(t-s)
    # if d<=1:
    # 	res=True
    # else:
    # 	res=False
    if((type(t)==type(s)) or (type(5.4))==type(t)):
        res=True
    else:
        res=False
    assert res
    # assert type(s)==type(t)

def test6():
    t =get_pickle('q6.pickle')
    s= get_pickle('pick/a6.pickle')
    assert type(s)==type(t)
def test7():
    t =get_pickle('q7.pickle')
    s= get_pickle('pick/a7.pickle')
    # d=abs(t-s)
    # if d<=1:
    # 	res=True
    # else:
    # 	res=False
    if((type(t)==type(s)) or (type(5.4))==type(t)):
        res=True
    else:
        res=False
    assert res
    # assert type(s)==type(t)
def test8():
    t =get_pickle('q8.pickle')
    s= get_pickle('pick/a8.pickle')
    assert type(s)==type(t)
def test9():
    t =get_pickle('q9.pickle')
    s= get_pickle('pick/a9.pickle')
    assert type(s)==type(t)
def test10():
    t =get_pickle('q10.pickle')
    s= get_pickle('pick/a10.pickle')
    if((type(t)==type(s)) or (type(np.int64(5)))==type(t)):
        res=True
    else:
        res=False
    assert res
    # assert type(s)==type(t)
    # print(type(np.int64(5)))
    # print(type(t))
def test11():
    t =get_pickle('q11.pickle')
    s= get_pickle('pick/a11.pickle')
    # d=abs(t-s)
    # if d<=1:
    # 	res=True
    # else:
    # 	res=False
    if((type(t)==type(s)) or (type(5.4))==type(t)):
        res=True
    else:
        res=False
    assert res
    # assert type(s)==type(t)
