#python module for test neural nets v0.1
import math
import random

#   code structure:
#       Basic: network contains layers, layers contains nodes
#       Advanced, network contains layers, layers can contain subnetworks and nodes
#       layer should contain metadata regarding nodes and possible sub networks
#
#       each class needs to have a function that prints out information about it
#       as well as this it is necesary to have a graphical representation of
#       the network, this could be achieved by recursive functions.
#           network function returns metadata and calls layers to do same,
#           layers call nodes etc
#
#       TODO: introduce iteration component to strucure simultaneous firings
#
#       nodes and connections:
#           when a node recieves a total sum above a certain threshold it will
#           then propagate to a random node among those it is connected to.
#
#           the node propagated to will be chosen randomly based on a weighted
#           connection. the 'signal' propagated will be based on an internal weight
#           and the connection itself
#               TODO: formulate propagation formula
#
#           TODO: should connections be contained in the netword directly?
#               or does this deserve a class of its own?
#
#       network:
#           network needs to ocntain layers which contain nodes
#           have to have input layer and output layer, hidden layers exist in between
#           network is responsible for creating additional layers
#           should network also be responsible for connections?
#
#
#   current goals:

class node(object): that is for a forward
#    node object for neural network
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#    internal variables:____________________________________________________
#       node identity: unique identifier for node
#       backwardNodeConnections, forwardNodeConnections:
#          list of nodes it propagates to and nodes it propagates from
#       activation: this value gets changed when this node is propagated to
#       activationThreshold: once activation reaches this the node will propagate
#       backwards/forwardsPropagationWeight: value this node propagates by
#       propagationBackwards/ForwardsNormal: total values of forwards/backwards
#          node activation weights, deciding which nodes to fire based on RNG
#       TODO: implement iteration stuff
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#    structure:
#
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def __init__(self, ident):
        self.ident=ident
        self.connectionList=[]
        self.activationPotential=0.0
        self.activationThreshold=5.0
        self.forwardPropagationWeight=1.0
        self.backwardPropagationWeight=0.1
        self.propagationForwardsNormal=0.0
        self.propagationBackwardsNormal=0.0

    def create_Connection(self):
#        fucntion to create node
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def propagate(self):
#        node propagates to another node, forwards or backwards
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def recieve_propagation(self, sender):
#        node recieves propagation, currently a dummy function that calls another
#        function to do the actual work
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.self_Propagation(sender)
        return

    def self_propagation(self, inputPropagation):
#        after other node propagates to this node test whether this node
#        propagates
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#       :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.activationPotential += inputPropagation
        #trigger forwards propagationnetwork
        if self.activationPotential >= self.forwardPropagationWeight:
            self.forward_propagate()
        return

    def back_propagate(self):
#        based on weights choose random backwards nodes and propagate to it
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def forward_propagate(self):
        import random
