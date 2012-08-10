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
#   INCLUDE_DIRS: export include directories (typically 'INCLUDE_DIRS include')
#   LIBRARIES   : export cpp libraries (used to create pkg-config and cmake-config modules)
#   CFG_EXTRAS  : export cmake modules (e.g.'CFG_EXTRAS my-module.cmake')
#   DEPENDS     : 
catkin_project(%(name)s
    DEPENDS %(cmake_depends)s
)

# The following generates ROS_INCLUDE_DIRS and ROS_LIBRARIES for use with cpp targets
find_package(ROS REQUIRED COMPONENTS %(cmake_depends)s)
include_directories(${ROS_INCLUDE_DIRS})

##############################################################################
# Binaries
##############################################################################

# An example executable
#add_executable(%(name)s main.cpp)
#target_link_libraries(%(name)s ${ROS_LIBRARIES})
#install(TARGETS %(name)s RUNTIME DESTINATION bin)

# An example library
#add_library(%(name)s mylib.cpp)
#target_link_libraries(%(name)s ${ROS_LIBRARIES})
#install(TARGETS %(name)s DESTINATION lib PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE)
