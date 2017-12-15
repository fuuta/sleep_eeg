
def omazinai():
    #==============this code added==================================================================================:
    import os
    if os.getenv("DDEBUG") == '1':
        print('Remote Debug Mode\n')
        import sys
        sys.path.append("pycharm-debug-py3k.egg")
        import pydevd

        # pydevd.settrace('<address of the Windows machine>', port=12345, stdoutToServer=True, stderrToServer=True)
        pydevd.settrace('192.168.13.203', port=12345, stdoutToServer=True, stderrToServer=True)
    #===============================================================================================================
