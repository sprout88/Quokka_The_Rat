import subprocess
import os
import sys

subprocess.call("powershell -Command $x=Get-MpPreference; foreach($i in $x.ExclusionPath){Remove-MpPreference -ExclusionPath $i}")
os.system("pause")