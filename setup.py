from distutils.core import setup

import sys
sys.path.insert(0, 'src')

from roscreate import __version__

setup(name='roscreate',
      version= __version__,
      packages=['roscreate'],
      package_dir = {'':'src'},
      scripts = ["scripts/roscreate-pkg","scripts/roscreate-legacy-pkg", "scripts/roscreate-comms-pkg", "scripts/roscreate-qt-pkg","scripts/roscreate-qt-legacy-pkg"],
      package_data = {'roscreate': [
           'templates/qt-ros/CMakeLists.txt',
           'templates/qt-ros/src/*.cpp',
           'templates/qt-ros/ui/*.ui',
           'templates/qt-ros/include/PACKAGE_NAME/*.hpp',
           'templates/qt-ros/resources/*.qrc',
           'templates/qt-ros/resources/images/*.png',
           'templates/qt-ros/mainpage.dox',
           'templates/qt-ros/manifest.xml',
           'templates/qt-ros/Makefile',
           'templates/qt-ros-legacy/CMakeLists.txt',
           'templates/qt-ros-legacy/src/*.cpp',
           'templates/qt-ros-legacy/ui/*.ui',
           'templates/qt-ros-legacy/include/PACKAGE_NAME/*.hpp',
           'templates/qt-ros-legacy/resources/*.qrc',
           'templates/qt-ros-legacy/resources/images/*.png',
           'templates/qt-ros-legacy/mainpage.dox',
           'templates/qt-ros-legacy/manifest.xml',
           'templates/qt-ros-legacy/Makefile',
           'templates/ros/CMakeLists.txt',
           'templates/ros/mainpage.dox',
           'templates/ros/manifest.xml',
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
      long_description = open('README.md').read(),
      license = "BSD"
      )

