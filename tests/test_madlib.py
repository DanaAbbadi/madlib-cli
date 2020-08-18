from madlib_cli.madlib import readfile, parse, merge

def testRead():
    expected = open('assets/template.txt','r').read()
    received = readfile()
    assert expected == received

def testParse():
    expected = ["first name","age"]
    received = parse("hello {first name}, I am {age} years old")
    assert expected == received

# def testMerge():
#     received = merge(readfile())
#     expected = open('assets/template.txt','r').read()
#     assert expected == received
