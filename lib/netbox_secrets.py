from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: netbox_secrets
    short_description: fetch secrets from NetBox
    requirements:
      - pynetbox
    options:
      device:
        description: device name you want to fetch secrets for
        required: True
      secret_name:
        description: name of the secret you want to retrieve
        required: True
      netbox_api:
        description: URL to NetBox
        required: True
        env:
          - name: NETBOX_API
      private_key_file:
        description: path to private key file for secrets authentication
        type: path
        required: True
        env:
          - name: NETBOX_KEY_PATH
      netbox_token:
        description: NetBox API token (read-only)
        required: True
        env:
          - name: NETBOX_TOKEN
"""

EXAMPLES = """
- secret_name: lookup netbox secret
  debug:
    msg: "{{ lookup('netbox_secrets', device=inventory_hostname, secret_name=root) }}
"""

RETURN = """
_raw:
  description: secret value retrieved from NetBox
"""

import os

HAVE_PYNETBOX = False
try:
    import pynetbox
    HAVE_PYNETBOX = True
except ImportError:
    pass

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):

        if not HAVE_PYNETBOX:
            raise AnsibleError("Module pynetbox is not installed")

        self.set_options(direct=kwargs)

        netbox_host = self.get_option('netbox_api')
        token = self.get_option('netbox_token')
        private_key_file = self.get_option('private_key_file')
        secret_name = self.get_option('secret_name')
        device = self.get_option('device')

        nb = pynetbox.api(
            netbox_host,
            private_key_file=private_key_file,
            token=token
        )

        secret = nb.secrets.secrets.get(device=device, name=secret_name).plaintext.split(",")

        return secret
