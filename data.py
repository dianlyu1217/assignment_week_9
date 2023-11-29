# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 读取CSV文件
# csv_file_path = 'database.csv'  # 请替换成你的CSV文件路径
# df = pd.read_csv(csv_file_path)
#
# # 统计数据
# total_games = len(df)
# player_x_wins = len(df[df['Winner'] == 'X'])
# player_o_wins = len(df[df['Winner'] == 'O'])
# draws = len(df[df['Winner'] == 'Draw'])
#
# # 打印统计数据
# print(f"总游戏数: {total_games}")
# print(f"玩家 X 获胜次数: {player_x_wins}")
# print(f"玩家 O 获胜次数: {player_o_wins}")
# print(f"平局次数: {draws}")
#
# # 创建表格报告
# plt.figure(figsize=(10, 6))
#
# # 创建饼图
# labels = ['Player X Wins', 'Player O Wins', 'Draws']
# sizes = [player_x_wins, player_o_wins, draws]
# colors = ['#ff9999', '#66b3ff', '#99ff99']
# explode = (0.1, 0, 0)  # 突出显示第一个切片
#
# plt.subplot(2, 2, 1)
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
# plt.axis('equal')
# plt.title('Distribution of game results')
#
# # 创建柱状图
# players = ['Player X', 'Player O']
# wins = [player_x_wins, player_o_wins]
#
# plt.subplot(2, 2, 2)
# plt.bar(players, wins, color=['#ff9999', '#66b3ff'])
# plt.title('Player wins')
#
# # 创建折线图
# game_numbers = df['Round']
# # draw_percentage = (draws / total_games) * 100
# draw_percentage = []
# winner = df['Winner']
# draw_number = 0
# round_number = 0
# for x in winner:
# 	round_number += 1
# 	if x == 'Draw':
# 		draw_number += 1
# 	draw_percentage.append((draw_number / round_number) * 100)
#
# plt.subplot(2, 2, 3)
# plt.plot(game_numbers, draw_percentage, marker='o', linestyle='-', color='green')
# plt.title('Draw percentage varies with game count')
#
# # 显示图表
# plt.tight_layout()
# plt.show()
#
# #
# # pd.dataframe
# #
# # df.describe()
