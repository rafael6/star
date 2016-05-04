#!/usr/bin/env python3

import system_1
import system_2
import system_3


index = {1: 'System-1',
         2: 'System-2',
         3: 'System-3'}

intro = '''\nWelcome to System Tester and Reporter (STaR).\n
Enter the number of the system you wish to test or Ctrl+C to exit:'''


def main():
    """ List a number of possibilities where each is a system test script."""

    while True:
        try:
            print(intro)

            for k, v in sorted(index.items()):
                print('\t', k, ': ', v, sep='')

            choice = int(input('\nEnter a number> '))

            application = index.get(choice, 'Not a valid selection!')

            if application == 'System-1':
                system_1.main()
            elif application == 'System-2':
                system_2.main()
            elif application == 'System-3':
                sytem_3.main()
            else:
                print('\n'+application)
                main()
        except KeyboardInterrupt:
            print('\n\nThank you for using STaR.')

if __name__ == "__main__":
    main()
