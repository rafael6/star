#!/usr/bin/python

__author__ = 'Rafael'

import system1

def main():
    """Start point. List system-test scripts as options and process the option
     selected by the user."""

    try:
        print '''\nWelcome to System Tester and Reporter (STaR).
        Enter an number from the options below or Ctr&C to exit:
                1. Script1
                2. Script2'''

        choice = raw_input('> ')

        if choice == '1':
            system1.main()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            print '%s is not a valid selection, try again' % choice
            main()

    except KeyboardInterrupt:
        print ' Thank you for using STaR.'
    finally:
        exit()


if __name__ == "__main__":
    main()