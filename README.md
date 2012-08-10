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

This shows how to use the scripts to build a stack/cpp package catkin style. It is configured
to work on ubuntu precise with the ros fuerte sources.

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

### Create Stack/Package

    > cd ~/rosws/src
    > roscreate-stack foo ros_comm std_msgs
    > cd foo
    > roscreate-cpp-pkg cfoo

* Edit ~/rosws/src/foo/stack.xml and add cfoo to the subdirectories to be included. Like this:

```
foreach(subdir
    cfoo
    )
    add_subdirectory(${subdir})
endforeach()
```

### Build

    > cd ~/rosws/build
    > cmake .
    > cd foo/cfoo
    > make -j5

### Test

    > cd ~/rosws/build
    > . env.sh
    > roslaunch cfoo test.launch
    > CTRL-C
    > exit

Just making sure to exit here, otherwise we'll get a conflict with ros stack's roscreate-pkg which we use below.

### Install

    > cd ~/rosws/build/foo/cfoo 
    > make install

### Create a dependant package

    > cd ~/rosws/src/foo
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
* Edit foo/CMakeLists.txt and add tfoo to the subdirectories to be added to the build.

Finally build:

    > cd ~/rosws/build
    > cmake .
    > cd foo/tfoo
    > make -j5

Test (don't need a roscore - this is pure c++)

    > cd ~/rows/build/foo/tfoo/bin
    > ./tfoo


## Conclusions

If all works, celebreate with a beer! If not, submit an issue here (even better, create a pull request) and I'll get right to it.
