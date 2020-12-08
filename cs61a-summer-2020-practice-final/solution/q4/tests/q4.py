test = {'name': 'q4',
 'points': 10,
 'suites': [{'cases': [{'code': '>>> t = Tree(4, [Tree(5, [Tree(6, '
                                '[Tree(5)])]), Tree(1, [])])\n'
                                '\n'
                                '>>> tree_search(t, lambda x: x % 2 == 1)\n'
                                'Link(1, Link(5, Link(5)))\n'
                                '\n'
                                '>>> t = Tree(6, [Tree(3, [Tree(5, [Tree(9), '
                                'Tree(2, [Tree(9)])]), Tree(1)]), Tree(4, '
                                '[Tree(0, [Tree(4)])])])\n'
                                '\n'
                                '>>> org = Organizer([lambda x: x > 4, lambda '
                                'x: x % 2 == 0])\n'
                                '\n'
                                '>>> org.categorize(t)\n'
                                '[Link(9, Link(5, Link(6))), Link(0, Link(4, '
                                'Link(2)))]\n'
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
             'setup': '>>> from q4 import *',
             'type': 'doctest'}]}