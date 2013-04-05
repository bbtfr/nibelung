# -*- mode: python -*-
a = Analysis(['app/app.py'],
             pathex=['/home/bbtfr/Workspace/nibelung'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'app'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
