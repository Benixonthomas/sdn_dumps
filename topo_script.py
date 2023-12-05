
from mininet.util import dumpNodeConnections,custom
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.node import RemoteController
import os,subprocess,time,datetime 

class CustomTopology(Topo):
    def build(self):
        # Add 3 hosts and 3 switches
        hosts = [self.addHost('h{}'.format(i + 1)) for i in range(3)]
        switches = [self.addSwitch('s{}'.format(i + 1)) for i in range(3)]
 
        # Add links between hosts and switches
        for i in range(3):
            self.addLink(hosts[i], switches[i])

        # Add links between switches
        self.addLink(switches[0], switches[1])
        self.addLink(switches[1], switches[2])

 

if __name__ == '__main__':

    # Create Mininet topology
    cmd="timeout 30s ryu-manager --observe-links ryu.app.simple_switch_13"
    dt_nw=datetime.datetime.now()
    print(dt_nw)
    fr_dt=dt_nw.strftime("%Y%m%d%H%M%S")
    filename="/home/student/git_repo/sdn_dumps/dumps/ryu_{}.log".format(fr_dt)
    print(filename)
    with open(filename,"w") as log_file:
        cmd1= ["cmd"] + cmd.split() + ["&"]
	ryu_process = subprocess.Popen(cmd,stdout=log_file,stderr=subprocess.STDOUT,stdin=subprocess.PIPE,shell=True,close_fds=True)
    print("Waiting for the controller to start ...")
    time.sleep(10)    
    topo = CustomTopology()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo,controller=c1)
    # Start Mininet network
    net.start()

    # Execute pingall in Mininet CLI
    net.pingAll()
    custom('echo "###### Dump connections ######"')
    dumpNodeConnections(net.hosts)

 

    # Ping between all three hosts

    for i in range(1, 4):

        for j in range(i + 1, 4):

            src = net.get('h{}'.format(i))

            dest = net.get('h{}'.format(j))

            print('Pinging from {} to {}:'.format(src.name, dest.name))

            print(src.cmd('ping -c 3 {}'.format(dest.IP())))

 

    # Stop Mininet network

    net.stop()
    # time.sleep(30)
    print ("Clearing the configs...")
    os.popen("mn -c")
    ryu_process.wait()
