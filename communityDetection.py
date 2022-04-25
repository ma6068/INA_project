import os
import networkx as nx
from cdlib.algorithms import louvain
import leidenalg
import igraph as ig


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


def getCommunities(G):
    communities = louvain(G).communities
    communities_teams = [[] for _ in range(len(communities))]
    for i in range(len(communities)):
        for j in range(len(communities[i])):
            communities_teams[i].append(labels[communities[i][j]])
    return communities_teams


def getNumberTeamsForCountry(communities_teams):
    n_england = 0
    n_france = 0
    n_germany = 0
    n_italy = 0
    n_spain = 0
    n_other = 0
    for community in communities_teams:
        for team in community:
            if team in england_teams:
                n_england += 1
            elif team in france_teams:
                n_france += 1
            elif team in germany_teams:
                n_germany += 1
            elif team in italy_teams:
                n_italy += 1
            elif team in spain_teams:
                n_spain += 1
            else:
                n_other += 1
    return [n_england, n_france, n_germany, n_italy, n_spain, n_other]


def getCountryForCommunity(communities_teams):
    result = []
    for i in range(len(communities_teams)):
        n_england = 0
        n_france = 0
        n_germany = 0
        n_italy = 0
        n_spain = 0
        n_other = 0
        for team in communities_teams[i]:
            if team in england_teams:
                n_england += 1
            elif team in france_teams:
                n_france += 1
            elif team in germany_teams:
                n_germany += 1
            elif team in italy_teams:
                n_italy += 1
            elif team in spain_teams:
                n_spain += 1
            else:
                n_other += 1
        result.append([n_england, n_france, n_germany, n_italy, n_spain, n_other])
    return result


if __name__ == "__main__":
    print('---------------------------')

    G, labels = read()
    communities_teams = getCommunities(G)
    print('Number of nodes: ' + str(len(G.nodes())))
    print('Number of edges: ' + str(len(G.edges())))
    print('---------------------------')

    number_teams_country = getNumberTeamsForCountry(communities_teams)
    print('Number of clubs for each country')
    print('England: ' + str(number_teams_country[0]) + ' France: ' + str(number_teams_country[1]) +
          ' Germany: ' + str(number_teams_country[2]) + ' Italy: ' + str(number_teams_country[3]) +
          ' Spain: ' + str(number_teams_country[4]) + ' Other: ' + str(number_teams_country[5]))
    print('---------------------------')

    community_country = getCountryForCommunity(communities_teams)
    print('Number of teams for each country by community')
    for i in range(len(community_country)):
        print('Community ' + str(i))
        print('England: ' + str(community_country[i][0]) + ' France: ' + str(community_country[i][1]) +
              ' Germany: ' + str(community_country[i][2]) + ' Italy: ' + str(community_country[i][3]) +
              ' Spain: ' + str(community_country[i][4]) + ' Other: ' + str(community_country[i][5]))
    print('---------------------------')