#        based on weights choose a random forward node and propagate to it
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        trigger = random.random()
        for node in self.forwardNodes:
            if trigger <= node[1]
                #propagate to that node
                pass
        return

    def node_maintainance(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def output_state(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def destroy_self(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

class connection(object):
#   conection object, used to connect nodes
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#    internal variables:________________________________________________________
#    sendID -- node that this connects from
#    recvID -- node that this connects to
#    connection strength -- currently just a placeholder for future implementation
#    connection length --  currently just a placeholder for future implementation
#
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#    structure:_________________________________________________________________
#    when send node intiates propagation along this connection it should trigger
#    an internal change in the recieving node -- typically increasing the internal
#    activation potential.
#    this object should also be able to record itself
#    changing the recieving node should also be possible, though there is currently
#    no need to do this and only exists for potential future use -- i.e multiple
#    receieving nodes?
#    the connection also needs to be self maintaining, destroying self in
#    in the event of the recieving node having been previously deleted and hence
#    informing the sending node that propagation failed and to initiate propagation
#    again.
#
#    TODO: implement itteration stuff
#           current thinking is have stack of propagations, each item in stack has
#           countdown which activates reciever node propagation when 0 is reached
#   TODO: implement extensive error handling
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def __init__(self, sendNode, recvNode):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#        sendNode -- sender node, is type node object
#        recvNode -- reciever node, is type node object
#        connectionStrength -- initiailise to 1.0 (float), currently placeholder
#        propagationTime -- initialise to 0 (integer), delay in iterations between
#                           being called and sending, 0 i son delay, 1 is single
#                           network iteration delay etc
#        propagationStack -- 2D list containing instances of propagation in case of
#                           multiple propagations along pipe
#        output:
#        internal values should be initialized
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.sendNode = sendNode
        self.recvNode = recvNode
        self.connectionStrength = 1.0
        self.propagationTime = 0
        self.propagationStack = []

    def update_iteration(self):
#        function for dealing with networking timestep at connection level
#        reduces propagation countdown on all items in stack and initiates
#        recvNode propagation fucntion when countdown reaches 0 then removes
#        item from propagationStack
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#        self
#        output:
#        returns none
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        for stackItem in xrange(len(propagationStack)):
            self.propagationStack[stackItem][0] -= 1
            if self.propagationStack[stackItem][0] <= 0:
                self.initiate_propagation(
                                    self.propagationStack[stackItem][1])
                self.propagationStack.pop(stackItem)
        return

    def initiate_propagation(self,nodePropagationValue):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#        self
#        nodePropagationValue: floating point value represnting propgation value
#        output:
#        appends propagation to stack
#        returns nothing
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            self.propagationStack.append([self.propagationTime,
                                                nodePropagationValue])
            return

    def propagate(self,nodePropagationValue):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#        nodePropagationValue: floating point value represnting propgation value
#        output:
#        calls associated reciever node's internal update function
#        returns nothing
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.recvNode.recieve_propagation(nodePropagationValue)
        return

    def output_state(self):
#        function to return data about self, in json format? should be called
#        by object above this one, typically the creating node which should then
#        pass the data up the object heirachy.
#       TODO: implement this function
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def connection_maintainance(self):
#        this is the fucntion that handles intenral errors and fallback.
#        this function should also handle maintainance, for instance if the sending
#        node gets deleted this should be automatically delted, otherwise memory
#        leaking will occur.
#        this node should also have the ability to check tht both ends are still
#        in existence, this needs to be done in such as way that it is not dependent
#        on the reciver actually being a node as future functionality may require
#        the connection to go to an entire layer or an entire sub network. this
#        shouldnt be the case but better to be safe now than sorry later
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def change_recvID(self):
#        this function is not needed currently but may be needed for future implementation
#        such as mutating one node into two or into a subnetwork or sublayer
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def destroy_self(self):
#        this function exsits to destroy an instance of itself, this is achieved
#        by deleting all reference to this object
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#        self
#        output:
#        destroys self and returns none
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

class layer(object):
#    object describing layer of nodes.
#    should contain layer metadata and series of nodes
#    it should be noted that in place of a node an entire network or even layer
#       can be contained.
    def __init__(self, spawnNumber):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def spawn_node(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def destroy_self(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def output_state(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def layer_maintainance(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    pass


class metadata(object):
    #dummy object
    pass

class Network(object,Layer):
#   class describing network, is a derived class of layer class
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#    internal variables:____________________________________________________
#
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#    structure:
#
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def __init__(self, inputList, outputList):
        layerList=[]
        create_input_layer(inputList)
        create_output_layer(outputList)


    def create_input_layer(self, inputList):
#        create the initial input later
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def create_output_layer(self, outputList):
#        create the initial output layer
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def create_new_layer(parameterDefinition, layerLocation):
#        create a layer in between input layer and output layer
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def network_maintainance(self):
        #       test network to ensure it can be completed and find any "dead"
        #       nodes where there are no incoming or outgoing connections
        #        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #        input:
        #
        #
        #        output:
        #
        #        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def increase_complexity(self):
#        function is WIP and details will be added later
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def output_state(self):
#        function to ouput self.
#        should do this by layer and be recursive for subnetwork case
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def destroy_self(self):
#        function to destroy self in event this is an empty network
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#
#
#        output:
#
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass
