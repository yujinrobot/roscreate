
import os
import utils

##############################################################################
# Template
##############################################################################

def get_text_templates(package, type):
    template_common_dir = os.path.join(os.path.dirname(__file__),'templates','common') 
    template_dir = os.path.join(os.path.dirname(__file__),'templates',type) 
    templates = {}
    templates['mainpage.dox'] = utils.read_template(os.path.join(template_common_dir,'mainpage.dox'))
    templates['CMakeLists.txt'] = utils.read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates['manifest.xml'] = utils.read_template(os.path.join(template_dir,'manifest.xml'))
    templates[os.path.join('msg','Dude.msg')] = utils.read_template(os.path.join(template_dir,'msg','Dude.msg'))
    templates[os.path.join('srv','HelloDude.srv')] = utils.read_template(os.path.join(template_dir,'srv','HelloDude.srv'))
    return templates

def create_comms_package(type):
    
	(package, depends) = utils.parse_arguments(['std_msgs'])
	
	# Make directories
	p = os.path.abspath(package)
	os.makedirs(os.path.join(p,"msg"))
	os.makedirs(os.path.join(p,"srv"))
	print "Created package directories."

	# Text files
	manifest_depends = ''.join(['  <depend package="%s"/>\n'%d for d in depends])
	cmake_depends = ''.join(['%s '%d for d in depends])
	templates = get_text_templates(package, type)
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
    
