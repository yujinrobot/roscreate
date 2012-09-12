
import os
import shutil
import utils

##############################################################################
# Template
##############################################################################

def get_templates(package):
    template_common_dir = os.path.join(os.path.dirname(__file__),'templates','common') 
    template_dir = os.path.join(os.path.dirname(__file__),'templates','cpp-ros') 
    templates = {}
    templates['mainpage.dox'] = utils.read_template(os.path.join(template_common_dir,'mainpage.dox'))
    templates['manifest.xml'] = utils.read_template(os.path.join(template_common_dir,'manifest.xml'))
    templates['CMakeLists.txt'] = utils.read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates[os.path.join('src','main.cpp')] = utils.read_template(os.path.join(template_dir,'src','main.cpp'))
    templates[os.path.join('src','CMakeLists.txt')] = utils.read_template(os.path.join(template_dir,'src','CMakeLists.txt'))
    templates[os.path.join('src','lib',package+'.cpp')] = utils.read_template(os.path.join(template_dir,'src','lib','package_name.cpp'))
    templates[os.path.join('src','lib','CMakeLists.txt')] = utils.read_template(os.path.join(template_dir,'src','lib','CMakeLists.txt'))
    templates[os.path.join('include',package,package+'.hpp')] = utils.read_template(os.path.join(template_dir,'include','PACKAGE_NAME','package_name.hpp'))
    templates[os.path.join('launch','test.launch')] = utils.read_template(os.path.join(template_dir,'launch','test.launch'))
    return templates

def create_cpp_ros_package():

    (package, depends) = utils.parse_arguments(['roscpp','std_msgs'])
    # Make directories
    p = os.path.abspath(package)
    os.makedirs(os.path.join(p,"src"))
    print "Created package directory 'src'"
    os.makedirs(os.path.join(p,"src","lib"))
    print "Created package directory 'src/lib'"
    os.makedirs(os.path.join(p,"include"))
    print "Created package directory 'include'"
    os.makedirs(os.path.join(p,"include",package))
    print "Created package directory 'include/%s'"%package
    os.makedirs(os.path.join(p,"launch"))
    print "Created package directory 'launch'"

    # Text files
    manifest_depends = ''.join(['  <depend package="%s"/>\n'%d for d in depends])
    cmake_depends = ''.join(['%s '%d for d in depends])
    templates = get_templates(package)
    for filename, template in templates.iteritems():
        contents = utils.instantiate_template(template, package, package, package, utils.author_name(), manifest_depends, cmake_depends)
        try:
            p = os.path.abspath(os.path.join(package, filename))
            f = open(p, 'w')
            f.write(contents.encode('utf-8'))
            print "Created package file", p
        finally:
            f.close()
    utils.print_concluding_catkin_message(package)
    
