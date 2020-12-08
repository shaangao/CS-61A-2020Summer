test = {'name': 'b',
 'points': 0.1,
 'suites': [{'cases': [{'code': "scm> (zip-tail '(1 2 3) '(4 5 6))\n"
                                '((1 4) (2 5) (3 6))\n'
                                '\n'
                                "scm> (zip-tail '(c 6 a) '(s 1 ! hello "
                                'world))\n'
                                '((c s) (6 1) (a !))\n'}],
             'scored': True,
             'setup': 'scm> (load-all ".")',
             'type': 'scheme'}]}