import os
import shutil
print()
print()
print('                                  _/_/_/_/    _/_/_/_/    _/      _/')
print('                                 _/      _/  _/      _/    _/  _/')
print('                                _/_/_/_/    _/_/_/_/        _/')
print('                               _/      _/  _/      _/    _/  _/')
print('                              _/      _/  _/_/_/_/    _/      _/')
print()
print('            _/_/_/    _/      _/    _/_/_/_/  _/_/_/_/_/    _/_/_/    _/          _/')
print('         _/      _/  _/      _/  _/              _/      _/      _/  _/_/      _/_/')
print('        _/          _/      _/    _/_/_/        _/      _/      _/  _/  _/  _/  _/')
print('       _/      _/  _/      _/          _/      _/      _/      _/  _/    _/    _/')
print('        _/_/_/      _/_/_/    _/_/_/_/        _/        _/_/_/    _/          _/')
print()
print('                               _/_/           _/_/_/')
print('                                _/         _/      _/')
print('                               _/         _/      _/')
print('                              _/         _/      _/')
print('                           _/_/_/   _/    _/_/_/')
print()
print()
print()
def file_exists_test(fordername):
    if not os.path.exists("custom\\"+fordername):
        print("Error : %s forder not found" % (fordername))
        print("press enter to exit")
        input()
        exit()
if not os.path.exists("custom"):
    print("Error : custom forder not found")
    print("press Enter to exit")
    input()
    exit()
file_exists_test("Clientsettings")
file_exists_test("cursor")
file_exists_test("font")
file_exists_test("particle")
file_exists_test("skybox")
file_exists_test("sound")
def autodata():
    path = os.listdir("C:\\Users\\")
    for i in path:
        path_dir = "C:\\Users\\" + i + "\\AppData\\Local\\Roblox\\"
        if os.path.exists(path_dir):
            winusername = i
    path = os.listdir("C:\\Users\\" + winusername + "\\AppData\\Local\\Roblox\\Versions\\")
    for i in path:
        path_dir = "C:\\Users\\" + winusername + "\\AppData\\Local\\Roblox\\Versions\\" + i + "\\RobloxPlayerLauncher.exe"
        if os.path.exists(path_dir):
            version = i
    return(winusername, version)

def cursor():
    f_name = "09g8zxbl034lncbvx94"
    for f_name in os.listdir('custom\\cursor\\'):
        if f_name.endswith('.png'):
            break
    ut_dir = ("custom\\cursor\\" + f_name)
    if os.path.exists(ut_dir):
        name = ["ArrowCursor.png", "ArrowFarcursor.png", "IBeamCursor.png"]
        for i in name:
            shutil.copyfile(ut_dir, cursordir+"\\"+i)
    else:
        print("Error : cursor file not exists")

def change(ut, cg_dir):
    path = os.listdir("custom\\"+ut+"\\")
    for i in path:
        ut_dir = "custom\\"+ut+"\\" + i
        shutil.copyfile(ut_dir, cg_dir+"\\"+i)

autodata()
winusername, version = autodata()
if not os.path.exists("C:\\Users\\"+ winusername +"\\AppData\\Local\\Roblox\\Versions\\"+ version +"\\RobloxPlayerLauncher.exe"):
    print("RobloxPlayer not exists")
    print("press enter to exit")
    input()
    exit()

maindir     =  "C:\\Users\\"+ winusername +"\\AppData\\Local\\Roblox\\Versions\\"+ version
fontdir     =  maindir + "\\content\\fonts"
cursordir   =  maindir + "\\content\\textures\\Cursors\\KeyboardMouse"
particledir =  maindir + "\\content\\textures\\particles"
skyboxdir   =  maindir + "\\PlatformContent\\pc\\textures\\sky"
soundfile   =  maindir + "\\content\\sounds\\ouch.ogg"

if os.path.exists(maindir + "\\ClientSettings"):
    shutil.rmtree(maindir +  "\\ClientSettings")
shutil.copytree("custom\\ClientSettings", maindir + "\\ClientSettings")
print("ClientSettings has been installed")
if not os.path.exists("custom\\sound\\ouch.ogg"):
    print("Error : ouch.ogg file not exists")
else:
    shutil.copyfile("custom\\sound\\ouch.ogg", soundfile)
    print("sound has been changed")
sky = ["moon.jpg", "sun.jpg"]
for i in sky:
    if os.path.exists(maindir + "\\content\\sky\\" + i):
        os.remove(maindir + "\\content\\sky\\" + i)

print("sun has been removed")
change("skybox", skyboxdir)
print("skybox has been changed")
change("font", fontdir)
print("font has been changed")
cursor()
print("corsur has been changed")
change("particle", particledir)
print("particle has been changed")
print("press enter to exit")
input()
exit()