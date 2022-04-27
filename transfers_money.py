import os


best_teams_ids = [985, 281, 31, 631, 11,
                  583, 244, 162, 1041, 1082,
                  27, 16, 23826, 18, 33,
                  5, 46, 506, 12, 398,
                  418, 131, 13, 1049, 621]

best_teams = ['Manchester United', 'Manchester City', 'Liverpool FC', 'Chelsea FC', 'Arsenal FC',
              'Paris Saint-Germain', 'Olympique Marseille', 'AS Monaco', 'Olympique Lyon', 'LOSC Lille',
              'Bayern Munich', 'Borussia Dortmund', 'RB Leipzig', 'Borussia Mönchengladbach', 'FC Schalke 04',
              'AC Milan', 'Inter Milan', 'Juventus FC', 'AS Roma', 'SS Lazio',
              'Real Madrid', 'FC Barcelona', 'Atlético de Madrid', 'Valencia CF', 'Athletic Bilbao']


def read_communities():
    result = [[] for _ in range(5)]   # 5 communities dobivme
    f = open('./communities_info.txt', 'r', encoding='utf8')
    lines = f.readlines()
    for i in range(len(lines)):
        teams = lines[i].split(',')
        for team in teams:
            result[i].append(team)
    f.close()
    return result


def get_team_money():
    result = dict()  # key: [potroseni_pari, zemeni_pari, razlika]
    f = open('./data/data.txt', 'r', encoding='utf8')
    f.readline()  # ja citame prvata linija
    lines = f.readlines()
    for line in lines:
        data = line.split(',')
        if data[1] in best_teams:
            if data[1] not in result:
                result[data[1]] = [0, 0, 0]
            price = int(float(data[8]))
            if data[3] == 'left':
                result[data[1]][0] += price
            elif data[3] == 'in':
                result[data[1]][1] += price
    for key in result.keys():
        result[key][2] = result[key][1] - result[key][0]
    f.close()
    return result


def get_team_transfers(community_dict):
    result_left = dict()  # key: [a, b, c, d, e]  // a,b,c,d,e oznacuvat broj na OUT transferi so sekoj community
    result_in = dict()  # key: [a, b, c, d, e]  // a,b,c,d,e oznacuvat broj na IN transferi so sekoj community
    f = open('./data/data.txt', 'r', encoding='utf8')
    f.readline()  # ja citame prvata linija
    lines = f.readlines()
    for line in lines:
        data = line.split(',')
        if data[1] in best_teams:
            if data[1] not in result_left:
                result_left[data[1]] = [0, 0, 0, 0, 0]  # imame 5 communities
            if data[1] not in result_in:
                result_in[data[1]] = [0, 0, 0, 0, 0]  # imame 5 communities
            team2 = data[6]
            if team2 not in community_dict:
                continue
            index = community_dict[team2]
            if data[3] == 'left':
                result_left[data[1]][index] += 1
            elif data[3] == 'in':
                result_in[data[1]][index] += 1
    f.close()
    return result_left, result_in


if __name__ == "__main__":
    communities = read_communities()
    coms_dict = dict()
    for i in range(len(communities)):
        for j in range(len(communities[i])):
            coms_dict[communities[i][j]] = i
    team_money = get_team_money()
    team_out_transfers, team_in_transfers = get_team_transfers(coms_dict)
    f = open('./money.txt', 'w', encoding='utf8')
    f.write('Tim, Potroseni pari, Zaraboteni pari, Razlika \n')
    for key in team_money.keys():
        f.write(key + ',' + str(team_money[key][0]) + ',' + str(team_money[key][1]) + ',' + str(team_money[key][2]) + '\n')
    f.close()

    f = open('./transfers.txt', 'w', encoding='utf8')
    f.write('Kolku OUT transferi ima napraveno ekipata za sekoj community \n')
    for key in team_out_transfers.keys():
        f.write(key + ',' + str(team_out_transfers[key][0]) + ',' + str(team_out_transfers[key][1])
                + ',' + str(team_out_transfers[key][2]) + ',' + str(team_out_transfers[key][3]) + ','
                + str(team_out_transfers[key][4]) + '\n')
    f.write('---------------------------------- \n')
    f.write('Kolku IN transferi ima napraveno ekipata za sekoj community \n')
    for key in team_in_transfers.keys():
        f.write(key + ',' + str(team_in_transfers[key][0]) + ',' + str(team_in_transfers[key][1])
                + ',' + str(team_in_transfers[key][2]) + ',' + str(team_in_transfers[key][3]) + ','
                + str(team_in_transfers[key][4]) + '\n')
    f.close()
