import random
from random import random as r, seed
import pickle
from uuid import uuid4

def createLayout(input_points, output_points, depth, layer_size_list):
    NN_Layout = []
    NN_Layout.append([])
    for x in range(input_points):
        NN_Layout[0].append([[0,x],[],[],[]])
    for layers in range(depth):
        layer = []
        for size in range(layer_size_list[layers]):
            node = []
            node_id = [layers, size]
            inputs = []
            weights = []
            outputs = []
            node.append(node_id)
            node.append(inputs)
            node.append(weights)
            node.append(outputs)
            layer.append(node)
        NN_Layout.append(layer)
    NN_Layout.append([])
    for x in range(output_points):
        NN_Layout[-1].append([[depth,x],[],[],[]])
    return NN_Layout

def add_inputs(layout):
    for layer in layout:
        for node in layer:
            if layout.index(layer) != 0:
                for size in range(0, random.randint(0, len(layout[layout.index(layer)-1]))):
                    node[1].append(random.choice(layout[layout.index(layer)-1])[0])
            else:
                node[1].append(0)

def add_weights(layout):
    seed(random.randint(0, 284))
    for layer in layout:
        for node in layer:
            IN_FRAME = []
            for x in range(len(node[1])):
                IN_FRAME.append(r()*(r()*random.randint(1, 43)))
            node[2].append(IN_FRAME)
            OUT_FRAME = []
            for x in range(len(node[3])):
                OUT_FRAME.append(r()*(r()*random.randint(1, 65)))
            node[2].append(OUT_FRAME)

def add_outputs(layout):
    for layer in layout:
        for node in layer:
            if layout.index(layer) < len(layout)-1:
                for size in range(0, random.randint(0, len(layout[layout.index(layer)+1]))):
                    node[3].append(random.choice(layout[layout.index(layer)+1])[0])
            else:
                node[3].append(0)

def picklefile(filename, data):
    outfile = open(filename, 'wb')
    pickle.dump(data, outfile)
    outfile.close()

def generate_NN(depth, layer_size_list, input_points, output_points):
    layout = createLayout(input_points, output_points, depth, layer_size_list)
    add_inputs(layout)
    add_outputs(layout)
    add_weights(layout)
    #assign_variables(layout, [45,7,29,3,12.7], [23,6,1,78,4,3.5])
    nn_str = 'neural_network_'+str(uuid4())
    picklefile(nn_str, layout)
    return nn_str

def assign_variables(layout, inputs, outputs):
    for data in inputs:
        layout[0][inputs.index(data)][1] = [data]
    for data in outputs:
        layout[len(layout)-1][outputs.index(data)][3] = [data]
    return layout


nn_location = generate_NN(5, [3,7,15,8,2], 10, 4)

new_layout = pickle.load(open(nn_location, 'rb'))

for layer in new_layout:
    for node in layer:
        print(node, '\n-------------')
    print('\n///////////////')

def Train_NN(input_variables, output_variables):
    assign_variables(new_layout, [val1,val2,val3,val4], [val1,val2,val3,val4])
    train_nodes