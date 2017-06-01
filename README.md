# Salesforce.org Project Cookiecutter Template

This template allows you to easily initialize a CumulusCI project for the following use cases:

* Unmanaged Metadata Project
* Standalone Managed Package
* Extension Managed Package
    * Easily build an extension of HEDA or NPSP

# Installation

You need cookiecutter installed which can be done with:
`pip install cookiecutter`

Create your project from the template:
`cookiecutter https://github.com/SalesforceFoundation/sfdo-package-cookiecutter`

## Publishing to Github

Create an empty repository in Github and then run the following commands

```
cd YourProjectName
git init
git add --all
git commit -m "initial project structure"
git remote add origin git@github.com:YourUsernameOrOrg/YourProject
git push --set-upstream origin master
```

# Example
```
$ cookiecutter https://github.com/SalesforceFoundation/sfdo-package-cookiecutter
project_name [TestRepo]: 
package_name [TestPackage]: 
namespace [No namespace]: testnamespace
api_version [39.0]: 
Select extends:
1 - Standalone Package
2 - HEDA
3 - NPSP
Choose from 1, 2, 3 [1]: 2

$ ls TestRepo/
cumulusci.yml  src/           
$ cat TestRepo/cumulusci.yml 
project:
    package:
        name: TestPackage
        namespace: testnamespace
        api_version: 39.0
    dependencies:
        - github: https://github.com/SalesforceFoundation/HEDAP
```
