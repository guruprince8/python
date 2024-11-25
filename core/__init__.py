__author__ = "Gurubrahmanandam Ekambaram"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2024- Gurubrahmanandam Ekambaram"
# Use of this source code is governed by the GNU license.
__license__ = "GNU"


def execute_if_block():
    x = int(input("Please enter an integer: "))

    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')


def execute_for_block():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))


execute_if_block()
execute_for_block()
