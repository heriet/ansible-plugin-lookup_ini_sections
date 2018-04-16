# ini_sections Lookup Plugin

[![Build Status](https://travis-ci.org/heriet/ansible-role-lookup_ini_sections.svg?branch=master)](https://travis-ci.org/heriet/ansible-role-lookup_ini_sections)

This plugin provides a lookup plugin to ini sections

## Requirements

ansible >= 2.0

## Example

test.ini

```
# test section 1
[section1]
one=1
two=2
three=3

# test section 2
[section2]
a=b
ccc=ddd
```

playbook

```
- name: My test Play
  hosts: all
  roles:
    - lookup_ini_sections
  tasks
    - debug: msg="{{ lookup('ini_sections', file='test.ini') }}"
```

```
ansible-playbook -i tests/inventory test.yml
```

```
ok: [localhost] => {
    "msg": [
        {
            "name": "section1",
            "params": {
                "one": "1",
                "three": "3",
                "two": "2"
            }
        },
        {
            "name": "section2",
            "params": {
                "a": "b",
                "ccc": "ddd"
            }
        }
    ]
}
```

## License

Apache License 2.0