
import os
import shutil
import utils

##############################################################################
# Template
##############################################################################

def get_text_templates():
    template_dir = os.path.join(os.path.dirname(__file__),'templates','stack') 
    templates = {}
    templates['CMakeLists.txt'] = utils.read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates['stack.xml'] = utils.read_template(os.path.join(template_dir,'stack.xml'))
    return templates

def create_stack():
    
    (stack, depends) = utils.parse_stack_arguments()

    s = os.path.abspath(stack)
    os.makedirs(s) 
    manifest_depends = ''.join(['  <build_depends>%s</build_depends>\n'%d for d in depends])
    cmake_depends = [] # These are currently a bit odd, they're packages
    templates = get_text_templates()
    for filename, template in templates.iteritems():
        contents = utils.instantiate_template(template, stack, stack, stack, utils.author_name(), manifest_depends, cmake_depends)
        try:
            p = os.path.abspath(os.path.join(stack, filename))
            f = open(p, 'w')
            f.write(contents.encode('utf-8'))
            print "Created stack file", p
        finally:
            f.close()

