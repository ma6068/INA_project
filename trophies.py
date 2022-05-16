best_teams_ids = [985, 281, 31, 631, 11,
                  583, 244, 162, 1041, 1082,
                  27, 16, 23826, 18, 33,
                  5, 46, 506, 12, 398,
                  418, 131, 13, 1049, 621]

best_teams = ['Manchester United', 'Chelsea FC', 'Arsenal FC', 'Manchester City', 'Liverpool FC',
              'Valencia CF', 'Atlético de Madrid', 'Real Madrid', 'FC Barcelona',  'Athletic Bilbao',
              'AC Milan', 'Juventus FC', 'SS Lazio', 'AS Roma', 'Inter Milan',
              'Bayern Munich', 'Borussia Dortmund', 'FC Schalke 04', 'Borussia Mönchengladbach', 'RB Leipzig',
              'Olympique Lyon', 'LOSC Lille', 'Paris Saint-Germain', 'Olympique Marseille', 'AS Monaco']

trofei = [2, 6, 4, 5, 2,
          1, 1, 10, 10, 0,
          0, 14, 2, 0, 0,
          15, 4, 1, 0, 0,
          1, 3, 14, 0, 1]



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
            print(line[0] + " spent: " + str(round(rezultat, 4)) + " billion")


        i = i + 1

