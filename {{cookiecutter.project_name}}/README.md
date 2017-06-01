# {{cookiecutter.package_name}}

{% if cookiecutter.namespace %}
`src` holds the metadata source for the managed package {{cookiecutter.package_name}}
**Namespace**: {{cookiecutter.namespace}}
{% else %}
`src` holds unmanaged metadata
{% endif %}

{% if cookiecutter.extends != 'Standalone' %}
# Dependencies

This project extends [{{cookiecutter.extends}}](https://github.com/SalesforceFoundation/{% if cookiecutter.extends == 'HEDA' %}HEDAP{% elif cookiecutter.extends == 'NPSP' %}Cumulus{% endif %}) and inherits the dependencies from its `cumulusci.yml` file
{% endif %}


# Deploying to a Salesforce Org

## Prerequisites

* A local git clone of this repostory
* **CumulusCI**: This project is configured for use with [CumulusCI](http://cumulusci.readthedocs.io) which you will need to have installed and configured locally.  The `cci` command should be available in your local environment.

## Useful Build Commands

`cci flow run dev_org`
completely configures a development org for the project

`cci flow run ci_feature`
Deploys the all dependencies and unmanaged metadata and runs all Apex tests

`cci flow run ci_master --org packaging`
Deploys the all dependencies and metadata to the packaging org to prepare for managed package version upload

`cci flow run release_beta --org packaging`
Uploads a managed beta version of the package metadata currently in the packaging org and creates a Github Release

`cci flow run install_beta`
Installs all dependencies and the latest beta release

`cci flow run install_prod`
Installs all dependencies and the latest production release

