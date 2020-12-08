test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t3 = Tree(10, [Tree(20, [Tree("advice", [Tree("advice", [Tree("advice")])])]), Tree(30, [Tree(50, [Tree("advice", [Tree("advice")])])]), Tree(40, [Tree(70, [Tree("advice", [Tree("advice")])])])])
          
          >>> print(t3)
          10
              20
                  advice
                      advice
                          advice
              30
                  50
                      advice
                          advice
              40
                  70
                      advice
                          advice
          
          >>> smallest_no_advice(t3)
          [10, 20]
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
