#python module for test neural nets v0.1
import math
import random
import logging
import traceback


logging.basicConfig(filename='debug.log',level=logging.DEBUG)

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
#
#       nodes and connections:
#           when a node receives a total sum above a certain threshold it will
#           then propagate to all nodes among those it is connected to.
#
#
#
#       network:
#           network needs to ocntain layers which contain nodes
#           have to have input layer and output layer, hidden layers exist in between
#           network is responsible for creating additional layers
#           should network also be responsible for connections?
#
#
#   Completion list:
#       barebones of node and connection classes (they can function)
#
#   MASTER TODO list:
#       more readable function to create connections manually
#       implement json output

class node(object):
    #    node object for neural network
    #    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #    internal variables:____________________________________________________
    #       node identity: unique identifier for node
    #       backwardNodeConnections, forwardNodeConnections:
    #          list of connections it propagates to and connections it propagates from
    #       activation: this value gets changed when this node is propagated to
    #       activationThreshold: once activation reaches this the node will propagate
    #       backwards/forwardsPropagationWeight: value this node propagates by
    #       propagationBackwards/ForwardsNormal: total values of forwards/backwards
    #          node activation weights, deciding which nodes to fire based on RNG
    #       TODO: implement iteration stuff -- done some, want to double check, think
    #               this can be done better.
    #    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #    structure:
    #
    #    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def __init__(self, ID="nd00", parentLayer=None, *args, **kwargs):
        self.ID = ID
        self.parentLayer = parentLayer
        self.sendToList = []
        self.recvFromList = []
        self.activationPotential = 0.0 #this is the value that gets increased when this node is propagated to
        self.activationThreshold = 1.0 #this is the threshold for the node to propagate
        self.propagationWeight = 1.0 #scale the propagation of outgoing connections
        self.propSendCount = 0 # counter
        self.propRecvCount = 0 # counter

    def update_iteration(self):
       #Function to handle iteration update procedure
       #first call incoming connection internal update function
       #then test to see whether node should propagate or not
        try:
            for i, cntn in enumerate(self.recvFromList):
                cntn.update_iteration()

        except Exception as e:
        #this works for now
            logging.debug([traceback.print_stack,e])
        try:
            if self.activationPotential >= self.activationThreshold:
                self.propagate()
                self.activationPotential = 0.0
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def create_connection(self,recvNode, connectionWeight=1.0, *args, **kwargs):
        #fucntion to create node
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #self & recvNode
        #output:
        #add connection data to node
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.sendToList.append(
                        connection(recvNode,
                                    self,
                                    self.generate_Connection_ID(),
                                    connectionWeight) )
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def remove_recvFrom(self, connectionID):
        #remove connection with connectionID from recvFromList
        try:
            for i, cntn in enumerate(self.recvFromList):
                if cntn.ID == connectionID:
                    del self.recvFromList[cntn]
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def remove_sendNode(self,connectionID):
        #remove connection with connectionID from sendToList
        try:
            for cntn, obj in enumerate(sendToList):
                if sendToList[cntn].ID == connectionID:
                    del self.sendToList[cntc]
        except Exception as e:
            logging.debug([traceback.print_stack,e])


    def propagate(self):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #node propagates along all outgoing connections
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.propSendCount += 1 #update counter
            for i, cntn in enumerate(self.sendToList):
                cntn.initiate_propagation(self.propagationWeight)
        except Exception as e:
            logging.debug([traceback.print_stack,e])


    def receive_propagation(self, connectionWeight, sender=None, *args, **kwargs):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #node receives propagation, currently a dummy function that calls another
        #function to do the actual work
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.propRecvCount += 1 #update counter
            self.activationPotential += connectionWeight
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def _node_maintainance(self, *errors):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #if send and/or recv lists are empty destroy_self, log any incoming errors
        #if for some reason a connection leads to a non-existent node then destroy
        #that connection.
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #TODO:log inforandom
        #TODO: if error critical stop propgram
        #destroy self
        self.destroy_self()

    def output_state(self):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input: data about self
        #   should call all incoming and outgoing connections to return data about
        #   themselves.
        #output:
        #   list object that contains the above information
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            state = [self.ID, self.activationThreshold, self.propagationWeight,
                 self.propSendCount, self.propRecvCount ]
            outList = ['output list']
            inList = ['input list']
            for i, cntn in enumerate(self.sendToList):
                outList.append(cntn.output_state())

            state.append(outList)
            del outList

            for i, cntn in enumerate(self.recvFromList):
                inList.append(cntn.output_state())

            state.append(inList)
            del inList

            return state
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def generate_Connection_ID(self):
        #give a connection a unique id in string format net$lyr$nd$cntn$
        #TODO: change this as can result in  name clashes
        try:
            return str(self.ID) + 'cntn' + str(len(self.sendToList))
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def destroy_self(self):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #destroy all incoming and outgoing connections then call parent layer to
        #to remove this node, all references to this should then be deleted and
        #garbage collector should be able to do its job
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #first delete incoming and outgoing nodes
        #for connection in self.sendToList:
        try:
            connection.destroy_self()
        except Exception as e:
            logging.debug([traceback.print_stack,e])

        for connection in self.recvFromList:
            try:
                connection.destroy_self()
            except Exception as e:
                logging.debug([traceback.print_stack,e])

        #then call node delete function in parent layer
        try:
            self.parentLayer.delete_node(self.ID)
        except Exception as e:
            logging.debug([traceback.print_stack,e])

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
    #    receieving nodes?ident
    #    the connection also needs to be self maintaining, destroying self in
    #    in the event of the recieving node having been previously deleted and hence
    #    informing the sending node that propagation failed and to initiate propagation
    #    again.
    #   TODO: error handling and logging
    #    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def __init__(self, recvNode, sendNode=None, ID="cntn00",  connectionWeight=1.0, *args, **kwargs):
    #        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #        input:
    #        sendNode -- sender node, is type node object
    #        recvNode -- receiver node, is type node object
    #        connectionStrength -- initiailise to 1.0 (float), currently placeholder
    #        propagationTime -- initialise to 0 (integer), delay in iterations between
    #                           being called and sending, 0 i son delay, 1 is single
    #                           network iteration delay etc
    #        propagationStack -- 2D list containing instances of propagation in case of
    #                           multiple propagations along pipe
    #        propCount -- number of times propagated
    #        output:
    #        internal values should be initialized
    #        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.sendNode = sendNode
        self.recvNode = recvNode
        recvNode.recvFromList.append(self)
        self.weight = connectionWeight
        self.propagationTime = 0
        self.propagationStack = []
        self.ID = ID # string of format net$lyr$nd$cntn$
        self.propCount = 0

    def __repr__(self):
        #defined output of self, should be similar to output state function but
        #nuanced for different conext. primarily output state is to be used for
        #more rigorous diagnostics and may be expanded upon later.
        try:
            return self.output_state() # this will do for now but can be expanded upon later
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def update_iteration(self):
        #function for dealing with networking timestep at connection level
        #reduces propagation countdown on all items in stack and initiates
        #recvNode propagation fucntion when countdown reaches 0 then removes
        #item from propagationStack
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #self
        #output:
        #returns none
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            for i, stackItem in enumerate(self.propagationStack):
                stackItem[0] -= 1
                if stackItem[0] <= 0:
                    self.propagate(stackItem[1])
                    del stackItem
        except Exception as e:
            logging.debug([traceback.print_stack,e])


    def initiate_propagation(self,nodePropagationValue):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #self
        #nodePropagationValue: floating point value represnting propgation value
        #output:
        #appends propagation to stack
        #returns nothing
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.propagationStack.append([self.propagationTime,
                                        nodePropagationValue * self.weight])
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def propagate(self,nodePropagationValue):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #nodePropagationValue: floating point value represnting propgation value
        #output:
        #calls associated receiver node's internal update function
        #returns nothing
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::agation
        try:
            self.recvNode.receive_propagation(nodePropagationValue)
            self.propCount += 1
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def output_state(self, *errors):
        #function to return data about self. should be calledrandom
        #by object above this one, typically the creating node which should then
        #pass the data up the object heirachy.
        #__repr__ should call this function and return this information + more
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:random
        #self
        #output:
        #returns object comprising of:
        #self.ID, sendNode.ID, recvNode.ID, self.connectionStrength,
        #self.propagationTime, self.propCount and  any possible errorsnodes are
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            state  = [self.ID, self.sendNode.ID, self.recvNode.ID, self.weight,
                    self.propagationTime, self.propCount]
            return state
        except exception as e:
            logging.debug([traceback.print_stack,e])

    def _connection_maintainance(self, *errors):
        #this function handles maintainance in the case that any other function
        #throws an exception. typically this means logging error details, raising
        #the error if critical and then destroying the connection by removing all references
        #to it in other scopes.
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #Error code from other function
        #output:
        #error log, sendNode and recvNode informed of connection removal
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #TODO:log inforandom
        #TODO: if error critical stop propgram

        #destroy self
        self.destroy_self()

    def destroy_self(self):
        #this function exsits to destroy an instance of itself, this is achieved
        #by deleting all reference to this object and letting the garbage collector
        #do its jobrandomagationthat is for a forward
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input: self
        #output:
        #destroys self and returns none
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.recvNode.remove_connection(self.ID)
            self.sendNode.remove_connection(self.ID)
            del self.recvNode
            del self.sendNode
        except Exception as fatal:
            pass
            #bad stuff has happened terminate the program

