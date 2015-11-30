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
        print len(self.and_gate.layerList)
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
            and_gates[gate].update_iteration()
            and_gates[gate].update_iteration()
            truthTable.append(and_gates[gate].layerList[1].nodeList[0].propRecvCount)


        and_11.input.nodeList[0].sendToList[0][1]

        self.assertSequenceEqual(truthTable, [1,0,0,0])

    #then test or gate
    def test_or(self):
        pass

    #then test for xor
    def test_xor(self):
        pass

if __name__ == '__main__':
    unittest.main(exit=False)
