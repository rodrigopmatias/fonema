'''
   Copyright (C) 2017  Bruno Guberfain do Amaral <bruno.do.amaral@gmail.com>

   Released under the terms of the BSD license
  
    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:
  
    1. Redistributions of source code must retain the above copyright notice, this
       list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice, this
       list of conditions and the following disclaimer in the documentation and/or
       other materials provided with the distribution.
  
  
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS' AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
    ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
    ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  
  ***********************************************************************
'''
import os

from setuptools import setup, Extension

c_ext = Extension(
   'fonema', 
   [
      'metaphone_ptbrpy.c',
      os.path.join('src', 'metaphone_ptbr.c'),
   ]
)

setup(
    name='fonema',
    author='Rodrigo Pinheiro Matias',
    author_email='rodrigopmatias@gmail.com',
    description="Simple library, to transform names into phonemes in the Portuguese language of Brazil."
    version='1.0.8',
    ext_modules=[c_ext],
    include_dirs=['.', 'src'],
    url='https://github.com/rodrigopmatias/fonema'
)
