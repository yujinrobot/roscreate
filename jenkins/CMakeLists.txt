##############################################################################
# CMake
##############################################################################

# set(CMAKE_VERBOSE_MAKEFILE TRUE)

##############################################################################
# Catkin
##############################################################################

project(tfoo)
find_package(catkin)

# Some other arguments to this function:
#   INCLUDE_DIRS: export include directories (typically 'INCLUDE_DIRS include')
#   LIBRARIES   : export cpp libraries (used to create pkg-config and cmake-config modules)
#   CFG_EXTRAS  : export cmake modules (e.g.'CFG_EXTRAS my-module.cmake')
#   DEPENDS     : 
catkin_project(tfoo
    DEPENDS cfoo 
)

# The following generates ROS_INCLUDE_DIRS and ROS_LIBRARIES for use with cpp targets
find_package(ROS REQUIRED COMPONENTS cfoo )
include_directories(${ROS_INCLUDE_DIRS})

##############################################################################
# Binaries
##############################################################################

# An example executable
add_executable(tfoo main.cpp)
target_link_libraries(tfoo ${ROS_LIBRARIES})
install(TARGETS tfoo RUNTIME DESTINATION bin)

# An example library
#add_library(tfoo mylib.cpp)
#target_link_libraries(tfoo ${ROS_LIBRARIES})
#install(TARGETS tfoo DESTINATION lib PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE)
