##############################################################################
# Utilities
##############################################################################

import os
import re
from optparse import OptionParser
import rospkg

##################
# Author
##################

def author_name():
    """
    Utility to compute logged in user name
    
    :returns: name of current user, ``str``
    """
    import getpass
    name = getpass.getuser()
    try:
        import pwd
        login = name
        name = pwd.getpwnam(login)[4]
        name = ''.join(name.split(',')) # strip commas
        # in case pwnam is not set
        if not name:
            name = login
    except:
        #pwd failed
        pass
    if type(name) == str:
        name = name.decode('utf-8')
    return name

##################
# Templates
##################

# Finds and reads one of the templates.
def read_template(tmplf):
    f = open(tmplf, 'r')
    try:
        t = f.read()
    finally:
        f.close()
    return t

# This inserts the labelled variables into the template wherever the corresponding
# %package, %brief, %description %manifest_depends and %cmake_depends is found.
def instantiate_template(template, name, brief, description, author, manifest_depends, cmake_depends):
    return template%locals()


##################
# Names
##################

# These routines are originally from roslib
# Todo: might be nice if they were in rospkg, not here.

BASE_RESOURCE_NAME_LEGAL_CHARS_P = re.compile('^[A-Za-z][\w_]*$') #ascii char followed by (alphanumeric, _)
def is_legal_resource_base_name(name):
    """
    Validates that name is a legal resource base name. A base name has
    no package context, e.g. "String".
    """
    # resource names can be unicode due to filesystem
    if name is None:
        return False
    m = BASE_RESOURCE_NAME_LEGAL_CHARS_P.match(name)
    return m is not None and m.group(0) == name

##################
# Argument Parser
##################

def parse_arguments(extra_depends=[], is_catkin=True):
	"""
	Parse the command line arguments - in format <package-name> [dependencies]".

	This will need to upgrade from optparse to argparse post python 2.7 
	"""
	parser = OptionParser(usage="usage: %prog <package-name> [dependencies...]")
	options, args = parser.parse_args()
	if not args:
		parser.error("You must specify a package name and optionally also list package dependencies")
	package = args[0]
	if type(package) == str:
		package = package.decode('utf-8')
	depends = args[1:] + extra_depends
		
	if not is_legal_resource_base_name(package):
		parser.error("illegal package name [%s]\n\nNames must start with a letter and contain only alphanumeric characters\nand underscores."%package)
	if os.path.exists(os.path.abspath(package)):
		parser.error("%s already exists, aborting"%package)
	
	print "Is_catkin? %r" % is_catkin
	if is_catkin == True: # not able to handle dependency checking
		print("WARNING: no ros environment found, skipping package and dependency checks\n")
	else: # legacy rosbuild, try and handle dependencies
		if not rospkg.get_ros_paths():
			print("WARNING: no ros environment found, skipping package and dependency checks\n")
		else:
			rospack = rospkg.RosPack()
			if package_already_exists(package, rospack): 
				parser.error("package already exists on the ROS_PACKAGE_PATH!")    
			if not rospkg.on_ros_path(package):
				parser.error("current working directory is not on ROS_PACKAGE_PATH!\nPlease update your ROS_PACKAGE_PATH environment variable.\n")    
			if not dependencies_exist(depends, rospack):
			   parser.error("dependency [%s] cannot be found"%d)
	return (package,depends)

def parse_stack_arguments():
    """
    Parse the command line arguments - in format <stack-name> [dependencies]".
    
    This will need to upgrade from optparse to argparse post python 2.7 
    """
    parser = OptionParser(usage="usage: %prog <stack-name> [stack dependencies...]")
    options, args = parser.parse_args()
    if not args:
        parser.error("You must specify a stack name and optionally also list stack dependencies")
    stack = args[0]
    if type(stack) == str:
        stack = stack.decode('utf-8')
    depends = args[1:]
    if not is_legal_resource_base_name(stack):
        parser.error("illegal stack name [%s]\n\nNames must start with a letter and contain only alphanumeric characters\nand underscores."%package)
    if os.path.exists(os.path.abspath(stack)):
        parser.error("%s already exists, aborting"%stack)
    # Could probably check if the stack already exists somewhere first, also dependencies.
    # We'd need rosstack though
    #if not rospkg.get_ros_paths():
        # Common in a catkin environment - you often don't sit in build's env.sh while working.
    #    print("WARNING: no ros environment found, skipping package and dependency checks\n")
    #else:
    #    rospack = rospkg.RosPack()
    #    if package_already_exists(package, rospack): 
    #        parser.error("package already exists on the ROS_PACKAGE_PATH!")    
    #    if not rospkg.on_ros_path(package):
    #        parser.error("current working directory is not on ROS_PACKAGE_PATH!\nPlease update your ROS_PACKAGE_PATH environment variable.\n")    
    #    if not dependencies_exist(depends, rospack):
    #       parser.error("dependency [%s] cannot be found"%d)
    return (stack,depends)

##################
# Checks
##################

def package_already_exists(package, rospack=rospkg.RosPack()):
    try:
        rospack.get_path(package)
    except rospkg.ResourceNotFound:
        return False
    return True
    
def dependencies_exist(depends, rospack=rospkg.RosPack()):
    for d in depends:
        try:
            rospack.get_path(d)
        except rospkg.ResourceNotFound:
            return False
    return True

##################
# Messages
##################

def print_concluding_message(package):
    print "\nPlease edit %s/manifest.xml and mainpage.dox to finish creating your package"%package

def print_concluding_catkin_message(package):
    print "\n***** Important - Update your Stack Info *****\n  1) edit the stack CMakeLists.txt file and add the package subdirectory.\n  2) edit the stack.xml and add your <build_depends> and <depends> tags\n"

