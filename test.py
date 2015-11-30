#testing for neural network
import unittest
import cbm
import copy




class test_basic_logic_gates(unittest.TestCase):
    #generate basic logic gates and test reason for this is
    def setUp(self):
        #logic gates

        #and gate:
        #first setup network with 2 input nodes and 1 output node
        self.and_gate = cbm.Network(2,1)
        #connect the input layer to the output layer with wieghting 1/2
        self.and_gate.layerList[0].nodeList[0].create_connection(
                self.and_gate.layerList[1].nodeList[0], 0.5)
        self.and_gate.layerList[0].nodeList[1].create_connection(
                self.and_gate.layerList[1].nodeList[0], 0.5)


        #or
        self.or_gate =  cbm.Network(2,1)

        self.or_gate.layerList[0].nodeList[0].create_connection(
                self.or_gate.layerList[1].nodeList[0], 1.0)
        self.or_gate.layerList[0].nodeList[1].create_connection(
                self.or_gate.layerList[1].nodeList[0], 1.0)



        #xor
        #xor_gate = Network(2,1)
        #or is special in that it needs a hidden layer
        #xor_gate


    #first test if and gate works
    def test_and(self):
        #cases:
        #(1,1)->1, (1,0)->0 ,(0,1)->0 ,(0,0)->0
        and_11 = copy.deepcopy(self.and_gate)
        and_11.layerList[0].nodeList[0].receive_propagation(1.0)
        and_11.layerList[0].nodeList[1].receive_propagation(1.0)

        and_10 = copy.deepcopy(self.and_gate)
        and_10.layerList[0].nodeList[0].receive_propagation(1.0)
        and_10.layerList[0].nodeList[1].receive_propagation(0.0)


        and_01 = copy.deepcopy(self.and_gate)
        and_01.layerList[0].nodeList[0].receive_propagation(0.0)
        and_01.layerList[0].nodeList[1].receive_propagation(1.0)


        and_00 = copy.deepcopy(self.and_gate)
        and_00.layerList[0].nodeList[0].receive_propagation(0.0)
        and_00.layerList[0].nodeList[1].receive_propagation(0.0)

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
        or_11.input.nodeList[0].receive_propagation(1.0)
        or_11.input.nodeList[1].receive_propagation(1.0)

        or_10 = copy.deepcopy(self.or_gate)
        or_10.input.nodeList[0].receive_propagation(1.0)
        or_10.input.nodeList[1].receive_propagation(0.0)

        or_01 = copy.deepcopy(self.or_gate)
        or_01.input.nodeList[0].receive_propagation(0.0)
        or_01.input.nodeList[1].receive_propagation(1.0)

        or_00 = copy.deepcopy(self.or_gate)
        or_00.input.nodeList[0].receive_propagation(0.0)
        or_00.input.nodeList[1].receive_propagation(0.0)

        truthTable = []
        or_gates = [or_11, or_10, or_01, or_00]

        for gate in xrange(len(or_gates)):
            or_gates[gate].update_iteration()
            truthTable.append(or_gates[gate].output.nodeList[0].propSendCount)

        self.assertSequenceEqual(truthTable, [1,1,1,0])


    #then test for xor
    # def test_xor(self):
    #     pass

    #test all IDs are correct


    #test output state functios

if __name__ == '__main__':
    unittest.main(exit=False)
