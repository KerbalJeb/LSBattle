# -*- mode: python -*-
import os, sys
p = '/Users/odakin/Dropbox/Physics/relativity/daiju/LSBattle'
a = Analysis(['LSBattle3D.py'],
             pathex=[p],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
a.datas = []
def add_data(root, to, remove=[]):
    global add_data, a
    lis = os.listdir(root)
    for name in lis:
        full_name = os.path.join(root, name)
        if os.path.isdir(full_name):
            add_data(full_name, os.path.join(to, name), remove)
        elif os.path.isfile(full_name):
            n, ext = os.path.splitext(name)
            if ext in remove:continue
            a.datas += [(os.path.join(to, name), os.path.join(root, name), "DATA")]

for i in ["resources/img", "resources/script", "resources/config"]:
    add_data(os.path.join(p, "", i), i, [".mqo"])

r = ['bz2', 'cPickle', 'openssl']
binaries = []
for i in a.binaries:
        for n in r:
            if n in i[0]:
                break
        else:
            binaries.append(i)
binaries = binaries + [("libSDL2.dylib", os.path.abspath(os.path.join(p, "resources/bin/%s/libSDL2.dylib"%os.name)), 'BINARY')]
a.binaries = binaries
a.zipfiles = []
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='LSBattle3D',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='LSBattle3D')
app = BUNDLE(coll,
             name='LSBattle3D.app',
             icon=None)
