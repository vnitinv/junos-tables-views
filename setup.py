from setuptools import setup, find_packages
import sys

# parse requirements
req_lines = [line.strip() for line in open(
    'requirements.txt').readlines()]
install_reqs = list(filter(None, req_lines))

setup(
    name="junos-tables-views",
    namespace_packages=['jnpr', 'jnpr.junos', 'jnpr.junos.op'],
    version="0.0.1",
    author="Nitin Kumar",
    author_email="jnpr-community-netdev@juniper.net",
    description=("Junos 'PyEZ' tables/views"),
    license="Apache 2.0",
    keywords="Junos NETCONF networking automation",
    url="http://www.github.com/Juniper/junos-tables-views",
    package_dir={'': 'lib'},
    packages=find_packages('lib'),
    package_data={
        'jnpr.junos.op': ['*/*.yml'],
    },
    install_requires=install_reqs,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: Text Processing :: Markup :: XML'
    ],
)
