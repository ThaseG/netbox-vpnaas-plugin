from setuptools import find_packages, setup

setup(
    name='netbox-vpnaas-plugin',
    version='0.1.0',
    description='A comprehensive NetBox plugin that provides VPN-as-a-Service capabilities',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Andrej Hyben',
    author_email='andrej@hyben.net',
    url='https://github.com/ThaseG/netbox-vpnaas-plugin',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.10',
    install_requires=[
        'Django>=4.2',
        'netbox>=4.0.0',
    ],
    zip_safe=False,
)