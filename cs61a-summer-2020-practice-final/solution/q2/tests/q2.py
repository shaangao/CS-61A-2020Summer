test = {'name': 'q2',
 'points': 14,
 'suites': [{'cases': [{'code': '>>> [k for k in range(1000) if is_combo(357, '
                                'k)]\n'
                                '[0, 7, 12, 15, 22, 35, 56, 105]\n'
                                '\n'
                                '>>> double = lambda x: x*2\n'
                                '\n'
                                '>>> square = lambda x: x**2\n'
                                '\n'
                                '>>> identity = lambda x: x\n'
                                '\n'
                                '>>> t1 = Tree(double, [Tree(square), '
                                'Tree(identity)])\n'
                                '\n'
                                '>>> t2 = Tree(6, [Tree(2), Tree(10)])\n'
                                '\n'
                                '>>> apply_tree(t1, t2)\n'
                                '\n'
                                '>>> t2\n'
                                'Tree(12, [Tree(4), Tree(10)])\n'
                                '\n'
                                '>>> t1 = Tree(5, [Tree(2), Tree(1)])\n'
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
                                'Tree(True, [Tree(True), Tree(False)])\n'
                                '\n'
                                '>>> t = Tree(3, [Tree(2, [Tree(5)]), '
                                'Tree(4)])\n'
                                '\n'
                                '>>> t.label\n'
                                '3\n'
                                '\n'
                                '>>> t.branches[0].label\n'
                                '2\n'
                                '\n'
                                '>>> t.branches[1].is_leaf()\n'
                                'True\n'}],
             'scored': True,
             'setup': '>>> from q2 import *',
             'type': 'doctest'}]}