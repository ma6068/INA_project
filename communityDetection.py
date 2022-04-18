import os
import networkx as nx
from cdlib.algorithms import louvain


def read():
    for filename in os.listdir('./data'):
        if filename != 'data.txt':
            continue
        G = nx.MultiGraph(name=filename)
        with open(os.path.join('./data', filename), 'r', encoding='utf8') as f:
            f.readline()  # read first row
            alldata = f.readlines()
            for el in alldata:
                data = el.split(',')
                if data[5] == 'Retired':
                    continue
                if data[0] not in list(G.nodes()):
                    G.add_node(int(data[0]))
                if data[5] not in list(G.nodes()):
                    G.add_node(int(data[5]))
                if data[3] == 'in':
                    G.add_edge(int(data[0]), int(data[5]))
                elif data[3] == 'left':
                    G.add_edge(int(data[5]), int(data[0]))
        return G


if __name__ == "__main__":
    G = read()
    communities = louvain(G).communities
    print(len(communities))

