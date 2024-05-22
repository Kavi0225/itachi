from setuptools import setup, find_packages

setup(
    name='sa',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    author='kavi0225',
    author_email='kavi02k25@gmail.com',
    description='find the synonym and antonym for sentence',
    url='https://github.com/Kavi0225/itachi.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.12',
)
