test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (leadership-locator 10)
          (1 0)
          
          scm> (leadership-locator 10001)
          (1 0 0 0 1)
          
          scm> (leadership-locator 8080)
          ((8) 0 (8) 0)
          
          scm> (leadership-locator 123456780)
          (1 2 3 4 5 6 7 (8) 0)
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'scm> (load-all ".")',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
