test = {'name': 'q6',
 'points': 8,
 'suites': [{'cases': [{'code': "scm> (zero-cond ((0 'result1) ((- 1 1) "
                                "'result2) ((* 1 1) 'result3) (2 'result4)))\n"
                                'result3\n'
                                '\n'
                                "scm> (zip-tail '(1 2 3) '(4 5 6))\n"
                                '((1 4) (2 5) (3 6))\n'
                                '\n'
                                "scm> (zip-tail '(c 6 a) '(s 1 ! hello "
                                'world))\n'
                                '((c s) (6 1) (a !))\n'
                                '\n'
                                "scm> (append '(1 2 3) '(4 5 6))\n"
                                '(1 2 3 4 5 6)\n'}],
             'scored': True,
             'setup': 'scm> (load-all ".")',
             'type': 'scheme'}]}