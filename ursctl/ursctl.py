#!/usr/bin/env python3

def run():
    import getopt, sys
    from pathlib import Path

    macPath = Path('/opt/cisco/anyconnect/bin/plugins/')
    macFiles = {'libacumbrellaapi.dylib', 'libacumbrellactrl.dylib', 'libacumbrellaplugin.dylib'}
    winPath = Path('C:/Program Files (x86)/Cisco/Cisco AnyConnect Secure Mobility Client/Plugins/')
    winFiles = {'acumbrellaapi.dll', 'acumbrellactrl.dll', 'acumbrellaplugin.dll'}

    usage = ("Cisco Umbrella Roaming Security module for AnyConnect control utility\n"
             "usage: ursctl [option]\n"
             "	-d, --disable	Disable the module\n"
             "	-e, --enable	Enable the module\n"
             "	-s, --status	Print module status")

    if len(sys.argv) != 2:
        print(usage)
        sys.exit(1)

    try:
        arguments, values = getopt.getopt(sys.argv[1:], 'des', ['disable', 'enable', 'status'])
    except getopt.error as err:
        print(str(err))
        print(usage)
        sys.exit(1)

    if macPath.exists():
        libPath = macPath
        libFiles = macFiles
    elif winPath.exists():
        libPath = winPath
        libFiles = winFiles
    else:
        sys.exit('Could not locate Cisco Umbrella Roaming Security module for AnyConnect')

    for currentArgument, currentValue in arguments:
        if currentArgument in ('-d', '--disable'):
            try:
                (libPath / 'disabled').mkdir(exist_ok=True)
                for libFile in libFiles:
                    if (libPath / libFile).exists():
                        (libPath / libFile).replace(libPath / 'disabled' / libFile)
            except:
                sys.exit('permission error, utility must be run with elevated privileges')
        elif currentArgument in ('-e', '--enable'):
            if not (libPath / 'disabled/').exists():
                sys.exit('cannot enable, module may not have been disabled by this utility')
            try:
                for libFile in libFiles:
                    if (libPath / 'disabled' / libFile).exists():
                        (libPath / 'disabled' / libFile).replace(libPath / libFile)
            except:
                sys.exit('permission error, utility must be run with elevated privileges')

    for libFile in libFiles:
        if (libPath / libFile).exists():
            print('Umbrella Roaming Security module is ENABLED')
            sys.exit(0)
    print('Umbrella Roaming Security module is DISABLED')
    sys.exit(0)

if __name__ == '__main__':
    run()

