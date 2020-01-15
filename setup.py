from distutils.core import setup
setup(
    name='PyTopsis',
    packages=['PyTopsis'],
    version='0.1',
    license='MIT',
    description='This is a Python Package implementing Topsis meathod used for multi-criteria decision analysis method',
    author='Shivam Behl',
    author_email='shivambehl123@gmail.com',
    url='https://github.com/shivambehl/PyTopsis',
    keywords=['topsis', 'mcda', 'UCS633', 'TIET'],
    install_requires=[            # I get to this in a second
        'numpy',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Students',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
    ],
)
