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

This shows how to use the scripts to build a stack/cpp package catkin style.

### Prep Workspace

The following downloads the mingw fuerte rosinstaller. Don't mind the fact that it's the
mingw installer. It is just a minimal set of ros sources that is tagged at a particular
version guaranteed to work with these roscreate shortcuts.

Note that you can also do it working off the apt-get rosinstalled environment. I'm 
doing it from sources here, because it lets you easily reference what is going on with other
catkinized stacks.

    rosinstall --catkin /opt/mingw https://raw.github.com/stonier/win_ros/master/mingw_fuerte.rosinstall
    > mkdir build
    > cd build
    > cmake /opt/mingw
    > make -j5

### Create Stack/Package

    > cd /opt/mingw
    > roscreate-stack foo ros_comm std_msgs
    > cd foo
    > roscreate-cpp-pkg cfoo

    
