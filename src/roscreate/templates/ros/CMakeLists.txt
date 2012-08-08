##############################################################################
# CMake
##############################################################################

# set(CMAKE_VERBOSE_MAKEFILE TRUE)

##############################################################################
# Catkin
##############################################################################

project(%(package)s)
find_package(catkin)
catkin_project(%(package)s)
find_package(ROS REQUIRED COMPONENTS %(cmake_depends)s)

include_directories(${ROS_INCLUDE_DIRS})

##############################################################################
# Binaries
##############################################################################

# An example executable
#add_executable(%(package)s main.cpp)
#target_link_libraries(%(package)s ${ROS_LIBRARIES})
#install(TARGETS %(package)s RUNTIME DESTINATION bin)

# An example library
#add_library(%(package)s mylib.cpp)
#target_link_libraries(%(package)s ${ROS_LIBRARIES})
#install(TARGETS %(package)s DESTINATION lib PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE)
