##############################################################################
# CMake
##############################################################################

cmake_minimum_required(VERSION 2.8)
project(%(name)s)

##############################################################################
# Catkin
##############################################################################

# Add other stack dependencies here (space separated package (not stack) list)
find_package(ROS REQUIRED COMPONENTS catkin)
catkin_stack()

##############################################################################
# Python Setup
##############################################################################

# If you have a setup.py for your stack, uncomment this (c.f. ros_comm).

# catkin_python_setup()

# Note: you must call catkin_python_setup() before recursing into subdirs so
# that rostest is available in build-space before anybody calls add_rostest().

##############################################################################
# Build
##############################################################################

#foreach(subdir
#    my_ros_pkg1
#    my_ros_pkg2
#    )
#  add_subdirectory(${subdir})
#endforeach()

##############################################################################
# Install
##############################################################################

# install all manifests
install_matching_to_share(manifest.xml)

install(FILES stack.xml
        DESTINATION share/%(name)s)

