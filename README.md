Roscreate
=========

Template style wizard shortcuts for creating ros packages, stacks.

Roscreate Shortcuts
-------------------

Catkin environment shortcuts

* roscreate-pkg
* roscreate-cpp-pkg
* roscreate-comms-pkg
* roscreate-qt-pkg (use with qt-ros stack)

Legacy environment shortcuts

* roscreate-legacy-pkg
* roscreate-qt-legacy-pkg (use with qt-ros stack)

## Tutorial

This shows how to use the scripts to build a stack/cpp package catkin style. The cpp 
configuration is your typical cpp ros package - it exports some headers, builds a library 
and also a test executable.

### Install Roscreate

It is configured to work on ubuntu precise with the ros fuerte sources.

    > sudo apt-get install python-pip
    > sudo pip install --upgrade roscreate

### Prep Workspace

The following downloads the mingw fuerte rosinstaller. Don't mind the fact that it's the
mingw installer. It is just a minimal set of ros sources that is tagged at a particular
version guaranteed to work with these roscreate shortcuts.

Note that you can also do it working off the apt-get rosinstalled environment (much less building required). I'm doing it from a complete set of sources here, because it lets you easily reference what is going on inside the other catkinized stacks.

    > rosinstall --catkin ~/rosws/src https://raw.github.com/stonier/win_ros/master/mingw_fuerte.rosinstall
    > mkdir -p ~/rosws/build
    > mkdir -p ~/rosws/install
    > cd ~/rosws/build
    > cmake -DCMAKE_INSTALL_PREFIX=~/rosws/install ../src
    > make -j5

### Create Stack/Packages

    > cd ~/rosws/src
    > roscreate-stack foo ros_comm std_msgs
    > cd foo
    > roscreate-cpp-pkg cfoo

We'll also create a dependant test package to make sure headers and libraries are exporting correctly.

    > roscreate-pkg tfoo cfoo
    > cd tfoo

* Create tfoo/main.cpp

```cpp
#include <cfoo/cfoo.hpp>
int main() {
  cfoo::Foo foo;
  foo.helloDude();
  return 0;
}
```

* Edit CMakeLists.txt and uncomment the three lines for the executable example
* Edit ~/rosws/src/foo/stack.xml and add cfoo,tfoo to the subdirectories to be included. Like this:

```
foreach(subdir
    cfoo
    tfoo
    )
    add_subdirectory(${subdir})
endforeach()
```

### Build

    > cd ~/rosws/build
    > cmake .
    > cd foo
    > make -j5

### Run

    > cd ~/rosws/build
    > . env.sh
    > roslaunch cfoo test.launch

Shut down, and then test tfoo which needs libcfoo (don't need a roscore, it is pure c++):

    > cd foo/tfoo/bin
    > ldd tfoo
    > ./tfoo

### Install

    > cd ~/rosws/build/foo/cfoo 
    > make install

## Conclusions

If all works, celebreate with a beer! If not, submit an issue here (even better, create a pull request) and I'll get right to it.
