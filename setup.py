from distutils.core import setup
setup(
    name = 'hohoho',         # How you named your package folder (MyLib)
    packages = ['hohoho'],   # Chose the same as "name"
    version = '0.2',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Festive esolang powered by whitespace',   # Give a short description about your library
    author = 'hohoho team',                   # Type in your name
    author_email = 'hohoho@nomail.com',      # Type in your E-Mail
    url = 'https://github.com/crnbrdrck/hohoho',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/crnbrdrck/hohoho/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['esolang', 'whitespace', 'festive'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'whitespace',
    ],
    entry_points = {'console_scripts': ['hohoho = hohoho:main']},
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
