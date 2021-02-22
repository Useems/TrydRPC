# -*- mode: python ; coding: utf-8 -*-

a = Analysis(['./src/main.py'],
	pathex=[],
	binaries=[],
	datas=[
		('assets/app.ico', 'assets')
	],
	hiddenimports=[
		'pystray._win32'
	],
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=None,
	noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data,
	cipher=None
)

exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas, [],
	name='trydrpc.exe',
	debug=False,
	bootloader_ignore_signals=False,
	strip=False,
	upx=True,
	upx_exclude=[],
	runtime_tmpdir=None,
	console=False,
	icon='assets/app.ico'
)
