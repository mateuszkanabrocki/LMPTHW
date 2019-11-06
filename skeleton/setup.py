try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='NAME',
    version='1.0',
    description='DESCRIPTION',
    author='Mateusz Kanabrocki',
    author_email='mateusz.kanabrocki@gmail.com',
    packages=['NAME'],  #same as name
    install_requires=['nose'], #external packages as dependencies
    url='https://github.com/mateuszkanabrocki/LMPTHW/?',
    download_url='https://github.com/mateuszkanabrocki/LMPTHW/?',
    include_package_data=True #include MANIFEST.in file
    # 'py_modules': ['MODULE_NAME'],
    # 'scripts': [],
)
