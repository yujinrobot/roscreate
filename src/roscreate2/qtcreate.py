
import os
import shutil
import utils

##############################################################################
# Template
##############################################################################

def get_qt_text_templates(package, type):
    template_common_dir = os.path.join(os.path.dirname(__file__),'templates','common') 
    template_dir = os.path.join(os.path.dirname(__file__),'templates',type) 
    templates = {}
    templates['mainpage.dox'] = utils.read_template(os.path.join(template_common_dir,'mainpage.dox'))
    if type == 'qt-ros-legacy':
        templates['Makefile'] = utils.read_template(os.path.join(template_common_dir,'Makefile'))
    templates['CMakeLists.txt'] = utils.read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates['manifest.xml'] = utils.read_template(os.path.join(template_dir,'manifest.xml'))
    templates[os.path.join('ui','main_window.ui')] = utils.read_template(os.path.join(template_dir,'ui','main_window.ui'))
    templates[os.path.join('src','main.cpp')] = utils.read_template(os.path.join(template_dir,'src','main.cpp'))
    templates[os.path.join('src','main_window.cpp')] = utils.read_template(os.path.join(template_dir,'src','main_window.cpp'))
    templates[os.path.join('src','qnode.cpp')] = utils.read_template(os.path.join(template_dir,'src','qnode.cpp'))
    templates[os.path.join('resources','images.qrc')] = utils.read_template(os.path.join(template_dir,'resources','images.qrc'))
    templates[os.path.join('include',package,'main_window.hpp')] = utils.read_template(os.path.join(template_dir,'include','PACKAGE_NAME','main_window.hpp'))
    templates[os.path.join('include',package,'qnode.hpp')] = utils.read_template(os.path.join(template_dir,'include','PACKAGE_NAME','qnode.hpp'))
    return templates

def create_qt_ros_package(type):
	is_catkin=True
	if type == 'qt-ros-legacy':
		is_catkin=False
	#print "Create qt_ros_package(is_catkin:%r)" % is_catkin
	(package, depends) = utils.parse_arguments(['qt_build','roscpp'], is_catkin)
			
    # Make directories
	p = os.path.abspath(package)
	os.makedirs(os.path.join(p,"src"))
	os.makedirs(os.path.join(p,"include"))
	os.makedirs(os.path.join(p,"include",package))
	os.makedirs(os.path.join(p,"resources"))
	os.makedirs(os.path.join(p,"resources","images"))
	os.makedirs(os.path.join(p,"ui"))
	print "Created qt package directories."

    # Qt text files
	manifest_depends = ''.join(['  <depend package="%s"/>\n'%d for d in depends])
	cmake_depends = ''.join(['%s '%d for d in depends])
	templates = get_qt_text_templates(package, type)
	for filename, template in templates.iteritems():
		contents = utils.instantiate_template(template, package, package, package, utils.author_name(), manifest_depends, cmake_depends)
		try:
			p = os.path.abspath(os.path.join(package, filename))
			f = open(p, 'w')
			f.write(contents.encode('utf-8'))
			print "Created package file", p
		finally:
			f.close()
	# Qt binary files
	template_dir = os.path.join(os.path.dirname(__file__),'templates',type) 
	shutil.copy(os.path.join(template_dir,'resources','images','icon.png'),
				os.path.join(os.path.abspath(package),'resources','images','icon.png'))
	if type == 'qt-ros-legacy':
		utils.print_concluding_message(package)
	else:
		utils.print_concluding_catkin_message(package)
    
    
