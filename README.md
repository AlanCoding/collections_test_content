### Progress testing locally

```
cd content
ansible-playbook -i hosts tsplay.yml 
ERROR! no action detected in task. This often indicates a misspelled module name, or incorrect module path.

The error appears to be in '/Users/alancoding/Documents/repos/collections_test_content/content/tsplay.yml': line 9, column 5, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

  - testmodule:
  - mynamespace.tscoll.testaction:
    ^ here

```

from project root

```
ansible-playbook -i content/hosts content/tsplay.yml 
ERROR! no action detected in task. This often indicates a misspelled module name, or incorrect module path.

The error appears to be in '/Users/alancoding/Documents/repos/collections_test_content/content/tsplay.yml': line 9, column 5, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

  - testmodule:
  - mynamespace.tscoll.testaction:
    ^ here

```

other playbook

```
ansible-playbook -i content/hosts content/rawpathplay.yml 
ERROR! no action detected in task. This often indicates a misspelled module name, or incorrect module path.

The error appears to be in '/Users/alancoding/Documents/repos/collections_test_content/content/rawpathplay.yml': line 4, column 5, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

  tasks:
  - a.mynamespace.mycollection.testmodule:
    ^ here
```

