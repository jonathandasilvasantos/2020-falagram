from setuptools import setup, find_packages
setup(
    name="falagram",
    version="0.1",
    py_modules=[
    'falagram.app.entrypoint',
    'falagram.app.utils',
    'falagram.app.validator',
    'falagram.app.search',
    'falagram.commands.history',
    'falagram.commands.chats',
    'falagram.commands.listen',
    'falagram.commands.version',
    'falagram.provider.speech',
    'falagram.provider.composer',
    'falagram.provider.personality'
    ],
    install_requires=[ "sox==1.3.7", "gTTS", "Pyrogram==0.17.1", "click==7.1.2", "pygame"],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "falagram=falagram.app.entrypoint:cli"
        ],
    },
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst", "*.md"]
    },

    author="Jonathan S. Santos",
    author_email="silva.santos.jonathan@gmail.com",
    description="Falagram allows user listen their Telegram chats.",
    keywords="tts telegram memory review speak aloud",
    url="https://github.com/jonathandasilvasantos/falagram",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v.3"
    ]


)
