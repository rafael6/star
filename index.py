#!/usr/bin/python

__author__ = 'Rafael'

import system1


def main():
    """Start point. List each system with a corresponding index/number as
    options. Calls the appropriate system for testing."""

    try:
        print '''\nWelcome to System Tester and Reporter (STaR).
        Enter a corresponding number from the options below or Ctr+C to exit:
                1. System 1
                2. System 2
                3. System 3'''

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