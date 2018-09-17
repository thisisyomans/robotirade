# RoboTirade

This is a top down, 2D shooter game made with Pygame.\
The downloads for Mac and Windows are ready, and will be available
on the website (whenever that is ready).

Mac: opens up the game window\
Windows: opens up the game windows + a terminal (just leave it open,
it makes it easier for Windows)

NOTE: This is mentioned again later, but the downloads will be zip files, as those
are the only files that contained the propely packaged applications.

NOTE: The game **may not** run smoothly the first time around, because PyInstaller
is nobody's best friend.

## How To Play

W - move character (soldier) upwards\
A - move character (soldier) to left\
S - move character (soldier) downwards\
D - move character (soldier) to right\
Space - shoot missiles\
Mouse - character will shoot missiles in direction of mouse (it acts as your aiming tool)\
Q - press 'Q' at any time to quit the game (or click the 'x' in the top left corner)\
\
NOTE: press 'Q' if you end up losing, restart feature will be added soon!

## How To Download

Go to the website to download a playabe version of the game: Coming Soon!\
Both are compressed as zips, so be sure to uncompress them to get the application.

## Getting Started (for developers)

### Prerequisites/Development Environment (for messing with the code)

What things you need to install/mess with the software and how to install them.
The easiest way to go about this is to clone the repository from here (or from your
own fork) and set up the following things within the directory created from the clone.

#### Python 3

```
Python 3 (Python is a programming language, and this game is written in version 3) - It can be downloaded from its official website (listed below)
```
* [Python 3](https://www.python.org/downloads/)

#### Pygame

```
Pygame is a python library meant for game development.
Note: the following steps will add the Pygame module to your project directory, not your globally on your machine.
Steps:
  1. We're assuming you have pip, as the up to date versions of Python 2 and 3 come with pip, if you don't, a link to the pip website that has instructions will be listed below.
  2. Navigate to your project directory through the command line.
  3. Once you are in your project directory, do one of the following:
    a. If your Python 3 download's environment variable on your machine is python3, type the following into your terminal:
      pip3 install pygame
    b. If your Python 3 download's environment variable on your machine is python, type the following into your terminal:
      pip install pygame
```
* [Pygame](www.pygame.org)
* [Installing pip](https://pip.pypa.io/en/stable/installing/)

#### PyInstaller

```
PyInstaller is a python library used for packaging python scripts as applications/executables.
Note: the following steps will add the PyInstaller module to your project directory, not your globally on your machine.
Steps:
  1. We're assuming you have pip, as the up to date versions of Python 2 and 3 come with pip, if you don't, a link to the pip website that has instructions will be listed below.
  2. Navigate to your project directory through the command line.
  3. Once you are in your project directory, do one of the following:
    a. If your Python 3 download's environment variable on your machine is python3, type the following into your terminal:
      pip3 install pyinstaller
    b. If your Python 3 download's environment variable on your machine is python, type the following into your terminal:
      pip install pyinstaller
```
* [PyInstaller](http://www.pyinstaller.org/)
* [Installing pip](https://pip.pypa.io/en/stable/installing/)

### Installing

A step by step series of examples that tell you how to get a development environment running.\
This is basically just an example of what was in prerequisites.

Note: Install Python 3 before doing any of this (makes life easy)

#### Case 1: Python 3 Environment Variable is python
Setting up the environment:
```
git clone https://github.com/username/repositoryname.git
pip install pygame
pip install pyinstaller
```
Running the game:
```
python game.py
```

#### Case 2: Python 3 Environment Variable is python3
Setting up the environment:
```
git clone https://github.com/username/repositoryname.git
pip3 install pygame
pip3 install pyinstaller
```
Running the game:
```
python3 game.py
```

### Running the tests

Coming soon!

#### Break down into end to end tests

Coming soon!

```
Coming Soon!
```

#### And coding style tests

Coming soon!

```
Coming Soon!
```

### Deployment

Coming soon! (This section will be on how the scripts were packaged into applications)

## Built With

* [Python 3](https://www.python.org/downloads/) - Programming language used to develop the game
* [Pygame](www.pygame.org) - Python module used for sprite handling, images, audio, etc
* [PyInstaller](http://www.pyinstaller.org/) - Python module used for packaging the game

## Contributing

We are currently not accepting contributions.

## Versioning

We use [Git](https://git-scm.com/) and [Github](https://github.com) for versioning.

## Authors

* **Manas Taneja** - *Developer* - [thisisyomans](https://github.com/thisisyomans)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgements

If we open up to contributors, then this section might have some mentions.
