import os
from setuptools import setup
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
   README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='conways_game_of_life',
    version='1.0a0',
    packages=find_packages(),

    download_url='',

    install_requires=[ 
                    'docopt',
                    'matplotlib',
                    'numpy',
                    'scipy'

    ],

    entry_points={'console_scripts': [
        'conways=conways_game_of_life.main:main',
        ]
        },

    include_package_data=True,
    #license='MIT License',
    description="",
    zip_safe=False,

    long_description=README,
    long_description_content_type='text/markdown',

    python_requires='>=3.8',

)