test = {
  'name': 'q1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (leadership-locator 12)
          (1 2)
          
          scm> (leadership-locator 1881)
          (1 (8) (8) 1)
          
          scm> (leadership-locator 0) ; no digits
          ()
          
          scm> (leadership-locator 88888888)
          ((8) (8) (8) (8) (8) (8) (8) (8))
          
          scm> (leadership-locator 1128651)
          (1 1 2 (8) 6 5 1)
          
          scm> (define just-guitar (cons-stream 'guitar just-guitar))
          just-guitar
          
          scm> (define two (cons-stream 1 (cons-stream 'guitar two)))
          two
          
          scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'guitar three))))
          three
          
          scm> (take 10 two)
          (1 guitar 1 guitar 1 guitar 1 guitar 1 guitar)
          
          scm> (take 10 three)
          (x y guitar x y guitar x y guitar x)
          
          scm> (take 10 (salad-switch two three))
          (1 x y 1 x y 1 x y 1)
          
          scm> (take 10 (salad-switch two just-guitar))
          (1 1 1 1 1 1 1 1 1 1)
          
          scm> (take 10 (salad-switch three three))
          (x y x y x y x y x y)
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
