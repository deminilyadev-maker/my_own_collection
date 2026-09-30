# Netology — Custom Ansible Module and Collection

**Student:** Ilya Demin

## Collection

GitHub repository:

[my_own_collection](https://github.com/deminilyadev-maker/my_own_collection)

Collection name: `my_own_namespace.yandex_cloud_elk`

Collection version: `1.0.0`

Collection archive: `my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz`

---

## Step 1. Create `my_own_module.py`

A new `my_own_module.py` file was created in the Ansible virtual environment.

The module was based on the standard Ansible custom module template and then modified according to the task requirements.

## Step 2. Fill the module with the Ansible module structure

The module contains `DOCUMENTATION`, `EXAMPLES`, `RETURN`, `AnsibleModule`, an argument specification, `run_module()`, and `main()`.

## Step 3. Implement the main task

The custom module was modified to create a text file on the remote host.

It accepts two required parameters:

| Parameter | Type | Description |
|---|---|---|
| `path` | string | Path to the text file |
| `content` | string | Content written to the file |

The module checks the existing file and content, creates or updates the file when necessary, and supports check mode.

## Step 4. Local module test

The custom module was tested locally with Ansible and successfully created the requested file.

![Step 4 — Local module test](screenshots/Task4.png)

## Step 5. Single-task playbook

A single-task playbook was created to use the custom module and create `/tmp/my_test.txt` with the content `Hello from my own module`.

## Step 6. Idempotency test

The playbook was executed repeatedly. When the file already contained the requested content, the module did not modify it and returned `changed=0`.

![Step 6 — Idempotency test](screenshots/Task6.png)

## Step 7. Exit the virtual environment

The virtual environment was exited after the initial module testing stage.

## Step 8. Initialize the collection

A new collection was initialized:

```text
my_own_namespace.yandex_cloud_elk
```

Command:

```bash
ansible-galaxy collection init my_own_namespace.yandex_cloud_elk
```

## Step 9. Move the module into the collection

The custom module was moved to:

```text
plugins/modules/my_own_module.py
```

## Step 10. Convert the single-task playbook into a role

The playbook was converted into the `my_own_role` role.

The role uses:

```text
my_own_namespace.yandex_cloud_elk.my_own_module
```

Role defaults:

```yaml
---
path: /tmp/my_test.txt
content: "Hello from my own module"
```

## Step 11. Create a playbook for the role

A playbook was created to use the role through its fully qualified collection name:

```text
my_own_namespace.yandex_cloud_elk.my_own_role
```

The playbook was tested successfully.

## Step 12. Collection documentation and Git repository

The collection documentation was completed and the collection was uploaded to GitHub.

Repository:

https://github.com/deminilyadev-maker/my_own_collection

Collection version:

```text
1.0.0
```

Git tag:

```text
1.0.0
```

## Step 13. Build the collection archive

The collection was packaged using:

```bash
ansible-galaxy collection build
```

Resulting archive:

```text
my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

## Step 14. Create a separate test directory

A separate directory was created for testing the collection from the local archive.

It contains:

```text
collection_test/
├── my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
└── test_role.yml
```

## Step 15. Install the collection from the local archive

The collection was installed using:

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

Installation completed successfully.

![Step 15 — Collection installation](screenshots/Task15.png)

## Step 16. Run the playbook

After installation from the local archive, the playbook was executed to verify that the installed collection works correctly.

The playbook successfully found and executed:

```text
my_own_namespace.yandex_cloud_elk.my_own_role
```

The final execution completed without errors.

![Step 16 — Final playbook execution](screenshots/Task16.png)

---

## Result

The following requirements were completed:

- Custom Ansible module created.
- Module creates and updates a text file using `path` and `content`.
- Module tested locally.
- Single-task playbook created.
- Idempotency verified.
- Ansible collection initialized.
- Custom module moved into the collection.
- Single-task role created.
- Role defaults configured for all module parameters.
- Playbook created for the collection role.
- Collection documentation completed.
- Collection uploaded to GitHub.
- Collection tagged with version `1.0.0`.
- Collection archive created with `ansible-galaxy collection build`.
- Archive and playbook copied to a separate test directory.
- Collection installed from the local archive.
- Playbook successfully executed using the installed collection.

## Submission

**Collection:** https://github.com/deminilyadev-maker/my_own_collection

**Archive:** `my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz`

**Screenshots:** Steps 4, 6, 15 and 16 are included above.
