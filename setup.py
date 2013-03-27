from distutils.core import setup

setup(
    name='furious',
    version='0.1',
    license='Apache',
    description='Furious is a lightweight library that wraps Google App Engine'
                'taskqueues to make building dynamic workflows easy.',
    author='Robert Kluin',
    author_email='robert.kluin@webfilings.com',
    url='http://github.com/WebFilings/furious',
    packages=[
        'furious',
    ],
    classifiers=[
        'Development Status :: 2 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Apache',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)