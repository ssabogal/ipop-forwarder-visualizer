### Forwarder and Visualizer

1. Create and instantiate a CloudLab experiment (Ubuntu 14.04 LTS or later) with a public IPv4 address.

2. Edit main.bash and set the variable ```NODE``` with the connection (in the form ```<username>@<hostname>```) of the experiment.

	```
	nano main.bash
	```

3. Execute the following:

	```
	bash main.bash accept
	bash main.bash source
	bash main.bash forward <recv_port> <forward_port>
	```

	(NOTE: select *any* value for ```<recv_port>``` and ```<forward port>```)
	(NOTE: record the output IPv4 address as ```<IPv4 of node>```)


4. For each IPOP configuration file, set the following flags:

	```
	BaseTopologyManager["use_central_visualizer"] = true
	CentralVisualizer["enabled"] = true
	CentralVisualizer["central_visualizer_addr"] = <IPv4 of node>
	CentralVisualizer["central_visualizer_port"] = <recv_port>
	```

5. Run all IPOP instances

6. Run the visualizer:

	```
	python3 visualizer.py tcp <IPv4 of node> <recv_port> <init_ip4> <nr_nodes> <canvas_sz>
	```

	(i.e. if the IPOP network has 9 nodes between 10.254.0.1 to 10.254.0.9, then ```<init_ip4> = 10.254.0.1``` and ```<nr_nodes> = 9```)