from setuptools import setup

setup(name='clean-folder',
      version='0.1.0',
      description='Python script for sorting files',
      author='Vladyslav Mytsai',
      license='MIT',
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})
