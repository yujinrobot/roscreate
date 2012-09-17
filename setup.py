from distutils.core import setup

import sys
sys.path.insert(0, 'src')

from roscreate2 import __version__

setup(name='roscreate',
      version= __version__,
      packages=['roscreate2'],
      package_dir = {'':'src'},
      scripts = ["scripts/roscreate-pkg","scripts/roscreate-catkin-pkg","scripts/roscreate-legacy-pkg", "scripts/roscreate-comms-pkg", "scripts/roscreate-qt-pkg","scripts/roscreate-qt-legacy-pkg","scripts/roscreate-stack","scripts/roscreate-cpp-pkg","scripts/roscreate-cpp-ros-pkg",
	             "scripts/roscreate-pkg.bat","scripts/roscreate-catkin-pkg.bat","scripts/roscreate-comms-pkg.bat", "scripts/roscreate-qt-pkg.bat","scripts/roscreate-stack.bat","scripts/roscreate-cpp-pkg.bat","scripts/roscreate-cpp-ros-pkg.bat"],
      package_data = {'roscreate2': [
           'templates/common/mainpage.dox',
           'templates/common/Makefile',
           'templates/common/manifest.xml',
           'templates/qt-ros/CMakeLists.txt',
           'templates/qt-ros/src/*.cpp',
           'templates/qt-ros/ui/*.ui',
           'templates/qt-ros/include/PACKAGE_NAME/*.hpp',
           'templates/qt-ros/resources/*.qrc',
           'templates/qt-ros/resources/images/*.png',
           'templates/qt-ros/manifest.xml',
           'templates/qt-ros-legacy/CMakeLists.txt',
           'templates/qt-ros-legacy/src/*.cpp',
           'templates/qt-ros-legacy/ui/*.ui',
           'templates/qt-ros-legacy/include/PACKAGE_NAME/*.hpp',
           'templates/qt-ros-legacy/resources/*.qrc',
           'templates/qt-ros-legacy/resources/images/*.png',
           'templates/qt-ros-legacy/manifest.xml',
           'templates/ros/CMakeLists.txt',
           'templates/ros/manifest.xml',
           'templates/cpp/CMakeLists.txt',
           'templates/cpp/manifest.xml',
           'templates/cpp/include/PACKAGE_NAME/package_name.hpp',
           'templates/cpp/src/main.cpp',
           'templates/cpp/src/CMakeLists.txt',
           'templates/cpp/src/lib/package_name.cpp',
           'templates/cpp/src/lib/CMakeLists.txt',
           'templates/cpp-ros/CMakeLists.txt',
           'templates/cpp-ros/manifest.xml',
           'templates/cpp-ros/include/PACKAGE_NAME/package_name.hpp',
           'templates/cpp-ros/src/main.cpp',
           'templates/cpp-ros/src/CMakeLists.txt',
           'templates/cpp-ros/src/lib/package_name.cpp',
           'templates/cpp-ros/src/lib/CMakeLists.txt',
           'templates/cpp-ros/launch/test.launch',
           'templates/ros-legacy/CMakeLists.txt',
           'templates/ros-legacy/manifest.xml',
           'templates/comms/CMakeLists.txt',
           'templates/comms/manifest.xml',
           'templates/comms/msg/Dude.msg',
           'templates/comms/srv/HelloDude.srv',
           'templates/stack/CMakeLists.txt',
           'templates/stack/stack.xml',
           ]},
      author = "Daniel Stonier",
      author_email = "d.stonier@gmail.com",
      url = "http://pypi.python.org/pypi/roscreate/",
      download_url = "https://github.com/yujinrobot/roscreate.git",
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License" ],
      description = "Creational templates for RoS",
      long_description = "Refer to the documentation at https://github.com/yujinrobot/roscreate.",
      license = "BSD"
      )

# This no longer works...it has to be a special parsable syntax of pypi's.
#      long_description = open('README.md').read(),

