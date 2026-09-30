# Ansible Collection - my_own_namespace.yandex_cloud_elk

Ansible collection containing a custom Ansible module and role for creating and managing a text file on a remote host.

## Collection information

- Namespace: `my_own_namespace`
- Collection: `yandex_cloud_elk`
- Version: `1.0.0`
- Author: Ilya Demin

## Requirements

- Ansible
- Python 3
- Linux target host

## Collection structure

    my_own_namespace/
    └── yandex_cloud_elk/
        ├── docs/
        ├── meta/
        ├── plugins/
        │   └── modules/
        │       └── my_own_module.py
        ├── roles/
        │   └── my_own_role/
        │       ├── defaults/
        │       │   └── main.yml
        │       ├── tasks/
        │       │   └── main.yml
        │       ├── handlers/
        │       ├── meta/
        │       ├── files/
        │       ├── templates/
        │       ├── tests/
        │       └── vars/
        ├── galaxy.yml
        ├── README.md
        └── test_role.yml

## Custom module

The collection provides the `my_own_module` custom Ansible module.

The module creates a text file on the remote host or updates an existing file when its content differs from the requested content.

### Module parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `path` | string | Yes | Path to the file that should be created or updated |
| `content` | string | Yes | Content that should be written to the file |

### Module example

    ---
    - name: Create a text file
      hosts: localhost
      connection: local
      gather_facts: false

      tasks:
        - name: Create test file
          my_own_namespace.yandex_cloud_elk.my_own_module:
            path: /tmp/my_test.txt
            content: "Hello from my own module"

## Idempotency

The module is idempotent.

If the requested file already exists and contains the specified content, the module does not modify the file.

The second execution returns:

    changed=0

If the file does not exist or its content differs from the requested content, the module creates or updates the file and returns:

    changed=1

## Check mode

The module supports Ansible check mode.

Example command:

    ansible-playbook -i localhost, -c local test_role.yml --check

In check mode the module checks whether the requested state differs from the current state without modifying the file.

## Role

The collection provides the `my_own_role` role.

The role uses the custom `my_own_module` module to create or update a text file.

### Role defaults

The role defines the following default variables in `roles/my_own_role/defaults/main.yml`:

    ---
    path: /tmp/my_test.txt
    content: "Hello from my own module"

### Role variables

| Variable | Default value | Description |
|---|---|---|
| `path` | `/tmp/my_test.txt` | Path to the file |
| `content` | `Hello from my own module` | File content |

### Using the role

The role can be used with its fully qualified collection name:

    ---
    - name: Test my own role
      hosts: localhost
      connection: local
      gather_facts: false

      roles:
        - my_own_namespace.yandex_cloud_elk.my_own_role

The role variables can be overridden:

    ---
    - name: Test my own role
      hosts: localhost
      connection: local
      gather_facts: false

      vars:
        path: /tmp/example.txt
        content: "Hello from the collection role"

      roles:
        - my_own_namespace.yandex_cloud_elk.my_own_role

## Testing

The collection role was tested locally using:

    ANSIBLE_COLLECTIONS_PATHS=/tmp/ansible_collections ansible-playbook -i localhost, -c local test_role.yml

Successful execution:

    TASK [my_own_namespace.yandex_cloud_elk.my_own_role : Create test file using custom module]
    ok: [localhost]

    PLAY RECAP
    localhost : ok=1 changed=0 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0

The `changed=0` result confirms that the module does not make unnecessary changes when the file already contains the requested content.

## Building the collection

The collection can be built from the collection root directory:

    ansible-galaxy collection build

The command creates an archive similar to:

    my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz

## Installing the collection

The built collection can be installed using:

    ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz

## License

MIT