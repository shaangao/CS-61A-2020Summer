test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t3 = Tree(10, [Tree(20), Tree(30, [Tree(50)]), Tree(40, [Tree(70)])])
          
          >>> pruner(t3, 4)
          
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
