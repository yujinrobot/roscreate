
import os
import shutil
import utils

##############################################################################
# Template
##############################################################################

def get_ros_text_templates(type):
    template_common_dir = os.path.join(os.path.dirname(__file__),'templates','common') 
    template_dir = os.path.join(os.path.dirname(__file__),'templates',type) 
    templates = {}
    templates['mainpage.dox'] = utils.read_template(os.path.join(template_common_dir,'mainpage.dox'))
    templates['manifest.xml'] = utils.read_template(os.path.join(template_common_dir,'manifest.xml'))
    templates['CMakeLists.txt'] = utils.read_template(os.path.join(template_dir,'CMakeLists.txt'))
    if type == 'ros-legacy':
        templates['Makefile'] = utils.read_template(os.path.join(template_common_dir,'Makefile'))
    return templates

def create_ros_package(type):
    
	is_catkin=True
	if type == 'ros-legacy':
		is_catkin=False
	(package, depends) = utils.parse_arguments([], is_catkin)
			
	p = os.path.abspath(package)
	os.makedirs(p) 
	manifest_depends = ''.join(['  <depend package="%s"/>\n'%d for d in depends])
	cmake_depends = ''.join(['%s '%d for d in depends])
	p = os.path.abspath(package)
	templates = get_ros_text_templates(type)
	for filename, template in templates.iteritems():
		contents = utils.instantiate_template(template, package, package, package, utils.author_name(), manifest_depends, cmake_depends)
		try:
			p = os.path.abspath(os.path.join(package, filename))
			f = open(p, 'w')
			f.write(contents.encode('utf-8'))
			print "Created package file", p
		finally:
			f.close()
	if type == 'ros-legacy':
		utils.print_concluding_message(package)
	else:
		utils.print_concluding_catkin_message(package)

