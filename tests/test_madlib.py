from madlib_cli.madlib import read_template, parse, merge
import pytest 

def testRead():
    expected = open('assets/template.txt','r').read()
    received = read_template()
    assert expected == received

def testParse():
    expected = ["first name","age"]
    received = parse("hello {first name}, I am {age} years old")
    assert expected == received

# def testMerge():
#     received = merge(readfile())
#     expected = open('assets/template.txt','r').read()
#     assert expected == received

# @pytest.mark.skip(reason="Still working on it")
def testMerge():
    words = ['smart', 'boxes', 'hungry', 'eat']
    text = 'A {} {} had a {} dog so they {} them'
    received = merge(text, words)
    expected = 'A smart boxes had a hungry dog so they eat them'
    assert expected == received