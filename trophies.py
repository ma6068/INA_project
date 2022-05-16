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

trofei = [2, 5, 2, 6, 4,
          14, 0, 1, 1, 3,
          15, 4, 0, 0, 1,
          0, 0, 14, 0, 2,
          10, 10, 1, 1, 0]


with open("money.txt", 'r', encoding='utf8') as f:
    f.readline()
    i = 0
    for line in f:
        line = line.split(',')
        if (trofei[i] == 0):
            print(line[0] + " has 0 trophies")
        else:
            rezultat = int(line[2]) / trofei[i]
            rezultat = rezultat / 1000000000
            print(line[0] + " spent: " + str(rezultat) + " billion")


        i = i + 1

