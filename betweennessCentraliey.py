import os
import networkx as nx

england_teams = []
france_teams = []
germany_teams = []
italy_teams = []
spain_teams = []
other_teams = []


def getTeamCountry(team_country, team_name):
    if team_country == 'England' and team_name not in england_teams:
        england_teams.append(team_name)
    elif team_country == 'Spain' and team_name not in spain_teams:
        spain_teams.append(team_name)
    elif team_country == 'France' and team_name not in france_teams:
        france_teams.append(team_name)
    elif team_country == 'Italy' and team_name not in italy_teams:
        italy_teams.append(team_name)
    elif team_country == 'Germany' and team_name not in germany_teams:
        germany_teams.append(team_name)
    elif team_name not in other_teams:
        other_teams.append(team_name)


def read():
    all_data = []
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
                getTeamCountry(data[2], data[1])
                getTeamCountry(data[7], data[6])
                if data[5] == 'Retired':
                    continue
                if data[0] not in list(G.nodes()):
                    G.add_node(int(data[0]), team_name=data[1], team_country=data[2])
                    labels[int(data[0])] = data[1]
                if data[5] not in list(G.nodes()):
                    G.add_node(int(data[5]), team_name=data[6], team_country=data[7])
                    labels[int(data[5])] = data[6]
                price = int(float(data[8]))
                if (int(data[0]), int(data[5]), price, data[4], data[9]) not in all_data \
                        and (int(data[5]), int(data[0]), price, data[4], data[9]) not in all_data:
                    if data[3] == 'left':
                        G.add_edge(int(data[0]), int(data[5]), price=price, player_position=data[4])
                        all_data.append((int(data[0]), int(data[5]), price, data[4], data[9]))
                    elif data[3] == 'in':
                        G.add_edge(int(data[5]), int(data[0]), price=price, player_position=data[4])
                        all_data.append((int(data[0]), int(data[5]), price, data[4], data[9]))
        return G, labels


G, labels = read()
results = nx.betweenness_centrality(G)
final = []
for i in range(5):
    max = 0.0
    maxKey = ''
    for key in results:
        if results[key] > max:
            max = results[key]
            maxKey = key
    final.append((maxKey, max))
    del results[maxKey]
print(final)




