              #Rock Paper Scissor Game#
import random
game=["Rock","Paper","Scissor"]
bot=random.choice(game).lower()
print("{Rock,Paper,Scissor}")
print("Select any one of them:")
human=input("Player:").lower()
print("computer:",bot)
if human==bot:
  print("TIE")
elif human=="rock" and bot=="scissor":
  print("player won")
elif bot=="rock" and human=="scissor":
  print("computer won")
elif bot=="rock" and human=="paper":
  print("Player won")  
elif bot=="paper" and human=="rock":
  print("Computer won")  
elif bot=="scissor" and human=="paper":
  print("Computer won")  
else:
  print("player won")