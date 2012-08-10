##############################################################################
# CMake
##############################################################################

# set(CMAKE_VERBOSE_MAKEFILE TRUE)

##############################################################################
# Catkin
##############################################################################

project(%(name)s)
find_package(catkin)

# Some other arguments to this function:
#   INCLUDE_DIRS: export include directories
#   LIBRARIES   : export cpp libraries (used to create pkg-config and cmake-config modules)
#   CFG_EXTRAS  : export cmake modules (e.g.CFG_EXTRAS my-module.cmake)
#   DEPENDS     : same as your manifest dependencies (pkg-config, cmake-config again)
catkin_project(%(name)s
  LIBRARIES %(name)s
  INCLUDE_DIRS include
  DEPENDS %(cmake_depends)s
  )

# The following generates ROS_INCLUDE_DIRS and ROS_LIBRARIES for use with cpp targets
find_package(ROS REQUIRED COMPONENTS %(cmake_depends)s)
include_directories(${ROS_INCLUDE_DIRS})

##############################################################################
# Sources
##############################################################################

add_subdirectory(src)

##############################################################################
# Additional Installs
##############################################################################

install(DIRECTORY include/
        DESTINATION include
        FILES_MATCHING PATTERN "*.h" PATTERN "*.hpp"
        PATTERN ".svn" EXCLUDE
        )

install(DIRECTORY launch/
        DESTINATION share/%(name)s/launch
        FILES_MATCHING PATTERN "*.launch"
        PATTERN ".svn" EXCLUDE
        )
        