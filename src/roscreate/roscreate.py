
import os
import shutil
from utils import author_name
from utils import read_template
from utils import instantiate_template

##############################################################################
# Template
##############################################################################

def get_ros_text_templates(package, type):
    template_dir = os.path.join(os.path.dirname(__file__),'templates',type) 
    templates = {}
    templates['mainpage.dox'] = read_template(os.path.join(template_dir,'mainpage.dox'))
    templates['CMakeLists.txt'] = read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates['manifest.xml'] = read_template(os.path.join(template_dir,'manifest.xml'))
    if type == 'ros-legacy':
        templates['Makefile'] = read_template(os.path.join(template_dir,'Makefile'))
    return templates

def create_ros_package(package, depends, type):
    
    p = os.path.abspath(package)
    os.makedirs(p) 
    manifest_depends = ''.join(['  <depend package="%s"/>\n'%d for d in depends])
    cmake_depends = ''.join(['%s '%d for d in depends])
    p = os.path.abspath(package)
    templates = get_ros_text_templates(package, type)
    for filename, template in templates.iteritems():
        contents = instantiate_template(template, package, package, package, author_name(), manifest_depends, cmake_depends)
        try:
            p = os.path.abspath(os.path.join(package, filename))
            f = open(p, 'w')
            print "Created package file", p
            f.write(contents)
        finally:
            f.close()
    
def create_ros_catkin_package(package, depends):
    create_ros_package(package, depends, 'ros')

def create_ros_legacy_package(package, depends):
    create_ros_package(package, depends, 'ros-legacy')
