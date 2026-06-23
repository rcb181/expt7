#!/usr/bin/python
#library/first_module.py
from ansible.module_utils.basic import AnsibleModule

module = AnsibleModule(
    argument_spec=dict(
        name=dict(type='str', required=True)
    )
)

module.exit_json(
    changed=False,
    message="Hello " + module.params['name']
)
