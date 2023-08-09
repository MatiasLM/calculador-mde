# -*- mode: python ; coding: utf-8 -*-

BASE_NAME = 'CalculadorMDE'
VERSION = '0.2'
NAME = BASE_NAME + '_' + VERSION
block_cipher = None

a = Analysis([BASE_NAME + '.py'],
             pathex=['D:\\USUARIO\\Documents\\Astronomia\\Astrometria y Fotometria\\GORA\\calculador-mde'],
             binaries=[],
             datas=[('C:\\Users\\Matias\\Anaconda2\\envs\\goratools-plt\\lib\\site-packages\\astroquery\\CITATION', 'astroquery'),
                    ('C:\\Users\\Matias\\Anaconda2\\envs\\goratools-plt\\lib\\site-packages\\colorama','colorama'),
                    ('C:\\Users\\Matias\\Anaconda2\\envs\\goratools-plt\\Lib\\site-packages\\matplotlib','matplotlib'),
                    ('C:\\Users\\Matias\\Anaconda2\\envs\\goratools-plt\\lib\\site-packages\\pyparsing.py','.'),
                    ('C:\\Users\\Matias\\Anaconda2\\envs\\goratools-plt\\lib\\site-packages\\cycler.py','.'),
                    ('C:\\Users\\Matias\\Anaconda2\\envs\\goratools-plt\\lib\\site-packages\\dateutil','dateutil'),
                    ('C:\\Users\\Matias\\Anaconda2\\envs\\goratools-plt\\lib\\site-packages\\kiwisolver.cp35-win_amd64.pyd','.')],
             hiddenimports=['tkinter','simpledialog'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name= NAME,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
