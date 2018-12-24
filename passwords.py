#! python3

# passwords.py: An insecure password manager program.

import pyperclip

passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python passwords.py [account] - copy account password.')
    sys.exit()

account = sys.argv[1]   # First command line arg is account name.

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no password for account')
