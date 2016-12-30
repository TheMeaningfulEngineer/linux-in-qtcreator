# linux-in-qtcreator

### Status
[![Build Status](https://travis-ci.org/TheMeaningfulEngineer/linux-in-qtcreator.svg?branch=master)](https://travis-ci.org/TheMeaningfulEngineer/linux-in-qtcreator)

# Motivation

I've always found that I miss a nice environment for experimenting with the Linux kernel so I can quickly jump 
to macro definitions or variable usages. Grepping from the shell on such a big codebase demotivated me.
Than I saw [a talk](http://google.com) in which Linux as a project was imported into Qt Creator and Eclipse.
The purpose of this script is to simplify the steps for achieving this.

# Example usage

```
~/workspace$ git clone https://github.com/torvalds/linux.git
~/workspace/linux$ cd linux
~/workspace/linux$ make clean
~/workspace/linux$ make tinyconfig
~/workspace/linux$ make KBUILD_VERBOSE=1 | tee build.log
```

* Start Qt Creator

* File -> New File or Project -> Import Project -> Import existing project

* Project name: linux  Location: ~/workspace/linux

* File selection: \< deselect all except README>

* Finish

```
~/workspace/linux$ git clone https://github.com/alan-martinovic/linux-in-qtcreator.git
~/workspace/linux$ cp linux-in-qtcreator/prepare_kernel_project.py .
~/workspace/linux$ chmod 755 prepare_kernel_project.py
~/workspace/linux$ ./prepare_kernel_project.py build.log
```

* Go back to Qt Creator. Only the source files used for the build have been included in the project.

# How it works

The script parses the build log for the used files and populates the Qt creator project config files accordingly.

# Future improvements

This was just a proof of concept that has been hacked to get a first functionality working. Suggestions for improvements are welcome in both functional (Example. "It would be cool if it would auto set building kernel modules from Qt creator) as well as implementation wise (Example. "That's not how one uses pytest"). :)


This repository, is released under the [MIT license](LICENSE.txt).
