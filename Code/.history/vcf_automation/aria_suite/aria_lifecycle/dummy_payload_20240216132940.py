import json

def dummy_payload():
    inputs = {
  "aria_lifecycle": {
    "hostname": "local-vrlcm.seanlab.local",
    "ipAddress": "192.168.1.103",
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
                "clusterVIP": "local-vra-lb.seanlab.local",
                "nodes": [
                  {
                    "type": "vrava-primary",
                    "properties": {
                        "vmName": "local-vra",
                        "ipAddress": "192.168.1.104	",
                        "hostname": "local-vra.seanlab.local"
                    }
                    },
                  {
                    "type": "vrava-secondary",
                    "properties": {
                        "vmName": "local-vra-2",
                        "ipAddress": "192.168.1.106",
                        "hostname": "local-vra-2.seanlab.local"
                  }
                    },
                  {
                    "type": "vrava-secondary",
                    "properties": {
                        "vmName": "local-vra-3",
                        "ipAddress": "local-vra-03.seanlab.local",
                        "hostname": "192.168.1.107"
                  }
                  }
                ]
              },
              "aria_operations": {
                "version": "1.0.0",
                "clusterVIP": "",
                "nodes": [
                  {
                    "type": "master",
                    "properties": {
                        "vmName": "local-vrops",
                        "ipAddress": "",
                        "hostname": "local-vrops.seanlab.local"
                    }
                  },
                  {
                    "type": "replica",
                    "properties": {
                        "vmName": "local-vrops-2",
                        "ipAddress": "",
                        "hostname": "local-vrops-2.seanlab.local"
                    }
                  },
                  {
                      "type": "data",
                        "properties": {
                            "vmName": "local-vrops-3",
                            "ipAddress": "",
                            "hostname": "local-vrops-3.seanlab.local"
                        }
                  }
                  {
                    "type": "remotecollector",
                    "properties": {
                        "vmName": "local-vrops-3",
                        "ipAddress": "",
                        "hostname": "local-vrops-3.seanlab.local",
                        "deployment_option": "smallrc"
                    }
                  },
                  {
                    "type": "cloudproxy",
                    "properties": {
                        "vmName": "local-vrops-4",
                        "ipAddress": "",
                        "hostname": "local-vrops-4.seanlab.local",
                        "deployment_option": "smallcp"
                    }
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