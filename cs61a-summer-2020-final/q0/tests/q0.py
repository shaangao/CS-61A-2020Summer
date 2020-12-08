test = {
  'name': 'q0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_compvsinterp in ['True, there is no way to convert an interpreter to a compiler', 'False, you can turn an interpreter into a compiler via a Futamura projection', 'False, compilers and interpreters are the same'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_pyfeatures in ['Memory Management', 'Coroutines', 'Lazy Evaluation', 'Functions'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_machine_learning in ['Determine f(x)', 'Determine x', 'Determine f'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_neural_networks in ['Being an inference tool', 'Approximating nonlinear relationships', 'Using high-dimensional space', 'Finding features'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
