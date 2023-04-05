import ctypes, sys, os, subprocess
def run_as_admin():
    # check is user admin already
    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    # get sysinfo of current running script
    script = sys.argv[0]
    params = ' '.join([f'"{x}"' for x in sys.argv[1:]])
    # ShellExecute to pop UAC
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, script, params, 1)
    # current process is not run as admin. so terminate and start new process (additionally by subprocess or not)
    sys.exit(0)

def add_WD_exclusion_dir(debug):
    script = "powershell -Command Add-MpPreference -ExclusionPath "+os.getcwd()
    #os.system(script)
    subprocess.call(script)
    # if(debug):
    #     print("added curruent dir to Windows Defender Exclusion dir....")
    #     os.system("pause")

def remove_WD_exclusion_dir(debug):
    script='''
        powershell -Command $x=Get-MpPreference
        foreach($i in $x.ExclusionPath){
        Remove-MpPreference -ExclusionPath $i
        }'''
        #os.system(script)
    subprocess.call(script,shell=True)
    if(debug):
        print("added curruent dit to Windows Defender Exclusion dir....")
        os.system("pause")

## test scripts...
run_as_admin()
add_WD_exclusion_dir(debug=False)