import os

f2 = open('./data/data.txt', 'w', encoding='utf8')
f2.write('Team1_Id, Team1_name, Country1, Direction, Position, Team2_id, Team2_name, Country2, Price \n')
for filename in os.listdir('./data'):
    if filename != 'transfers.csv':
        continue
    with open(os.path.join('./data', filename), 'r', encoding='utf8') as f:
        f.readline()  # read first row
        alldata = f.readlines()
        for el in alldata:
            data = el.split(',')
            if int(data[1]) >= 2011 and (data[0] == 'GB1' or data[0] == 'ES1' or data[0] == 'IT1' or data[0] == 'L1' or data[0] == 'FR1'):
                # nekade ima loso ime na drzava (pr. Korea, South) i tie gi trgame
                if len(data) != 23:
                    continue
                team1_id = data[3]
                team1_name = data[4]
                team1_country = data[5]
                direction = data[6]
                player_name = data[8]
                position = data[12]
                team2_id = data[13]
                team2_name = data[14]
                team2_country = data[15]
                price1 = data[16]
                price2 = data[17]
                if not price1:
                    price1 = 0
                if not price2:
                    price2 = 0
                price = float(price1) + float(price2)
                if team2_country != 'England' and team2_country != 'France' and team2_country != 'Germany' and team2_country != 'Italy' and team2_country != 'Spain':
                    team2_country = 'Other'
                f2.write(team1_id + ',' + team1_name + ',' + team1_country + ',' + direction + ',' + position + ',' + team2_id + ',' + team2_name + ',' + team2_country + ',' + str(price) + ',' + player_name + '\n')
