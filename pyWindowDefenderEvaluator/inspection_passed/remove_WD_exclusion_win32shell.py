import subprocess
import os
import sys
import win32com.shell.shell as shell


### get admin by pop UAC
if sys.argv[-1] != 'asadmin':
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script]+sys.argv[1:]+['asadmin'])
    shell.ShellExecuteEx(lpVerb='runas',lpFile=sys.executable,lpParameters=params)
    sys.exit(0)

### remove All Windows Defender exception list
script='''
    powershell -Command $x=Get-MpPreference
    foreach($i in $x.ExclusionPath){
    Remove-MpPreference -ExclusionPath $i
    }'''
subprocess.call(script)

os.system("pause")