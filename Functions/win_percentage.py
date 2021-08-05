def win_percentages(wins, losses):
  games = wins + losses
  win_percentages = (wins / games) * 100
  return win_percentages

print(win_percentages(5, 5))
