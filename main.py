#python module for test neural nets v0.1
import math
import random
import logging

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
#       logging & error handling in ALL classes

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
    def __init__(self, parentLayer, ID="nd00"):
        self.ID = ID
        self.parentLayer = partentLayer
        self.sendToList = []
        self.recvFromList = []
        self.activationStack = [0.0]
        self.activationPotential = 0.0
        self.activationThreshold = 5.0
        self.propagationWeight = 1.0
        self.backwardPropagationWeight = 0.1 #dummy value to be dealt with later
        self.propagationNormal = 0.0
        self.propagationBackwardsNormal = 0.0
        self.propSendCount = 0 # counter for number of times this node propagates
        self.propRecvCount = 0 # counter for number of times this node has been
                                # propagated to
        self.relaxationTime = 0 # after node propagates cannot fire for a number
                                # of iterations equal to relaxationTime

    def update_iteration(self):
#       Function to handle iteration update procedure
#       first call connection internal update functions
#       then test to see whether node should propagate or not
        for cntn in xrange(len(sendToList)):
            sendToList[cntc].update_iteration()

        #done this way so that can add in functionality later
        for activation in xrange(len(self.activationStack)):
            if activation > 0:
                self.propagate()
                self.activationStack[activation] = 0


    def create_Connection(self,recvNode):
#        fucntion to create node
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#        self & recvNode
#        output:
#        add connection data to node
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.propagationNormal * len(sendToList)
        self.sendToList.append( [1.0, connection(self, recvNode,
                                        self.generate_Connetion_ID())] )
        self.propagationNormal += 1.0
        self.propagationNormal /= len(sendToList)

    def remove_recvFrom(self, connectionID):
#        remove connection with connectionID from recvFromList
        for cntn in xrange(len(recvFromList)):
            if recvFromList[cntn].ID == connectionID:
                del recvFromList[cntn]


    def remove_sendNode(self,connectionID):
