

import os
import sys
import logging as log
from openvino.inference_engine import IENetwork, IECore



class Network:
    """
    Load and configure inference plugins for the specified target devices 
    and performs synchronous and asynchronous modes for the specified infer requests.
    """

    def __init__(self):
        ### TODO: Initialize any class variables desired ###
        self.plugin = None
        self.network = None
        self.input_blob = None
        self.output_blob = None
        self.exec_network = None
        self.infer_request = None

    
    def load_model(self, model, CPU_EXTENSION, DEVICE, console_output= False):
        ### TODO: Load the model ###
        model_xml = model
        model_bin = os.path.splitext(model_xml)[0] + ".bin"
        
        self.plugin = IECore()
        self.network = IENetwork(model=model_xml, weights=model_bin)
        ### TODO: Check for supported layers ###
        #if not all_layers_supported(self.plugin, self.network, console_output=console_output):
        
        supported_layers = self.plugin.query_network(self.network, device_name="CPU")
        
        
        for layer in self.network.layers.keys():
                if layer not in supported_layers:
                    print("Check whether extensions are available to add to IECore.")
                    
        
        
        self.plugin.add_extension(CPU_EXTENSION, DEVICE)
            
        self.exec_network = self.plugin.load_network(self.network, DEVICE)
        # Get the input layer
        self.input_blob = next(iter(self.network.inputs))
        self.output_blob = next(iter(self.network.outputs))
       
        ### TODO: Return the loaded inference plugin ###
        ### Note: You may need to update the function parameters. ###
        return

    def get_input_shape(self):
        ### TODO: Return the shape of the input layer ###
        all_shapes = {}
        for shape in self.network.inputs:
            all_shapes[shape] = (self.network.inputs[shape].shape)
        return all_shapes
    

    def exec_net(self, net_input, request_id):
        ### TODO: Start an asynchronous request ###
        ### TODO: Return any necessary information ###
        self.infer_request_handle = self.exec_network.start_async(
                request_id, 
                inputs=net_input)
        ### TODO: Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        return 


    def wait(self):
        ### TODO: Wait for the request to be complete. ###
        ### TODO: Return any necessary information ###
        ### Note: You may need to update the function parameters. ###
        return self.infer_request_handle.wait()
        
    

    def get_output(self):
        ### TODO: Extract and return the output results
        ### Note: You may need to update the function parameters. ###
        return self.infer_request_handle.outputs[self.output_blob]
         

def all_layers_supported(engine, network, console_output=False):
    ### TODO check if all layers are supported
    ### return True if all supported, False otherwise
    layers_supported = engine.query_network(network, device_name='CPU')
    layers = network.layers.keys()

    all_supported = True
    for l in layers:
        if l not in layers_supported:
            all_supported = False

    return all_supported