import subprocess, setuptools

from distutils.core import setup
from setuptools.command.install import install

version='1.0.1'

class Installer(install):
    def run(self):
        install.run(self)
        subprocess.run(['pyinstaller', '--onefile', 'app.spec'])

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='TrydRPC',
    version=version,
    description='Discord Rich Presence for Tryd plataform',
    download_url='https://github.com/Useems/TrydRPC/archive/'+version+'.tar.gz',
    url='https://github.com/Useems/TrydRPC',
    author='Marcos André',
    author_email='marcos@outlook.in',
    keywords=['tryd', 'trydrpc'],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires = required,
    cmdclass={
        'install': Installer,
    }
)