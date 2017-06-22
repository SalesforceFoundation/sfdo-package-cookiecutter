import re
import sys

project_type = '{{ cookiecutter.project_type }}'

if project_type.endswith('Managed Extension Package'):
    namespace = '{{ cookiecutter.namespace }}'
    if namespace == 'No namespace':
        print ('ERROR: You must provide a namespace to configure a managed extension package')
        sys.exit(1)
