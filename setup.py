from setuptools import setup

setup(
    name='pyrorouter',
    version='0.1.0',
    description='A simple router for Pyrogram',
    url='https://github.com/tshelter/pyrorouter',
    author='Lukasz Tshipenchko',
    author_email='dev@zxc.sx',
    license="LGPLv3",
    packages=['pyrorouter'],
    python_requires="~=3.7",
    install_requires=["pyrogram"],

    keywords="pyrogram telegram chat messenger mtproto api client library python",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
)
