# junos-tables-views
User defined PyEZ tables and views

# INSTALLATION

## PIP

Installation requires Python 2.6 or 2.7 or >=3.4 and associated `pip` tool

Installing from Git is only supported as of now (OS must have git installed).

    pip install git+https://github.com/vnitinv/junos-tables-views

## Example 

````python
from jnpr.junos import Device
from jnpr.junos.op.vnitinv.bgpneighbor import BGPNeighborTable

with Device('host', user='user', passwd='passwrd') as dev:
    bgp = BGPNeighborTable(dev).get()
    for item in bgp:
       print item.neighbor
       print item.state
       print item.type
       print item.flap_count
````

## How to contribute your Table/View
Create a folder at lib/jnpr/junos/op/<github-user-name>
Github user name is preffered as it helps in tracking. Inside this folder copy your .py and .yml files corresponding to tables/views.

# LICENSE

Apache 2.0

# CONTRIBUTORS

Juniper Networks is actively contributing to and maintaining this repo. Please contact jnpr-community-netdev@juniper.net for any queries.

*Contributors:*

[Nitin Kumar](https://github.com/vnitinv)
