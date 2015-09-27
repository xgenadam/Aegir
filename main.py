#python module for test neural nets
import math
import random
class node(object):
    """
    node object for neural network
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    input:


    output:

    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    """
    def __init__(self, ident):
        self.ident=ident
        self.backwardNodeConnections=[]
        self.forwardNodeConnections=[]
        self.activation=0.0
        self.forwardPropagationWeight=1.0
        self.backwardPropagationWeight=0.1
        self.propagationForwardsNormal=0.0
        self.propagationBackwardsNormal=0.0

    def create_Node(self):
        pass

    def create_prevNode(self, nodeData):
        """
        add to list of node connections that propagate to this node
        """
        nodaData[2] += self.propagationBackwardsNormal
        self.backwardsNodes.append(nodeData)
        self.propationBackwardsNormal += nodeData[2]
        return

    def create_nextNode(self, nodeData):
        """
        add to list of node connections that this node propagates to
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        nodeData[1] += self.propagationForwardsNormal
        self.nextNodes.append(nodeData)
        self.propagationForwardsNormal += nodeData[1]
        return

    def propagate(self,direction):
        """
        node propagates to another node, forwards or backwards
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        #choose random node from next list
        if direction != 'Backwards':
            self.forwards_propagate()
        else:
            self.back_propagate()
        return

    def recieve_propagation(self, sender):
        """
        node recieves propagation, currently a dummy function that calls another
        function to do the actual work
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        self.self_Propagation(sender)
        return

    def self_Propagation(self, inputPropagation):
        """
        after other node propagates to this node test whether this node
        propagates
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        self.activation += inputPropagation
        #trigger forwards propagation
        if self.activation >= self.forwardPropagationWeight:
            self.forward_propagate()
        return

    def back_propagate(self):
        """
        based on weights choose random backwards nodes and propagate to it
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        pass

    def forward_propagate(self):
        import random
        """
        based on weights choose a random forward node and propagate to it
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        trigger = random.random()
        for node in self.forwardNodes:
            if trigger <= node[1]
                #propagate to that node
                pass
        return

class connection(object):
    """
    conection object, is dummy object currently
    """
    pass

class Network(object):
    def __init__(self):
        nodeList=[]
        create_input_layer()
        create_output_layer()
        nodeList.append(inputLayer)
        nodeList.append(outputLayer)


    def create_input_layer():
        """
        create the initial input later
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        pass

    def create_output_layer():
        """
        create the initial output layer
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        pass

    def create_layer():
        """
        create a layer in between input layer and output layer
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        layerHead=0 #need to update this with object that contains layer info
        layer=[layerHead]

        pass

    def increase_complexity():
        """
        function is wip and details will be added later
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        pass

    def print_network():
        """
        function to print network.
        should do this by layer and be recursive for subnetwork case
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        input:


        output:

        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """
        pass
