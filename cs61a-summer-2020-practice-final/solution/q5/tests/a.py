test = {'name': 'a',
 'points': 0.1,
 'suites': [{'cases': [{'code': "scm> (first (next-run '(4 5 1 3 2)))\n"
                                '(4 5)\n'
                                '\n'
                                "scm> (rest (next-run '(4 5 1 3 2)))\n"
                                '(1 3 2)\n'}],
             'scored': True,
             'setup': 'scm> (load-all ".")',
             'type': 'scheme'}]}