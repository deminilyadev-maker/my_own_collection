#!/usr/bin/python

# Copyright: (c) 2026, Ilya Demin
# GNU General Public License v3.0+
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file on a remote host

version_added: "1.0.0"

description:
    - Creates a text file on a remote host.
    - The file path is specified by the C(path) parameter.
    - The file content is specified by the C(content) parameter.

options:
    path:
        description:
            - Path to the text file that should be created.
        required: true
        type: str

    content:
        description:
            - Content that should be written to the file.
        required: true
        type: str

author:
    - Ilya Demin
'''

EXAMPLES = r'''
# Create a text file
- name: Create a text file
  my_namespace.my_collection.my_own_module:
    path: /tmp/my_test.txt
    content: "Hello from my own module"

# Create a text file with multiple lines
- name: Create a text file with multiple lines
  my_namespace.my_collection.my_own_module:
    path: /tmp/example.txt
    content: |
      First line
      Second line
      Third line
'''

RETURN = r'''
path:
    description: Path to the file.
    type: str
    returned: always
    sample: '/tmp/my_test.txt'

content:
    description: Content written to the file.
    type: str
    returned: always
    sample: 'Hello from my own module'
'''

import os

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    # Check mode
    if module.check_mode:
        if not os.path.exists(path):
            result['changed'] = True
        else:
            try:
                with open(path, 'r') as file:
                    current_content = file.read()

                if current_content != content:
                    result['changed'] = True

            except OSError as exc:
                module.fail_json(
                    msg='Unable to read existing file: {}'.format(exc),
                    **result
                )

        module.exit_json(**result)

    # If the file exists, check its current content.
    if os.path.exists(path):
        try:
            with open(path, 'r') as file:
                current_content = file.read()

        except OSError as exc:
            module.fail_json(
                msg='Unable to read existing file: {}'.format(exc),
                **result
            )

        # File already contains the required content.
        if current_content == content:
            module.exit_json(**result)

    # Create or update the file.
    try:
        with open(path, 'w') as file:
            file.write(content)

    except OSError as exc:
        module.fail_json(
            msg='Unable to create or write file: {}'.format(exc),
            **result
        )

    result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()