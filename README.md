# Backup Ubiquiti Networks devices

## Description

This repository shows how to backup configration of Ubiquiti Networks devices with Ansible. The list of devices, as well as the passwords to access them, are pulled from NetBox.

We use native Ansible modules to fetch configuration for each device and store them in `backup/[hostname].cfg`.

The examples here apply to Freifunk Düsseldorf. Please adjust the variables to your installation.

## Requirements

Install Python 3.6 or higher and then the requirements with the following command:

```
pip install --user -r requirements.txt
```

Set an environment variable with the path of our NetBox installation:

```
export NETBOX_API=https://netbox.freifunk-duesseldorf.de
```

Create a [NetBox token](https://netbox.freifunk-duesseldorf.de/user/api-tokens/) and set a environment variable in your shell:

```
export NETBOX_TOKEN=[your token]
```

Finally, create a [NetBox secret key](https://netbox.freifunk-duesseldorf.de/user/user-key/) and put it in a file:

```
export NETBOX_KEY_PATH=[path to your key file]
```

Then you're all set!

## Usage

After changing configuration on a device, run the following command to fetch its configuration:

```
ansible-playbook fetch.yml
```

Then commit the changes in the backup folder to git
