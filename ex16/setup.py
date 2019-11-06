try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='sorting',
    version='1.0',
    description='3 scripts implementing bubble sort, merge sort and quick sort algorithms',
    author='Mateusz Kanabrocki',
    author_email='mateusz.kanabrocki@gmail.com',
    packages=['sorting'],  #same as name
    install_requires=['pytest'], #external packages as dependencies
    url='https://github.com/mateuszkanabrocki/LMPTHW/sorting',
    download_url='https://github.com/mateuszkanabrocki/LMPTHW/sorting',
    include_package_data=True #include MANIFEST.in file
    # 'py_modules': ['MODULE_NAME'],
    # 'scripts': [],
)

