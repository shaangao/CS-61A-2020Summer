test = {
  'name': 'q3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> hacker = cat([1,2], 2)
          
          >>> hacker(1)
          
          >>> hacker(2)
          'Access granted!'
          
          >>> hacker = cat([1,2], 1)
          
          >>> hacker(1)
          
          >>> hacker(3) # used up attempts to gain access
          
          >>> hacker(2) # correct attempt to gain access, but already locked
          'The trapdoor has been activated!'
          
          >>> hacker = cat([1,2], 2)
          
          >>> hacker(1)
          
          >>> hacker(3) # 1 attempt left to gain access
          
          >>> hacker(2) # correct attempt to gain access
          'Access granted!'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hacker = cat([1], 4)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          'The trapdoor has been activated!'
          
          >>> hacker = cat([1], 4)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(1)
          'The trapdoor has been activated!'
          
          >>> hacker = cat([1], 4)
          
          >>> hacker(1)
          'Access granted!'
          
          >>> hacker = cat([1, 2, 3, 4, 5, 6], 4)
          
          >>> hacker(1)
          
          >>> hacker(2)
          
          >>> hacker(3)
          
          >>> hacker(4)
          
          >>> hacker(5)
          
          >>> hacker(6)
          'Access granted!'
          
          >>> hacker = cat([1,2,3,4], 2)
          
          >>> hacker(1)
          
          >>> hacker(2)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(4)
          'Access granted!'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
