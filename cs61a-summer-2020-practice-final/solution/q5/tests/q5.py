test = {'name': 'q5',
 'points': 9,
 'suites': [{'cases': [{'code': "scm> (first (next-run '(4 5 1 3 2)))\n"
                                '(4 5)\n'
                                '\n'
                                "scm> (rest (next-run '(4 5 1 3 2)))\n"
                                '(1 3 2)\n'
                                '\n'
                                "scm> (runs '(3 4 7 6 6 8 1 2 5 5 4))\n"
                                '((3 4 7) (6 6 8) (1 2 5 5) (4))\n'
                                '\n'
                                "scm> (runs '(4 3 2 3))\n"
                                '((4) (3) (2 3))\n'}],
             'scored': True,
             'setup': 'scm> (load-all ".")',
             'type': 'scheme'}]}