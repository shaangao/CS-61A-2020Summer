test = {'name': 'a',
 'points': 0.1,
 'suites': [{'cases': [{'code': '>>> t = Tree(4, [Tree(5, [Tree(6, '
                                '[Tree(5)])]), Tree(1, [])])\n'
                                '\n'
                                '>>> tree_search(t, lambda x: x % 2 == 1)\n'
                                'Link(1, Link(5, Link(5)))\n'}],
             'scored': True,
             'setup': '>>> from q4 import *',
             'type': 'doctest'}]}