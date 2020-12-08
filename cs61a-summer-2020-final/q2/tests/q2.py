test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t1 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])]), Tree(5)])
          
          >>> print(t1)
          1
              2
                  3
                      4
              5
          
          >>> pruner(t1, 2)
          
          >>> print(t1)
          1
              2
                  3
              5
                  advice
          
          >>> t2 = Tree(4, [Tree(5, [Tree(6), Tree(7)]), Tree(10), Tree(15, [Tree(16, [Tree(17, [Tree(18, [Tree(19)])])])])])
          
          >>> pruner(t2, 3)
          
          >>> print(t2)
          4
              5
                  6
                      advice
                  7
                      advice
              10
                  advice
                      advice
              15
                  16
                      17
          
          >>> t1 = Tree(1, [Tree(2, [Tree(3)]), Tree(5, [Tree("advice")])])
          
          >>> print(t1)
          1
              2
                  3
              5
                  advice
          
          >>> smallest_no_advice(t1)
          [1, 5]
          
          >>> t2 = Tree(4, [Tree(5, [Tree(6, [Tree("advice")]), Tree(7, [Tree("advice")])]), Tree(10, [Tree("advice", [Tree("advice")])]), Tree(15, [Tree(16, [Tree(17)])])])
          
          >>> print(t2)
          4
              5
                  6
                      advice
                  7
                      advice
              10
                  advice
                      advice
              15
                  16
                      17
          
          >>> smallest_no_advice(t2)
          [4, 10]
          
          >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
          
          >>> t.label
          3
          
          >>> t.branches[0].label
          2
          
          >>> t.branches[1].is_leaf()
          True
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
