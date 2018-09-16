import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['numpy.core._methods', 'numpy.lib.format', 'matplotlib.backends.backend_qt5agg','code','appdirs',
         'packaging.version', 'packaging.specifiers', 'packaging.requirements',],
        'excludes': ['gtk', 'PyQt4', 'wx', 'tkinter','setuptools', 'IPython', 'pytz']
    }
}

executables = [
    Executable('SubSub_WAY.py', base=base)
]

setup(name='SubSub_WAY',
      version='2.0',
      description='For FUN NO use.',
      options=options,
      executables=executables
      )
# py setup.py build
# lib里面的zip 放到外面 重命名 python36 并且把txt copy进来就可以