import os
import networkx as nx
from cdlib.algorithms import louvain
import leidenalg
import igraph as ig


def read():
    for filename in os.listdir('./data'):
        if filename != 'data.txt':
            continue
        labels = dict()
        G = nx.MultiGraph(name=filename)
        with open(os.path.join('./data', filename), 'r', encoding='utf8') as f:
            f.readline()  # read first row
            alldata = f.readlines()
            for el in alldata:
                data = el.split(',')
                if data[5] == 'Retired':
                    continue
                if data[0] not in list(G.nodes()):
                    G.add_node(int(data[0]), label=data[1])
                    labels[int(data[0])] = data[1]
                if data[5] not in list(G.nodes()):
                    G.add_node(int(data[5]), label=data[6])
                    labels[int(data[5])] = data[6]
                if data[3] == 'in':
                    G.add_edge(int(data[0]), int(data[5]))
                elif data[3] == 'left':
                    G.add_edge(int(data[5]), int(data[0]))
        return G, labels


if __name__ == "__main__":
    G, labels = read()
    communities = louvain(G).communities
    communities_teams = [[] for _ in range(len(communities))]
    for i in range(len(communities)):
        for j in range(len(communities[i])):
            communities_teams[i].append(labels[communities[i][j]])
    print(communities_teams)
    # G = ig.Graph.from_networkx(G)
    # com = leidenalg.find_partition(G, leidenalg.ModularityVertexPartition)
    # print(com)
    # ig.plot(c, bbox=(600, 500), vertex_label_size=5, margin=50)
    # print(communities)
