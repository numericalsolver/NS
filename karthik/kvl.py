import matplotlib.pyplot as plt
from schemdraw import elements as elm
from schemdraw import Drawing


def parse_circuit_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    components = {}
    connections = []

    for line in lines:
        if line.startswith('WIRE'):
            # Parse wire data
            wire_data = line.split(' ')
            if len(wire_data) >= 4:
                connections.append((wire_data[1],wire_data[2], wire_data[3],wire_data[4].strip()))
            else:
                print(f"Ignoring line: {line.strip()} - Invalid wire data format")
        elif line.startswith('SYMBOL'):
            # Parse component data
            component_data = line.split(' ')
            component_name = component_data[1]
            component_x = component_data[2]
            component_y = component_data[3]
            component_orientation = component_data[4].strip()
            components[component_name] = {
                'name': component_name,
                'x': component_x,
                'y': component_y,
                'orientation': component_orientation
            }
        elif line.startswith('SYMATTR'):
            # Parse component attributes
            attr_data = line.split(' ')
            # component_name = attr_data[1]
            attr_name = attr_data[1]
            attr_value = attr_data[2].strip()
            if attr_name == 'Value':
                components[component_name][attr_name] = attr_value
            elif attr_name == 'InstName':
                components[component_name][attr_name] = attr_value

    print("components", components)
    print("connections", connections)
    return components, connections


def reconstruct_circuit(components, connections):
    drawing = Drawing()
    
    # Add components to the drawing
    for component_name, component_data in components.items():
        if component_data['name'] == 'cap':
            drawing.add(elm.Capacitor().label(component_data['InstName'], loc='bottom').label(str(component_data['Value']) + 'F', loc='top'))
        elif component_data['name'] == 'voltage':
            drawing.add(elm.SourceV().label(component_data['InstName'], loc='bottom').label(str(component_data['Value']) + 'V', loc='top'))
        elif component_data['name'] == 'res':
            drawing.add(elm.Resistor().label(component_data['InstName'], loc='bottom').label(str(component_data['Value']) + 'Ω', loc='top'))
        else:
            print(f"Unknown component type: {component_data['name']}")

    # Add wires to the drawing
    for connection in connections:
        start_x, start_y, end_x, end_y = map(int, connection)
        drawing.add(elm.Line(start=(start_x, start_y), end=(end_x, end_y)).color('black'))
    
    # Display the drawing
    drawing.draw()

    

def apply_kvl(components, connections):
    for connection in connections:
        # Apply KVL for each loop in the circuit
        # Calculate voltage drops across components based on component values and orientations
        pass

# Example usage
file_path = 'a.asc'
components, connections = parse_circuit_data(file_path)
reconstruct_circuit(components, connections)
plt.show()
