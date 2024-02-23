from aria_suite.aria_lifecycle.aria_lifecycle_product_payloads import get_aria_lifecycle_environment_details

def dummy_payload():
    #have to update the venter name in aria 
    inputs = {
  "aria_lifecycle": {
    "hostname": "local-vrlcm.seanlab.local",
    "aria_lifecycle_email": "sean.e.gadso@gmail.com",
    "ipAddress": "192.168.1.103",
    "license_key": "5b",
    "deployment_datacenter": {
      "name": "Default-DC",
      "primaryLocation": "Palo Alto;California;US;37.44188;-122.14302"
    },
    "deployment_vcenter": {
      "name": "Default-VC",
      "hostname": "bigdaddykingdom.seanlab.local",
      "username": "administrator@seanlab.local",
      "password": "x9SyJnRR!"
    },
    "aria_enviorments": {
      "name": "aria_enviornment_1",
      "deployment_vcenter_datacenter": "Diversity_Equity_Inclusion_Datacenter",
      "aria_suite_cluster": "Main-Cluster",
      "aria_suite_datastore": "management_domain_datastore",
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
                "ipAddress": "192.168.1.104",
                "hostname": "local-vra.seanlab.local"
              }
            },
            {
              "type": "vrava-secondary",
              "properties": {
                "vmName": "local-vra-02",
                "ipAddress": "192.168.1.106",
                "hostname": "local-vra-02.seanlab.local"
              }
            },
            {
              "type": "vrava-secondary",
              "properties": {
                "vmName": "local-vra-03",
                "ipAddress": "192.168.1.107",
                "hostname": "local-vra-03.seanlab.local"
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
                "vmName": "vrops-master",
                "ipAddress": "192.168.1.94",
                "hostname": "vrops-master.seanlab.local"
              }
            },
            {
              "type": "replica",
              "properties": {
                "vmName": "local-vrops-2",
                "ipAddress": "192.168.1.95",
                "hostname": "vrops-replica.seanlab.local"
              }
            },
            {
              "type": "data",
              "properties": {
                "vmName": "local-vrops-3",
                "ipAddress": "192.168.1.97",
                "hostname": "vrops-data.seanlab.local"
              }
            },
            {
              "type": "remotecollector",
              "properties": {
                "vmName": "local-vrops-3",
                "ipAddress": "192.168.1.96",
                "hostname": "vrops-remotecollector.seanlab.local",
                "deployment_option": "smallrc"
              }
            },
            {
              "type": "cloudproxy",
              "properties": {
                "vmName": "local-vrops-4",
                "ipAddress": "192.168.1.93",
                "hostname": "vrops-lb.seanlab.local",
                "deployment_option": "smallcp"
              }
            }
          ]
        },
        "aria_operations_network": {
          "version": "1.0.0",
          "clusterVIP": "192.168.1.100",
          "nodes": [
            {
              "type": "vrni-platform",
              "properties": {
                "vmName": "vrni-platform",
                "ipAddress": "192.168.1.98",
                "hostname": "vrni-platform.seanlab.local"
              }
            },
            {
              "type": "vrni-collector",
              "properties": {
                "vmName": "vrni-collector",
                "ipAddress": "192.168.1.99",
                "hostname": "vrni-collector.seanlab.local"
              }
            }
          ]
        },
        "aria_operations_logs": {
          "version": "1.0.0",
          "clusterVIP": "192.168.1.93",
          "nodes": [
            {
              "type": "vrli-master",
              "properties": {
                "vmName": "vrli-master",
                "ipAddress": "192.168.1.109",
                "hostname": "vrli-master.seanlab.local"
              }
            },
            {
              "type": "vrli-worker",
              "properties": {
                "vmName": "vrli-workder",
                "ipAddress": "192.168.1.110",
                "hostname": "vrli-workder.seanlab.local"
              }
            }
          ]
        }
      }
    }
  }
}
    return inputs


def create_aria_suite_products(payload, aria_enviornment_name):
    # Create Environment Payload
    get_aria_lifecycle_environment_details(payload, aria_enviornment_name)

    return payload
def main():
    payload = dummy_payload()
    aria_enviornment_name = 'aria_enviornment_1'
    create_aria_suite_products(payload, aria_enviornment_name)


if __name__ == "__main__":
    main()
