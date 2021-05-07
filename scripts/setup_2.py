from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("scripts/ffmax_2.pyx", 
                              compiler_directives={'language_level' : 3}))
