# learn-mouse

Learn basic mouse usage. For children 2-3 years old.

Simple python script with use of Tcl/Tk to help children learn use of mouse in a simple and fun way.

Caution! With appropriate choice of pictures could be addictive even for adults :)


## Setup
You need Python (tested on Python 2.7.6) and Tcl/Tk (with headers) installed. Also you will need PIL library for Python (this is outdated) or Pillow (which is more up-to-date fork of PIL). I used 

```
sudo pip install https://pypi.python.org/packages/source/P/Pillow/Pillow-3.0.0.zip#md5=dd81f6cc3f3a5e5fe72f0f1d936339c3
```

Then you need to create images folder along with learn-mouse.py script and put some pictures there. I just googled images of whatever animal my children ask. Make sure the images are not too small - so it should be relatively easy to mouse over them - and not too large to take half the screen.

Also you may need to tune names of modes which appear on buttons when you start script (they are in Russian). And set command line player and list of audio files you want to use on success acction. Defaults in script are available on Ubuntu 14.04, so for other system you probably have to change them.


## How to run and play

just run the script:

```
python learn-mouse.py
```

It has two modes: moving and clicking. You can choose mode by after start by clicking appropriate button. To change mode, just close window (any key will do) and run script again. 

Script randomly shows an image from a directory. Image disappear with some "bang!" if player manages to mouse over (for moving mode) or point and click image (for clicking mode).

Have fun!


