# Salesforce.org Project Cookiecutter Template

This template helps easily create a CumulusCI project for the following use cases:

* Unmanaged Metadata Project
* Standalone Managed Package
* Extension Managed Package
    * Easily build an extension of HEDA or NPSP

# Starting a Project

**You need cookiecutter installed which can be done with:**

`pip install cookiecutter`

**Create your project from the template:**

`cookiecutter https://github.com/SalesforceFoundation/sfdo-package-cookiecutter`

**Create an empty repository in Github and then run the following commands**

```
cd YourProjectName
git init
git add --all
git commit -m "initial project structure"
git remote add origin git@github.com:YourUsernameOrOrg/YourProject
git push --set-upstream origin master
```

# Example: Create a managed extension of HEDA
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

# Example: Create an unmanaged extension of NPSP loading from an existing production org with NPSP installed and customized

**NOTE**: First, log into the existing production org, go to Setup, and search for "Package".  Create a new unmanaged package and add all the custom metadata you want to retrieve to version control to that package.  The examples below assume that package is called TestPackage but it could be any name.

```
$ cookiecutter https://github.com/SalesforceFoundation/sfdo-package-cookiecutter
project_name [TestRepo]: 
package_name [TestPackage]: 
namespace [No namespace]:
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
        api_version: 39.0
    dependencies:
        - github: https://github.com/SalesforceFoundation/HEDAP

$ cd TestRepo
$ git init
$ cci org connect prod
# Browser opens to Salesforce login page to log into the production org

$ cci task run retrieve_src --org prod

$ cci org scratch dev scratch --default
$ cci flow run dev_org
```
