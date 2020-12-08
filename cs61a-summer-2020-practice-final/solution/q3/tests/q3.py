test = {'name': 'q3',
 'points': 9,
 'suites': [{'cases': [{'code': '>>> cs61a_plus = Network()\n'
                                '\n'
                                ">>> cs61a_plus.add_friend('Robert', "
                                "'Jeffrey')\n"
                                '\n'
                                ">>> cs61a_plus.friends['Robert']\n"
                                "['Jeffrey']\n"
                                '\n'
                                ">>> cs61a_plus.friends['Jeffrey']\n"
                                "['Robert']\n"
                                '\n'
                                ">>> cs61a_plus.add_friend('Jessica', "
                                "'Robert')\n"
                                '\n'
                                ">>> cs61a_plus.friends['Robert']\n"
                                "['Jeffrey', 'Jessica']\n"
                                '\n'
                                '>>> cs61a_plus = Network()\n'
                                '\n'
                                ">>> cs61a_plus.friends = {'Robert': "
                                "['Jeffrey', 'Jessica'], 'Jeffrey': ['Robert', "
                                "'Jessica', 'Yulin'], 'Jessica': ['Robert', "
                                "'Jeffrey', 'Yulin'], 'Yulin': ['Jeffrey', "
                                "'Jessica'], 'Albert': []}\n"
                                '\n'
                                ">>> cs61a_plus.degrees('Robert', 'Yulin', 2) "
                                '# Exactly 2 degrees\n'
                                'True\n'
                                '\n'
                                ">>> cs61a_plus.degrees('Robert', 'Jessica', "
                                '2) # Less than 2 degrees\n'
                                'True\n'
                                '\n'
                                ">>> cs61a_plus.degrees('Yulin', 'Robert', 1) "
                                '# More than 1 degree\n'
                                'False\n'
                                '\n'
                                ">>> cs61a_plus.degrees('Albert', 'Jessica', "
                                '10) # No friends!\n'
                                'False\n'}],
             'scored': True,
             'setup': '>>> from q3 import *',
             'type': 'doctest'}]}