class layer(object):
    #    object describing layer of nodes. just as nodes contain connections, layers
    #    contain nodes
    #    should contain layer metadata and series of nodes
    #    it should be noted that in place of a node an entire network or even layer
    #       can be contained.
    def __init__(self, spawnNumber, parentNetwork = None, ID="lyr00"):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #internal variables
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.ID = ID
        self.parentNetwork = parentNetwork
        self.nodeList = []
        for spawn in xrange(spawnNumber):
            self.create_node()

    def update_iteration(self):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #iteration component
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        #first update all internal nodes
        try:
            for i, node in enumerate(self.nodeList):
                node.update_iteration()
        except Exception as e:
            logging.debug([traceback.print_stack,e])


    def create_node(self):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #create node in layer here
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.nodeList.append(node(self.generate_Node_ID(), self))
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def delete_node(self, nodeID):
        #remove reference to node here
        try:
            for i, node in enumerate(self.nodeList):
                if node.ID == nodeID:
                    del node
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def destroy_self(self):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #call all sub nodes to destroy self then call parent network to remove this layer
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        for nodes in enumerate(self.nodeList):
            try:
                node.destroy_self()
            except Exception as e:
                logging.debug([traceback.print_stack,e])


        try:
            self.parentNetwork.destroy_layer(self.ID)
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def generate_Node_ID(self):
       #generate ID for sub nodes, net$lyr$nd$cntn$
        #TODO: change this as can result in  name clashes
        return self.ID + 'nd' + str(len(self.nodeList))


    def output_state(self):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #output state function
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            state = []
            for node in enumerate(self.nodeList):
                state.append(node.output_state())

            return [self.ID, len(self.nodeList), state]
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def layer_maintainance(self):
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #layer maintainance protocol TODO: implement this
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

