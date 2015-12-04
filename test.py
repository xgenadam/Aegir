#testing for neural network
import unittest
import cbm
import copy
import json


class test_basic_logic_gates(unittest.TestCase):
    #generate basic logic gates and test reason for this is
    def setUp(self):
        #logic gates

        #and gate:
        #first setup network with 2 input nodes and 1 output node
        self.and_gate = cbm.Network(2,1)
        #connect the input layer to the output layer with wieghting 1/2
        self.and_gate.input.nodeList[0].create_connection(
                self.and_gate.output.nodeList[0], 0.5)
        self.and_gate.input.nodeList[1].create_connection(
                self.and_gate.output.nodeList[0], 0.5)


        #or
        self.or_gate =  cbm.Network(2,1)

        self.or_gate.input.nodeList[0].create_connection(
                self.or_gate.output.nodeList[0], 1.0)
        self.or_gate.input.nodeList[1].create_connection(
                self.or_gate.output.nodeList[0], 1.0)


        #xor
        self.xor_gate = cbm.Network(2,1)
        self.xor_gate.create_new_layer(3)
        for retinaNode in self.xor_gate.input.nodeList:
            for hiddenNode in self.xor_gate.layerList[1].nodeList:
                retinaNode.create_connection(hiddenNode, 1.0)

        XorHiddenLayer = self.xor_gate.layerList[1].nodeList
        XorOutputLayer = self.xor_gate.output.nodeList


        XorHiddenLayer[1].activationThreshold = 2.0
        XorHiddenLayer[0].create_connection(XorOutputLayer[0], 1.0)
        XorHiddenLayer[1].create_connection(XorOutputLayer[0], -2)
        XorHiddenLayer[2].create_connection(XorOutputLayer[0], 1.0)

        f = open("xor_network", "w")
        print >> f, json.dumps(self.xor_gate.output_state())

    #first test if and gate works
    def test_and(self):
        #cases:
        #(1,1)->1, (1,0)->0 ,(0,1)->0 ,(0,0)->0
        and_11 = copy.deepcopy(self.and_gate)
        and_10 = copy.deepcopy(self.and_gate)
        and_01 = copy.deepcopy(self.and_gate)
        and_00 = copy.deepcopy(self.and_gate)

        and_11.retina(1.0, 1.0)
        and_10.retina(1.0, 0.0)
        and_01.retina(0.0, 1.0)
        and_00.retina(0.0, 0.0)

        truthTable = []
        and_gates = [and_11, and_10, and_01, and_00]

        #and_11.input.nodeList[0].output_state()

        for gate in xrange(len(and_gates)):
            and_gates[gate].update_iteration()
            truthTable.append(and_gates[gate].output.nodeList[0].propSendCount)

        #assert correct output
        self.assertSequenceEqual(truthTable, [1,0,0,0])



    #then test or gate
    def test_or(self):
        #cases:
        #(1,1)->1, (1,0)->1 ,(0,1)->1 ,(0,0)->0

        or_11 = copy.deepcopy(self.or_gate)
        or_10 = copy.deepcopy(self.or_gate)
        or_01 = copy.deepcopy(self.or_gate)
        or_00 = copy.deepcopy(self.or_gate)

        or_11.retina(1.0, 1.0)
        or_10.retina(1.0, 0.0)
        or_01.retina(0.0, 1.0)
        or_00.retina(0.0, 0.0)


        truthTable = []
        or_gates = [or_11, or_10, or_01, or_00]

        for gate in xrange(len(or_gates)):
            or_gates[gate].update_iteration()
            truthTable.append(or_gates[gate].output.nodeList[0].propSendCount)

        self.assertSequenceEqual(truthTable, [1,1,1,0])

    def test_xor(self):
        xor_11 = copy.deepcopy(self.xor_gate)
        xor_10 = copy.deepcopy(self.xor_gate)
        xor_01 = copy.deepcopy(self.xor_gate)
        xor_00 = copy.deepcopy(self.xor_gate)

        xor_11.retina(1.0, 1.0)
        xor_01.retina(0.0, 1.0)
        xor_10.retina(1.0, 0.0)
        xor_00.retina(0.0, 0.0)

        truthTable = []
        xor_gates = [xor_11, xor_10, xor_01, xor_00]
        for gate in xrange(len(xor_gates)):
            xor_gates[gate].update_iteration()
            truthTable.append(xor_gates[gate].output.nodeList[0].propSendCount)

        self.assertSequenceEqual(truthTable, [0,1,1,0])


    #test all IDs are correct


    #test output state functios

if __name__ == '__main__':
    unittest.main(exit=False)
