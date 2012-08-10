##############################################################################
# CMake
##############################################################################

# set(CMAKE_VERBOSE_MAKEFILE TRUE)

##############################################################################
# Catkin
##############################################################################

project(%(name)s)
find_package(catkin)
catkin_project(%(name)s
  INCLUDE_DIRS include
  DEPENDS %(cmake_depends)s
)

include_directories(include)

##############################################################################
# Sources
##############################################################################

add_message_files(
  DIRECTORY msg
  FILES
  Dude.msg
)

add_service_files(
  DIRECTORY srv
  FILES HelloDude.srv
)

generate_messages(DEPENDENCIES std_msgs %(cmake_depends)s)

##############################################################################
# Install
##############################################################################

install(DIRECTORY include/
        DESTINATION include
        FILES_MATCHING PATTERN "*.h"
        PATTERN ".svn" EXCLUDE
        PATTERN ".git" EXCLUDE)