class Network(object):
    #   class describing network, is a derived class of layer class
    #    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #    internal variables:____________________________________________________
    #
    #    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #    structure:
    #
    #    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::random

    def __init__(self, numInputNodes, numOutputNodes, ID='ntwk00', parent=None , *args, **kwargs):

        self.ID = ID
        self.layerList = [None,None]
        self.parent = parent
        self.create_input_layer(numInputNodes) #number of desired nodes for input layer
        self.create_output_layer(numOutputNodes) #number of desired nodes for output layer


    def create_input_layer(self, numNodes=0):
        #create the initial input later
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input: numNodes
        #output: layer object consisting of number of nodes equal to numNodes
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.layerList[0] = layer(numNodes, self, self.ID + 'lyrI')
            self.input = self.layerList[0]
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def create_output_layer(self, numNodes=0):
        #create the initial output layer
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #output:
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.layerList[-1] = layer(numNodes, self, self.ID + 'lyrO')
            self.output = self.layerList[-1]
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def generate_layer_ID(self):
       #generate ID for sub nodes, net$lyr$nd$cntn$
        #TODO: change this as can result in  name clashes
        try:
            return self.ID + 'lyr' + str(len(self.layerList) -1)
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def create_new_layer(self, numNodes, layerLocation=-1):
        #create a layer in between input layer and output layer
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #output:
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.layerList.insert(layerLocation, layer(numNodes, self, self.generate_layer_ID()) )
        except Exception as e:
            logging.debug([traceback.print_stack,e])

    def update_iteration(self):
        #call update functions in all layers
        try:
            for i, layer in enumerate(self.layerList):
                layer.update_iteration()
        except Exception as e:
            logging.debug([traceback.print_stack,e])


    def retina(self, *args, **kwargs):
        #easier way to pass information to the input layer
        try:
            for i, arg in enumerate(args):
                self.input.nodeList[i].receive_propagation(arg)
                # logging.info(str(arg), str(args[arg]))
        except Exception as e:
            logging.debug([traceback.print_stack,e])



    def network_maintainance(self):
        #test network to ensure it can be completed and find any "dead"
        #nodes where there are no incoming or outgoing connections
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #output:
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def output_state(self):
        #function to ouput self.
        #should do this by layer and be recursive for subnetwork case
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #output:
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            state = []
            for layer in xrange(len(self.layerList)):
                state.append( self.layerList[layer].output_state() )
            return [self.ID, len(self.layerList), state]
        except Exception as e:
            loging.debug([traceback,print_stack, e])
    def destroy_self(self):
        #function to destroy self in event this is an empty network
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #input:
        #output:
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass
