# linux-in-qtcreator

### Status
[![Build Status](https://travis-ci.org/TheMeaningfulEngineer/linux-in-qtcreator.svg?branch=master)](https://travis-ci.org/TheMeaningfulEngineer/linux-in-qtcreator)

# Example usage

```
~/workspace$ git clone https://github.com/torvalds/linux.git
~/workspace/linux$ cd linux
~/workspace/linux$ make clean
~/workspace/linux$ make tinyconfig
~/workspace/linux$ make KBUILD_VERBOSE=1 | tee build.log
~/workspace/linux$ git clone https://github.com/alan-martinovic/linux-in-qtcreator.git
~/workspace/linux$ cp linux-in-qtcreator/prepare_kernel_project.py .
~/workspace/linux$ chmod 755 prepare_kernel_project.py
~/workspace/linux$ ./prepare_kernel_project.py build.log linux
```

* Open project in QtCreator.
  File -> Open File or Project -> ~/workspace/linux/linux.creator

# Future improvements

This was just a proof of concept that has been hacked to get a first functionality working. Suggestions for improvements are welcome in both functional (Example. "It would be cool if it would auto set building kernel modules from Qt creator) as well as implementation wise (Example. "That's not how one uses pytest"). :)


This repository, is released under the [MIT license](LICENSE.txt).
