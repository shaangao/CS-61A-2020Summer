test = {'name': 'c',
 'points': 0.1,
 'suites': [{'cases': [{'code': '>>> t1 = Tree(5, [Tree(2), Tree(1)])\n'
                                '\n'
                                '>>> fn_tree = make_checker_tree(t1)\n'
                                '\n'
                                '>>> t2 = Tree(5, [Tree(10), Tree(7)])\n'
                                '\n'
                                '>>> apply_tree(fn_tree, t2) #5 is a combo of '
                                "5, 10 is a combo of 52, 7 isn't a combo of "
                                '51\n'
                                '\n'
                                '>>> t2\n'
                                'Tree(True, [Tree(True), Tree(False)])\n'}],
             'scored': True,
             'setup': '>>> from q2 import *',
             'type': 'doctest'}]}