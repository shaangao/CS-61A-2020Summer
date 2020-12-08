test = {'name': 'b',
 'points': 0.1,
 'suites': [{'cases': [{'code': '>>> double = lambda x: x*2\n'
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
                                'Tree(12, [Tree(4), Tree(10)])\n'}],
             'scored': True,
             'setup': '>>> from q2 import *',
             'type': 'doctest'}]}