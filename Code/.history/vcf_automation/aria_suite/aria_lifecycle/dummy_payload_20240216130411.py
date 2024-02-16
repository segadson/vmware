import json

def dummy_payload():
    inputs = {
  "aria_lifecycle": {
    "hostname": "localhost",
    "ipAddress": "",
    "deployment_datacenter": {
        "name": "Default-VC",
        "primaryLocation": "Palo Alto;California;US;37.44188;-122.14302"
    },
    "deployment_vcenter":{
            "name": "Default-VC",
            "hostname": "bigdaddykingdom.seanlab.local",
            "username": "administrator@seanlab.local",
            "password": "x9SyJnRR!"
    },
    "aria_enviorments":[
        {
            "name": "aria_enviornment_1",
            "aria_suite_cluster": "Main-Cluster",
            "aria_suite_datastore": "Main-Datastore",
            "aria_suite_username": "admin",
            "aria_suite_password": "x9SyJnRR!",
            "deployment_network_properties": {
                    "network_name": "VM Network",
                    "portgroup": "vlan1024",
                    "gateway": "192.168.1.1",
                    "netmask": "255.255.255.0",
                    "domain": "seanlab.local",
                    "searchpath": "seanlab.local"
                    },
            "products": {
              "aria_automation": {
                "version:": "1.0.0",
                "clusterVIP": "",
                "collectorGroups": {
                  "name": "collector-group-1",
                  "operation": "add",
                  "collectors": [
                    {
                      "type": "remotecollector",
                      "name": "aria-suite-3",
                      "ipAddress": "",
                      "deployment_option": "smallrc"
                    },
                    {
                      "type": "cloudproxy",
                      "name": "aria-suite-4",
                      "ipAddress": "",
                      "deployment_option": "smallcp"
                    }
                  ]
                },
                "nodes": [
                  {
                    "type": "vrava-primary",
                    "name": "aria-automation-1",
                    "ipAddress": ""
                  },
                  {
                    "type": "vrava-secondary",
                    "name": "aria-automation-2",
                    "ipAddress": ""
                  },
                  {
                    "type": "vrava-secondary",
                    "name": "aria-automation-3",
                    "ipAddress": ""
                  }
                ]
              },
              "aria_operations": {
                "version": "1.0.0",
                "clusterVIP": "",
                "nodes": [
                  {
                    "type": "master",
                    "name": "aria-suite-1",
                    "ipAddress": ""
                  },
                  {
                    "type": "replica",
                    "name": "aria-suite-2",
                    "ipAddress": ""
                  },
                  {
                    "type": "remotecollector",
                    "name": "aria-suite-3",
                    "ipAddress": "",
                    "deployment_option": "smallrc"
                  },
                  {
                    "type": "cloudproxy",
                    "name": "aria-suite-4",
                    "ipAddress": "",
                    "deployment_option": "smallcp"
                  }
                ]
              },
              "aria_operations_network": {
                "version": "1.0.0",
                "clusterVIP": "",
                "nodes": [
                  {
                    "type": "vrni-platform",
                    "name": "aria-suite-1",
                    "ipAddress": "",
                    "vrni_node_size": "small"
                  },
                  {
                    "type": "vrni-collector",
                    "name": "aria-suite-2",
                    "ipAddress": "",
                    "vrni_node_size": "small"
                  }
                ]
              },
              "aria_operations_logs": {
                "version": "1.0.0",
                "clusterVIP": "",
                "nodes": [
                  {
                    "type": "vrli-master",
                    "name": "aria-suite-1",
                    "ipAddress": ""
                  },
                  {
                    "type": "vrli-worker",
                    "name": "aria-suite-2",
                    "ipAddress": ""
                  }
                ]
              }
            }
        }
    ]
  }
}
    return json.dumps(inputs)