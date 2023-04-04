import subprocess
import os
import sys

#script = "powershell -Command Add-MpPreference -ExclusionPath "+os.getcwd()
#subprocess.call(script,shell=True)
subprocess.call("powershell -Command $x=Get-MpPreference; foreach($i in $x.ExclusionPath){Remove-MpPreference -ExclusionPath $i}")
#os.system("pause")