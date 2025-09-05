# 🎲 Multiplayer Dice Game (Python)

A fun **multiplayer dice game** built in Python.  
Players take turns rolling a die to reach the target score (default **50 points**).  
But beware — if you roll a **1**, you lose all points from that round!  

---

## ✨ Features
- 2 to 4 players can play  
- Players can choose to **roll again** or **hold** their score  
- Rolling a **1** wipes out the round’s points  
- Fun messages and emojis for a more lively experience  
- First player to reach **50 points** wins 🎯  

---

## 🚀 How to Run

### 1. Clone or Download
Download the file `dice_game.py`.

### 2. Run the Game
Make sure you have Python 3 installed.  
Run in your terminal:

```bash
python dice_game.py
```

## 🎮 Gameplay

Enter the number of players (2–4).

On your turn:

Press y to roll the die

Press n to hold and keep your round score

If you roll a 1:

💀 You lose your round score and your turn ends!

First to 50 points is crowned the winner 🏆

## 📊 Example
Enter the number of Players (2-4): 2

🎲 Welcome to the Dice Game! First to reach 50 points wins! 🎯

✨ Player 1's Turn ✨
🏆 Your Total Score: 0
Roll the dice? (y/n): y
🎲 You rolled a 6!
🔥 Current round score: 6
Roll the dice? (y/n): y
🎲 You rolled a 1!
💀 Oh no! You rolled a 1. Turn over, no points this round!
📊 Updated Scores: [0, 0]

✨ Player 2's Turn ✨
🏆 Your Total Score: 0
...
🏆 Winning

At the end of the game:

🏆 Game Over! 🏆
🎉 Player 2 WINS with a score of 52! 🎉

##🔮 Future Ideas

1.Add a target score option (instead of fixed 50)
2.Add a computer (AI) player
3.Add ASCII art dice faces
## 📜 License

MIT License
