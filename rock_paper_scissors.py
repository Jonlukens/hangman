
import random

def f():

        play_or_no = input ("Start a game of Rock-Papper-Scissors? Y/N:")
        play_or_no = str (play_or_no)

        if play_or_no == "Y":
            
            while True: 
                name_1 = input ("Player 1:")
                name_2 = input ("Player 2:")
                first_player = random.choice([name_1,name_2])
    
                if first_player == name_1:
                    second_player = name_2

                else:
                    second_player = name_1

                while True:
                
                    move_for_first_player = input ("{}, do you want rock, paper, or scissors? :".format(first_player))
                    move_for_first_player = str (move_for_first_player)

                    move_for_second_player = input ("{},do you want rock, paper, or scissors? :".format(second_player))
                    move_for_second_player = str (move_for_second_player)


                    if move_for_first_player == "rock":

                        if move_for_second_player == "rock":
                            print ("You guessed the same thing! Guess again!")
                            continue


                        elif move_for_second_player == "paper":
                            print("Congratulations {}! You Won!".format(second_player))
                            break


                        elif move_for_second_player == "scissors":
                            print("Congratulations {}! You Won!".format(first_player))
                            break


                    if move_for_first_player == "paper":

                        if move_for_second_player == "rock":
                            print("Congratulations {}! You Won!".format(first_player))
                            break
    

                        elif move_for_second_player == "paper":
                            print ("You guessed the same thing! Guess again!")
                            continue


                        elif move_for_second_player == "scissors":
                            print("Congratulations {}! You Won!".format(second_player))
                            break


                
                    if move_for_first_player == "scissors":

                        if move_for_second_player == "rock":
                            print("Congratulations {}! You Won!".format(second_player))
                            break

                        elif move_for_second_player == "paper":
                            print("Congratulations {}! You Won!".format(first_player))
                            break

                        elif move_for_second_player == "scissors":
                            print ("You guessed the same thing! Guess again!")
                            continue

                play_again = input ("Do you want to play again? Y/N:")
                play_again = str (play_again)

                if play_again == "Y":
                    continue

                else:
                    print ("Goodbye!")
                    break



        else:
            print ("Goodbye!")
                

f()
