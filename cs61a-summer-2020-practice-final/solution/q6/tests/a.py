test = {'name': 'a',
 'points': 0.1,
 'suites': [{'cases': [{'code': "scm> (zero-cond ((0 'result1) ((- 1 1) "
                                "'result2) ((* 1 1) 'result3) (2 'result4)))\n"
                                'result3\n'}],
             'scored': True,
             'setup': 'scm> (load-all ".")',
             'type': 'scheme'}]}