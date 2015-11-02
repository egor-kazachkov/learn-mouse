# learn-mouse

Learn basic mouse usage. For children 2-3 years old.

Simple python script with use of Tcl/Tk to help children learn use of mouse in a simple and fun way.

Caution! With appropriate choice of pictures could be addictive even for adults :)


## Setup
You need Python (tested on Python 2.7.6) and Tcl/Tk (with headers) installed. Also you will need PIL library for Python (this is outdated) or Pillow (which is more up-to-date fork of PIL). I used 

```
sudo pip install https://pypi.python.org/packages/source/P/Pillow/Pillow-3.0.0.zip#md5=dd81f6cc3f3a5e5fe72f0f1d936339c3
```

Then you need to create images folder along with learn-mouse.py script and get some pictures here. I just googled images of whatever animal my children ask. Make sure the images are not too small - so it should be relatively easy to mouse over them - and not too large to take half the screen.




## How to run and play

It has two modes: moving and clicking. Script randomly shows an image from a directory. My daughers prefer various animals but could be anything. Image disappear with some "bang!" if child manage to mouse over (for moving mode) or point and click image (for clicking mode).


