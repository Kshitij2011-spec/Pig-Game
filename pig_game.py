import random
import time

def roll_dice():
    return random.randint(1, 6)

while True:
    players = input("Enter the number of Players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("⚠️ Please enter between 2 and 4 players!")
    else:
        print("⚠️ Invalid input, enter a number!")

max_score = 50
player_scores = [0 for _ in range(players)]

print("\n🎲 Welcome to the Dice Game! First to reach 50 points wins! 🎯\n")
time.sleep(1)

while max(player_scores) < max_score:
    for player_idx in range(players):
        current_score = 0
        print(f"\n✨ Player {player_idx+1}'s Turn ✨")
        print(f"🏆 Your Total Score: {player_scores[player_idx]}")
        
        while True:
            choice = input("Roll the dice? (y/n): ").lower()
            if choice != "y":
                print("👉 You decided to hold your score.")
                break
            value = roll_dice()
            print(f"🎲 You rolled a {value}!")
            if value == 1:
                print("💀 Oh no! You rolled a 1. Turn over, no points this round!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"🔥 Current round score: {current_score}")

        player_scores[player_idx] += current_score
        print(f"📊 Updated Scores: {player_scores}")
        time.sleep(1)
max_score=max(player_scores)
winner_index = player_scores.index(max_score)
print("\n🏆 Game Over! 🏆")
print(f"🎉 Player {winner_index+1} WINS with a score of {player_scores[winner_index]}! 🎉")
