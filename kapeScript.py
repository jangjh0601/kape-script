import os
import os.path
import glob
import shutil

def createFolder(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print('Error: Failed to creat directory. ')

setupapi_extra_dir = os.getcwd() + '\\kapeTarget\\setupapi_log\\'
install_extra_dir = os.getcwd() + '\\kapeTarget\\install_log\\'
appcache_extra_dir = os.getcwd() + '\\kapeTarget\\appcache_log\\'

createFolder(setupapi_extra_dir)
createFolder(install_extra_dir)
createFolder(appcache_extra_dir)

setupapi_path = os.environ['WINDIR'] + '\INF\\'
install_path = os.environ['WINDIR'] + '\\appcompat\\Programs\\Install\\'
appcache_path = os.environ['LOCALAPPDATA'] + '\Packages\\Microsoft.Windows.Search_cw5n1h2txyewy\\LocalState\\DeviceSearchCache\\'

for filename in glob.glob(setupapi_path + 'setupapi.dev.*.log'):
    shutil.copy(filename, setupapi_extra_dir)

for filename in glob.glob(setupapi_path + 'setupapi.dev.log'):
    shutil.copy(filename, setupapi_extra_dir)

for filename in glob.glob(install_path + 'INSTALL_*.txt'):
    shutil.copy(filename, install_extra_dir)

for filename in glob.glob(appcache_path + 'AppCache*.txt'):
    shutil.copy(filename, appcache_extra_dir)

