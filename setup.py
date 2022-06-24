import setuptools
import timecoptracker


setuptools.setup(
    name='timecop-tracker',
    version=timecoptracker.__version__,
    packages=['timecoptracker'],
    license='MIT',
    description = 'Helps you keep your work time sheets on track',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Marek Narozniak',
    author_email = 'marek.yggdrasil@gmail.com',
    install_requires=[''],
    url = 'https://github.com/marekyggdrasil/timecop',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data = {},
    entry_points={
        'console_scripts': [
            'timecop=timecoptracker.timecop:main',
            'dead-man=timecoptracker.deadman:main',
        ],
    },
)
