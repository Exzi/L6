import random
team1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [max(score1, score2) for score1, score2 in zip(team1, team2)]
print("Очки первой команды:", team1)
print("Очки второй команды:", team2)
print("Победители:", winners)