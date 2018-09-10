# Nagios Redfish API Integration: Out-of-band (BMC) based Monitoring

[Nagios] (https://www.nagios.org/) is an industry standard for HPC infrastructure monitoring including hosts and associated hardware components, networks, storages, services, and applications. However, there are significant issues with traditional Nagios over all solution including:
* Nagios requires human intervention for the definition and maintenance of remote hosts configurations in Nagios Core. 
* It requires Nagios Remote Plugin Executor (NRPE) on Nagios Server and each monitored remote host. 
* It also mandates Nagios Service Check Acceptor (NSCA) on each monitored remote host.
* And also requires Check specific agents (e.g. SNMP) on each monitored remoted host.

In order to address these issues, I have integrated Distributed Management Task Force (DMTF)’s Redfish API (https://redfish.dmtf.org) with Nagios core. DMTF's Redfish API is an open industry standard specification and schema designed to meet the expectations of end users for simple, modern and secure management of scalable platform hardware. Redfish API is essentially out-of-band protocol which is implemented in baseboard management controller (BMC) of the High Performance Computing (HPC) system. Redfish-based plugins for Nagios will be directly communicating to BMC so it eliminates the requirement of any agent and configuration on remote hosts. Redfish API integration with Nagios is potentially a huge paradigm shift in Nagios based monitoring in terms of:
*	simplifying communication between Nagios server and monitored hosts; and 
*	eliminating computational cost & complexity of running Nagios native protocols (NRPE & NSCA) and other agents (SNMP) on the monitored hosts.