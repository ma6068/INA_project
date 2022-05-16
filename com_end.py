best_teams = ['Manchester United', 'Manchester City', 'Liverpool FC', 'Chelsea FC', 'Arsenal FC',
              'Paris Saint-Germain', 'Olympique Marseille', 'AS Monaco', 'Olympique Lyon', 'LOSC Lille',
              'Bayern Munich', 'Borussia Dortmund', 'RB Leipzig', 'Borussia Mönchengladbach', 'FC Schalke 04',
              'AC Milan', 'Inter Milan', 'Juventus FC', 'AS Roma', 'SS Lazio',
              'Real Madrid', 'FC Barcelona', 'Atlético de Madrid', 'Valencia CF', 'Athletic Bilbao']


def getCommunities():
    f = open('communities_info.txt', 'r', encoding="utf8")
    comms = [[] for _ in range(5)]
    lines = f.readlines()
    for i in range(len(lines)):
        data = lines[i].split(',')
        comms[i] = data
    f.close()
    return comms


def getIn(comms):
    result = [[0, 0, 0, 0, 0] for _ in range(25)]
    result_money = [[0, 0, 0, 0, 0] for _ in range(25)]
    f = open('./data/data.txt', 'r', encoding='utf8')
    f.readline()  # ja citame prvata linija
    lines = f.readlines()
    for line in lines:
        data = line.split(',')
        if data[1] in best_teams and data[3] == 'in':
            index = best_teams.index(data[1])  # index na timot sto go gledas sega (onoj sto e vo best_teams)
            team = data[6]  # timot od koj sto imat kupeno
            for i in range(len(comms)):
                if team in comms[i]:
                    result[index][i] += 1
                    result_money[index][i] += int(float(data[8]))
    f.close()
    return result, result_money


def getOut(comms):
    result = [[0, 0, 0, 0, 0] for _ in range(25)]
    result_money = [[0, 0, 0, 0, 0] for _ in range(25)]
    f = open('./data/data.txt', 'r', encoding='utf8')
    f.readline()  # ja citame prvata linija
    lines = f.readlines()
    for line in lines:
        data = line.split(',')
        if data[1] in best_teams and data[3] == 'left':
            index = best_teams.index(data[1])  # index na timot sto go gledas sega (onoj sto e vo best_teams)
            team = data[6]  # timot od koj sto imat kupeno
            for i in range(len(comms)):
                if team in comms[i]:
                    result[index][i] += 1
                    result_money[index][i] += int(float(data[8]))
    f.close()
    return result, result_money


if __name__ == "__main__":
    communities = getCommunities()
    result1, result1_money = getIn(communities)
    f = open('./komunikacijaIN.txt', 'w', encoding='utf8')
    f.write('Ekipa, IN transferi za sekoj communiti, dobieni pari \n')
    for i in range(len(best_teams)):
        f.write(best_teams[i] + ' \n')
        for j in range(len(result1[i])):
            f.write('Community ' + str(j) + ", transferi: " + str(result1[i][j]) + " pari: " + str(result1_money[i][j]) + ' \n')
    f.close()
    print(result1)
    print(result1_money)

    result1, result1_money = getOut(communities)
    f = open('./komunikacijaOUT.txt', 'w', encoding='utf8')
    f.write('Ekipa, OUT transferi za sekoj communiti, potroseni pari \n')
    for i in range(len(best_teams)):
        f.write(best_teams[i] + ' \n')
        for j in range(len(result1[i])):
            f.write('Community ' + str(j) + ", transferi: " + str(result1[i][j]) + " pari: " + str(
                result1_money[i][j]) + ' \n')
    f.close()
    print(result1)
    print(result1_money)