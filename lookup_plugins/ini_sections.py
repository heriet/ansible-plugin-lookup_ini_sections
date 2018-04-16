# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

DOCUMENTATION = """
      lookup: file
        author: heriet
        short_description: ini sections lookup plugin
        description:
            - This lookup returns dict of INI contents.
        options:
          file:
            description: path(s) of files to read
            required: True
"""

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

try:
    # Python 2
    import ConfigParser as configparser
except ImportError:
    # Python 3
    import configparser


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        ret = []

        if 'file' not in kwargs:
            raise AnsibleError("ini_sections need option file")

        file = kwargs['file']
        display.debug("ini_sections lookup file: %s" % file)

        file_path = self.find_file_in_search_path(variables, 'files', file)
        display.debug("ini_sections lookup file path: %s" % file_path)

        config = configparser.ConfigParser()
        config.read(file_path)
        sections = config.sections()

        for section_name in sections:
            section = {
                'name': section_name,
                'params': dict(config.items(section_name)),
            }
            ret.append(section)

        return ret