#       remove connection with connectionID from sendToList
        for cntn in xrange(len(sendToList)):
            if sendToList[cntn][1].ID == connectionID
                self.propagationNormal * len(sendToList)
                self.propagationNormal -= sendToList[cntn][0]
                del sendToList[cntc]
                self.propagationNormal /= len(sendToList)


    def propagate(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        node propagates to another node
#        pick a connection and call its propagation function
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        trigger = random.random() * self.propagationNormal #random number used to pick which connection to use
        weightTotal = 0.0
        self.propSendCount += 1 #update counter
        for connection in xrange(len(sendToList)):
            weightTotal += sendToList[connection][0]
            if weightTotal > trigger:
                sendToList[connection][1].initiate_propagation(
                    self.propagationWeight)
                break

    def recieve_propagation(self, sender):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        node recieves propagation, currently a dummy function that calls another
#        function to do the actual work
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #self.self_propagation(sender)

        self.propRecvCount += 1 #update counter
        return

    def self_propagation(self, inputPropagation):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        after other node propagates to this node test whether this node
#        propagates
#       :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.activationPotential += inputPropagation
        #trigger forwards propagationnetwork
        if self.activationPotential >= self.forwardPropagationWeight:
            self.activationStack[0] += 1 # done this way so that if multiple triggers
                                        # in single iteration can maybe do somethin different
        return

    def back_propagate(self):
        #TODO: implement back propagation scheme
        pass

    def _node_maintainance(self, *errors):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#       if send and/or recv lists are empty destroy_self, log any incoming errors
#       if for some reason a connection leads to a non-existent node then destroy
#       that connection.
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #TODO:log inforandom

        #TODO: if error critical stop propgram

        #destroy self
        self.destroy_self()

    def output_state(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input: data about self
#           should call all incoming and outgoing connections to return data about
#           themselves.
#        output:
#           list object that contains the above information
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        state = [self.ID, self.activationThreshold, self.propagtionWeight,
            self.propagationNormal, self.relaxationTime, self.propSendCount,
             self.propRecvCount ]
            outList = []
            inList = []
            for cntn in xrange(len(sendToList)):
                outList.append([sendToList[0] ,sendToList[cntn][1].output_state()])

            state.append(outList)
            del outList

            for cntn in xrange(len(recvFromList)):
                inList.append(recvFromList[cntn].output_state())

            state.append(inList)
            del inList

            return state

    def generate_Connection_ID(self):
        #give a connection a unique id in string format net$lyr$nd$cntn$
        #TODO: change this as can result in  name clashes
        return self.ID + 'cntn' + str(len(sendToList))


    def destroy_self(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        destroy all incoming and outgoing connections then call parent layer to
#        to remove this node, all references to this should then be deleted and
#        garbage collector should be able to do its job
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #first delete incoming and outgoing nodes
        for connection in sendToList:
            try:
                connection.destroy_self()
            except:
                pass

        for connection in recvFromList:
            try:
                connection.destroy_self()
            except:
                pass

        #then call node delete function in parent layer
        try:
            self.parentLayer.delete_node(self.ID)
        except:
            #TODO: add in critical error logging functionality, if this doesnt work
            # something has gone wrong
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
#    receieving nodes?ident
#    the connection also needs to be self maintaining, destroying self in
#    in the event of the recieving node having been previously deleted and hence
#    informing the sending node that propagation failed and to initiate propagation
#    again.
#   TODO: implement extensive error handling
#         add logging functionality
#    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def __init__(self, sendNode, recvNode, ID="cntn00"):
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
#        propCount -- number of times propagated
#        output:
#        internal values should be initialized
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.sendNode = sendNode
        self.recvNode = recvNode
        self.connectionStrength = 1.0
        self.propagationTime = 0
        self.propagationStack = []
        self.ID = ID # string of format net$lyr$nd$cntn$
        self.propCount = 0

    def __repr__(self):
        #defined output of self, should be similar to output state function but
        #nuanced for different conext. primarily output state is to be used for
        #more rigorous diagnostics and may be expanded upon later.
        return self.output_state() # this will do for now but can be expanded upon later

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
        try:
            for stackItem in xrange(len(propagationStack)):
                self.propagationStack[stackItem][0] -= 1
                if self.propagationStack[stackItem][0] <= 0:
                    self.propagate(self.propagationStack[stackItem][1])
                    self.propagationStack.pop(stackItem)
        except Exception as e:
            connection_mainainance(e)


    def initiate_propagation(self,nodePropagationValue):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#        self
#        nodePropagationValue: floating point value represnting propgation value
#        output:
#        appends propagation to stack
#        returns nothing
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.propagationStack.append([self.propagationTime,
                                                nodePropagationValue])
        except Exception as e:
            connection_mainainance(e)


    def propagate(self,nodePropagationValue):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#        nodePropagationValue: floating point value represnting propgation value
#        output:
#        calls associated reciever node's internal update function
#        returns nothing
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::agation
        try:
            self.recvNode.recieve_propagation(nodePropagationValue)
        except Exception as e: #TODO: add error codes, if recvNode does not recieve initiaite
            connection_mainainance(e)           # maintainance function


    def output_state(self, *errors):
#        function to return data about self. should be calledrandom
#        by object above this one, typically the creating node which should then
#        pass the data up the object heirachy.
#       __repr__ should call this function and return this information + more
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:random
#        self
#        output:
#        returns object comprising of:
#        self.ID, sendNode.ID, recvNode.ID, self.connectionStrength,
#        self.propagationTime, self.propCount and  any possible errorsnodes are
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        state  = [self.ID, self.sendNode.ID, self.recvNode.ID,
                self.ConnectionStrength, self.propagationTime, self.propCount]
        for error in errors:
            state.append(error)
        return state

    def _connection_maintainance(self, *errors):
#        this function handles maintainance in the case that any other function
#        throws an exception. typically this means logging error details, raising
#        the error if critical and then destroying the connection by removing all references
#        to it in other scopes.
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input:
#        Error code from other function
#        output:
#        error log, sendNode and recvNode informed of connection removal
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #TODO:log inforandom

        #TODO: if error critical stop propgram

        #destroy self
        self.destroy_self()


    def change_recvID(self):
#        this function is not needed currently but may be needed for future implementation
#        such as mutating one node into two or into a subnetwork or sublayer
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        dummy function not in use
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        pass

    def destroy_self(self):
#        this function exsits to destroy an instance of itself, this is achieved
#        by deleting all reference to this object and letting the garbage collector
#        do its jobrandomagationthat is for a forward
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        input: self
#        output:
#        destroys self and returns none
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        try:
            self.recvNode.remove_connection(self.ID)
            self.sendNode.remove_connection(self.ID)
        except Exception as fatal:
            pass
            #bad stuff has happened terminate the program

class layer(object):
#    object describing layer of nodes. just as nodes contain connections, layers
#    contain nodes
#    should contain layer metadata and series of nodes
#    it should be noted that in place of a node an entire network or even layer
#       can be contained.
    def __init__(self, spawnNumber, parentNetwork, ID="lyr00"):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        internal variables
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.ID = ID
        self.parentNetwork = parentNetwork
        self.nodeList = []
        for spawn in xrange(spawnNumber):
            self.spawn_node()

    def update_iteration(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        iteration component
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        #first update all internal nodes
        for node in xrange(len(self.nodeList)):
            self.nodeList[node].update_iteration()


    def spawn_node(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        create node in layer here
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.nodeList.append(node(self))

    def delete_node(self, nodeID):
        #remove reference to node here
        for node in xrange(len(nodeList)):
            if nodeList[node].ID == nodeID:
                del nodeList[node]

    def destroy_self(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        call all sub nodes to destroy self then call parent network to remove this layer
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        for nodes in xrange(len(self.nodeList)):
            try:
                nodeList[node].destroy_self()
            except Exception as e:
                pass


        try:
            self.parentNetwork.destroy_layer(self.ID)
        except Exception as e:
            pass

    def generate_Node_ID(self):
#       generate ID for sub nodes, net$lyr$nd$cntn$
        #TODO: change this as can result in  name clashes
        return self.ID + 'nd' + str(len(nodeList))


    def output_state(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        output state function
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        state = []
        for node in xrange(len(nodeList)):
            state.append(nodeList[node].output_state())

        return [self.ID, len(nodeList), state]

    def layer_maintainance(self):
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        layer maintainance protocol TODO: implement this
#        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    pass


class metadata(object):
    #dummy object
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

    def __init__(self, inputList, outputList, ID='ntwk00'):

        self.ID = ID
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

    def generate_layer_ID(self):
#       generate ID for sub nodes, net$lyr$nd$cntn$
        #TODO: change this as can result in  name clashes
        return self.ID + 'lyr' + str(len(nodeList))


    def create_new_layer(parameterDefinition, layerLocation=-1):
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
