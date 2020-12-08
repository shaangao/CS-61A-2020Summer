test = {
  'name': 'question_2',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sculptural(1234, 1)
          4
          
          >>> sculptural(32749, 2)
          79
          
          >>> sculptural(1917, 2)
          97
          
          >>> sculptural(32749, 18)
          32749
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from question_2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
