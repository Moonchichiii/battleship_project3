<h1 style="text-decoration: none; border-bottom: none;">Battleship Game</h1>
<h3>Ahoooooy Sailors! Ready to navigate some rough waters?</h3>



#### ****Visit the live project below.****

  <a href="https://battleshipv2-30e17c867991.herokuapp.com/" style="text-decoration: none;">👉 Click Here.</a>
 


# ![Alt text](assets/readme_images/new_signin_prompt.png)

<br>

## Table of Contents
- [Project Goals](#project-goals)
  - [Site Owner Goals](#site-owner-goals)
 [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [User stories Manual Testing](#manual-testing)
    - [User Manual](#user-manual)    
- [Flow Chart](#flowchart)
- [Design](#design)
- [Game Features](#game-features)
    * [Game Settings](#game-settings)
- [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Validator Testing](#validator-testing)
- [Bugs & Fixes](#bugs-fixes)
- [Technologies Used](#technologies-used)
    * [Dependencies](#dependencies)
    * [Installation (Cloning the Project)](#installation-cloning-the-project)
    * [Python Libraries Used](#python-libraries-used)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)




## Project Goals

- Battleships is a classic game of strategy and wit. Played on a ruled grid, whether on paper or board, 
- the player must locate a concealed fleet of warships. By taking shots at specific grid coordinates,
- the objective is to identify and sink the entire hidden fleet.






## site-owner-goals


* Create a Battleship game that is intuitive and engaging for the user.
* Ensure that new users can effortlessly sign up.
* Ensure that existing users can log in smoothly.
* Handle and display errors in a clear manner to the user.
* Allow users the option to restart the game.

<br>

[Back to top](#)


<br>


## User Experience



### User Stories

1. **First Prompt**: <br>
Start screen, you're given an option to signup or login. If you have registered before then just login.    
[Manual Testing](#first-prompt)
    
2. **Board Size Selection**: <br>
Choose between a 5x5 or 8x8 board size.<br>
[Manual Testing](#manual-testing-board-size-selection)

3. **Ship Placement**:
    <br>Decide the number of ships you wish to randomly place on your board.
    <br>
    [Manual Testing](#manual-testing-ship-placement)

4. **Turn Selection**:
    <br>Decide the number of turns (tries) you'd like: 5 or 10 turns to locate the ships.
    <br>
    [Manual Testing](#manual-testing-turn-selection)

5. **Ship Count Display**:
    <br>Above the board, the number of remaining ships is shown.
    <br>
    [Manual Testing](#manual-testing-ship-count-display)

6. **Hit Count Display**:
    <br>View the number of successful hits above the board.
    <br>
    [Manual Testing](#manual-testing-hit-count-display)

7. **Turns Left Display**:
    <br>Monitor the number of turns you have left, displayed above the board.
    <br>
    [Manual Testing](#manual-testing-turns-left-display)

8. **Board Display**:
    <br>The board consist of "*" symbols. Hits are displayed by "X" and misses by "M".
    <br>
    [Manual Testing](#manual-testing-board-display)

9. **Endgame**:
    <br>Once all turns are used or all ships are hit, you're asked if you'd like to play again.
    <br> 
    [Manual Testing](#manual-testing-endgame)

10. **Restarting the Game**:
    <br>Return to the signup/login screen to either sign in again or register a new game user.
    <br>
     [Manual Testing](#manual-testing-restarting)



[Back to top](#)







### User Manual


**If you're new to Battleship check out this link** 👉 https://en.wikipedia.org/wiki/Battleship

* Start with a Sailor Sign in / registration for new Sailors, and simple Login for returning players,
  I've kept it very simple, ensuring you can get back into the battle again.

* Once you've been greeted by the sailor prompt and you're all set,
    it's time to decide on your game's layout. For a quick game, the 5x5 board is a perfect choice.

* After setting up the board prompt, decide how many ships you'd like
    to hide on the game board. Remember: more ships on a smaller board means more chances to sink ships.

* Next, determine the number of turns (or tries) you want for hunting those hidden ships.
    You can choose anywhere between 5-10 turns per game.

    **Here's a hint:**
    
   *   If you've chosen the 5x5 board with 6 ships and go for 10 turns,
   *   get ready for an exciting round filled with sunken ships.
   
   *   Once your game has ended, the outcomes of your successful sinkings are 
   *   displayed on the main game board, and ships left.
    
       - Then, we'll ask: 
       - Ready for another round on the seas?



[Back to top](#)


## Flowchart

👇 CLICK TO EXPAND BELOW <details><summary>A graphical representation of the game process</summary> 

![FlowChart](assets/readme_images/new_flowchart.png)

[Back to top](#)

</details>


<br><br>


## Design
<br>

 * **Simplicity:** The design is straightforward,very simple and user-friendly.
 * **Clean interface:** Using the 'clear' function, the screen is tidy after each prompt.

<br><br>

[Back to top](#)

<br><br>

## Game Features

  * ***Sign in / registration for new Sailors, and simple Login for returning players.***  
<br>

  
![Alt text](assets/readme_images/new_greeting_prompt.png)



[Back to top](#)


### Game settings

<br>

1. **Prompted with the question if you ever sailed with us before?** 
2. **If you have sailed with us before you will simply login again.**
3. **If not you will be asked to create your Sail account**

### Then it's of to the internal Game settings you will be asked. 

5. **Choose between a 5x5 or an 8x8 board** 
6. **Decide on having between 2 to 6 ships**
7. **Determine how many turns to play**

[Back to top](#)

## Testing 

- Pythontutor excellent for visually understanding and verifying how your code executes.

[Execution Visualization Tool](https://pythontutor.com/cp/composingprograms.html#mode=edit)


### Manual Testing

###  User stories Manual Testing

[1. First Prompt](#first-prompt)
<details>
<summary id="first-prompt">1. First Prompt:</summary>


| **Feature**  | **Instruction**              | **User Input**           | **Expected Behavior**                   | **Actual Behavior** |
| :---         |    :----:                    |          :---:           |   :---:                                 |        ---:         |
| First Prompt | Have you played before? (y/n):|        N / Y            | N = signup  / Y = Login                 | Works as intended   |
| signup/login | Please enter A username:     |       Empty input        | Every sailor has a name? Try again!     | Works as intended   |
| signup/login | Please enter A username:     |         "12"             | Every sailor has a name? Not a number!  | Works as intended   |
| signup + login|Please enter A username:/Please select a password:     |                          | Sign up successful / Login  successful  | Works as intended   | 

![Alt text](assets/manual_testing_images/Empty_number_input.png)
![Alt text](assets/manual_testing_images/signup_successful.png)
![Alt text](assets/manual_testing_images/Login_successful.png)
</details><br>

[Manual Testing](#manual-testing-board-size-selection)
<details>
<summary id="manual-testing-board-size-selection">2. Board Size Selection:</summary>

| **Feature**  | **Instruction**              | **User Input**           | **Expected Behavior**                   | **Actual Behavior** |
| :---         |    :----:                    |          :---:           |   :---:                                 |        ---:         |
| Board size   | Prompts user for 5x5 or 8x8 board| "5" or "8"           | Returns correct size                    | Works as intended   |
|              | Select board size (5 or 8):  | Empty input              | Please select a valid! board size (5x5 or 8x8)     | Works as intended   |
|              |                              | 1111                     | invalid size. Please choose between (5x5 or 8x8)?  | Works as intended   | 

![Alt text](assets/manual_testing_images/Boardsize_empty_wrong_number.png)


</details><br>

[Manual Testing](#manual-testing-ship-placement)
<details>
<summary id="manual-testing-ship-placement">3. Ship Placement:</summary>

| **Feature**  | **Instruction**              | **User Input**           | **Expected Behavior**                   | **Actual Behavior** |
| :---         |    :----:                    |          :---:           |   :---:                                 |        ---:         |
| Number of ships | Choose the number of ships? (2-6):| "2","3","4" "6"      |  Returns correct number (2 or 6)       | Works as intended   |
|              |                              | Empty input              |  Please enter a valid number between 2 and 6   | Works as intended   |
|              |                              | "8" "9"                  |  Invalid number! Please choose between 2 and 6 ships? | Works as intended   | 


![Alt text](assets/manual_testing_images/ships_placement_empty_wrong_number.png)

</details><br>

[Manual Testing](#manual-testing-turn-selection)
<details>
<summary id="manual-testing-turn-selection">4. Turn Selection:</summary>

| **Feature**  | **Instruction**              | **User Input**           | **Expected Behavior**                   | **Actual Behavior** |
| :---         |    :----:                    |          :---:           |   :---:                                 |        ---:         |
| Number of turns ? | How many turns ? (5-10):| "5" or "10"               | Returns correct size                    | Works as intended   |
|              |                              | Empty input             | Please enter a valid number between (5 and 10) | Works as intended   |
|              |                              | 1                     | invalid turns! Select a number from (5 to 10)? | Works as intended   | 

![Alt text](assets/manual_testing_images/turns_empty_wrong_number.png)

</details><br>


[Manual Testing](#manual-testing-ship-count-display)
<details>
<summary id="manual-testing-ship-count-display">5. Ship Count Display:</summary>

| **Feature**  | **Expected Behavior**        | **Actual Result**      |   
| :---         |    :----:                    |          ---:          |  
| Ships left: 6|   Ships left: 5              | Not working as intended| 
| Numbers of Hits: 1  | Numbers of Hits: 1    | Works as intended      | 
| Turns left: 1|    Turns left: 1             | Works as intended      |
|              |                              |                        | 

![Alt text](assets/manual_testing_images/ships_count_going_down.png)


- **Issue with ships remaining** 
- Plan of action: When a ship is hit,remove one ship from count. 

![Alt text](assets/readme_images/ships_left_hits_turns.png)

**Issue with ships remaining**
- Resolved.

![Alt text](assets/readme_images/resolved_ship_issue.png)

</details><br>

[Manual Testing](#manual-testing-hit-count-display)
<details>
<summary id="manual-testing-hit-count-display">6. Hit Count Display:</summary>

| **Feature**  | **Expected Behavior**        | **Actual Result**      |   
| :---         |    :----:                    |          ---:          |  
| Numbers of Hits: 1  | Numbers of Hits: 1    | Works as intended      | 
|              |                              |                        | 

![Alt text](assets/manual_testing_images/hit_count_display_empty.png)
![Alt text](assets/manual_testing_images/hit_count_number_of_hits.png)

</details><br>

[Manual Testing](#manual-testing-turns-left-display)
<details>
<summary id="">7. Turns Left Display:</summary>

| **Feature**  | **Expected Behavior**        | **Actual Result**      |   
| :---         |    :----:                    |          ---:          |  
| Turns left: |    Turns left: 9             | Works as intended      |
| Turns left: |    Turns left: 7             | Works as intended      |

![Alt text](assets/manual_testing_images/hit_count_display_empty.png)

![Alt text](assets/manual_testing_images/hit_count_number_of_hits.png)

</details><br>


[Manual Testing](#manual-testing-board-display)
<details>
<summary id="manual-testing-board-display">8. Board Display:</summary>

| **Feature**  | **Instruction**              | **User Input**           | **Expected Behavior**                   | **Actual Behavior** |
| :---         |    :----:                    |          :---:           |   :---:                                 |        ---:         |
| Choose a row | Choose a row (0-5):          | "1"                      | Returns correct row                     | Works as intended   |
| Choose a col | Choose a col (0-5):          | "1"                      | Returns correct col                     | Works as intended   |
|              |                              | Empty input              | Please enter a valid number             | Works as intended   | 
|              |                              | "9"  "10"                | Please pick a valid number (1-5)        | Works as intended   | 

![Alt text](assets/manual_testing_images/row_col_empty_wrong_number.png)



</details><br>

[Manual Testing](#manual-testing-endgame)
<details>
<summary id="manual-testing-endgame">9. Endgame:</summary>

| **Feature**  | **Instruction**              | **User Input**           | **Expected Behavior**                   | **Actual Behavior** |
| :---         |    :----:                    |          :---:           |   :---:                                 |        ---:         |
| Out of Turns! Game over! | Ahooy Sailor! try again? (y/n):|            | Out of Turns! Game over!                | Works as intended   |

![Alt text](assets/manual_testing_images/endgame.png)

</details><br>




[Manual Testing - restarting](#manual-testing-restarting)
<details>
<summary id="manual-testing-restarting">10. Restarting the Game:</summary>

| **Feature**  | **Instruction**              | **User Input**           | **Expected Behavior**                   | **Actual Behavior** |
| :---         |    :----:                    |          :---:           |   :---:                                 |        ---:         |
| Ahooy Sailor! try again? | Ahooy Sailor! try again? (y/n):| "12"       | Please confirm with (y or n) Not a number!| Works as intended   |
| Ahooy Sailor! try again? | Ahooy Sailor! try again? (y/n):| Empty      | Please confirm with (y or n) Not empty space!| Works as intended   |
| Ahooy Sailor! try again? | Ahooy Sailor! try again? (y/n):| y          | clears screen back to Login.            | Works as intended   |
| Ahooy Sailor! try again?| Ahooy Sailor! try again? (y/n):| n          | Thank you for playing! Exiting...       | Works as intended   |



![Alt text](assets/manual_testing_images/restart_fixed_empty_number.png)

![Alt text](assets/manual_testing_images/y_restart.png)

![Alt text](assets/manual_testing_images/n_restart.png)


- Older restart loop:

- **Issue with restart prompt on Empty input.** 

 - ![Alt text](assets/readme_images/restart_empty.png)


- **Issue with restart prompt on Empty input Resolved!** 

- ![Alt text](assets/readme_images/Restart_working.png)

- ![Alt text](assets/readme_images/restart_linter.png)
</details><br>


[Back to top](#)

<br>

### Validator Testing

***keep your Python code neat and PEP 8 friendly.***
[Code Linter](https://pep8ci.herokuapp.com/)

<details><summary>CI Python Linter - Result</summary>

![Alt text](assets/readme_images/new_check_pep8.png)

[Back to top](#)

</details><br>


## Bugs & Fixed Bugs

### Stuck in a login loop, Invalid username.

<details><summary>login test invalid username loop</summary>

![Alt text](assets/readme_images/login_test_invalid_username_loop.png)
https://bobbyhadz.com/blog/python-username-password-input-3-attempts


[Back to top](#)
</details><br>

<details><summary>Very good examples how to setup bccrypt in python.</summary>

https://python.hotexamples.com/examples/bcrypt/-/hashpw/python-hashpw-function-examples.html
https://stackabuse.com/hashing-passwords-in-python-with-bcrypt/
https://www.youtube.com/watch?v=hNa05wr0DSA
https://www.makeuseof.com/tag/encryption-terms/
https://onebite.dev/snippet/python
https://onebite.dev/how-to-make-bcrypt-checkpw-function-work/
https://www.programcreek.com/python/example/81834/bcrypt.hashpw 

</details><br>


<details><summary>Images of the change to bccrypt</summary>

![Alt text](assets/readme_images/bccrypt_password_check.png)

![Alt text](assets/readme_images/Password_check_bccrypt.png)

https://saturncloud.io/blog/how-to-use-the-bcrypt-algorithm-within-the-encrypt-function-in-mysql-for-verifying-passwords/


</details><br>

<details><summary>Fetching the password. Didn't get it to work fully in the end so abandoned the use of Argon2. </summary>

https://inquiryum.com/modules/nodejs%20module/Hashing-Passwords-&-Argon2/


https://www.youtube.com/watch?v=eCBUuu7BPn4
</details><br>

<details><summary>Wrong referenching in the turns_of_play = number_of_turns()</summary>

- ![Alt text](assets/readme_images/numbers_of_turns.png)
- Wrong referenching in the turns_of_play = number_of_turns()  
- print(f"number of turns {turns_of_play}")  # wrong referenching <---- turns_of_play! 

</details><br>

<details><summary>Corrected Wrong referenching in the turns_of_play</summary>

- ![Alt text](assets/readme_images/numbers_of_turns.png)
- Wrong referenching in the turns_of_play = number_of_turns()  
- print(f"number of turns {turns_of_play}")  # wrong referenching <---- turns_of_play! 

</details><br>

<details><summary>Printing the board and and hiding the ships.</summary>


- ![Alt text](assets/readme_images/print_rows_col_board.png)


```python
def print_board(board):
    """ Display the game board in the terminal """
    for i, row in enumerate(board):
        print_row = []
        for j, cell in enumerate(row):
            if cell == 'S':
                print_row.append('*')
            else:
                print_row.append(cell)
        print(" ".join(print_row))

```
![Alt text](<assets/readme_images/Screenshot 2023-08-09 143103.png>)

* Linter error message with the code above. 
''' 
	"code": "unused-variable",
	"severity": 4,
	"message": "Unused variable 'i'",
	"source": "pylint",
			
	"code": "unused-variable",
	"severity": 4,
	"message": "Unused variable 'j'",
	"source": "pylint",
	"startLineNumber": 135,
	'''
* Linter error message resolved. 
 '''
 for row in (board):
        print_row = []
        for cell in (row):
            if cell == 'S':
                print_row.append('*')
            else:
                print_row.append(cell)
        print(" ".join(print_row))
        '''

- ![Alt text](<assets/readme_images/Screenshot 2023-08-09 143410.png>)


</details><br>


<details><summary>Tested function using pythonTutor for step-by-step validation 
checking the cells for hit or miss.</summary>

```python

board_size = 5
total_ships = 10
name = "john"


board = build_board(board_size)
board_with_ships = ships_placement(board, total_ships)


def hit_or_miss(board, row, col):
    if board[row][col] == 'S':
        print(f"Great job Sailor {name}! That's a HIT..")
        return True
    return False


row, col = randint(0, board_size - 1), randint(0, board_size - 1)
test_hit = hit_or_miss(board_with_ships, row, col)


if test_hit:
    board_with_ships[row][col] = 'X'
else:
    board_with_ships[row][col] = 'M'
print_board(board_with_ships)


```
</details><br>

<details><summary>New usersname prompt with validation!</summary>


- More about isnumeric.
- https://stackoverflow.com/questions/63973777/cant-forbid-numbers-from-a-username-that-includes-alphabetical-characters

- ![Number test](<assets/readme_images/checking_for_ numbers.png>)


- ![blank name and number](assets/readme_images/numnber_blank_name.png)  

</details><br>

<details><summary>Restart loop</summary>

- Restart game loop i found. 

- ![Alt text](assets/readme_images/restart_copy.png)
 - https://stackoverflow.com/questions/41718538/how-do-i-insert-a-restart-game-option

- was the same as inside of the game at the end, just looping on 'Y'
- ![Alt text](assets/readme_images/restart1.png)

- ![Alt text](assets/readme_images/restart2.png)

- not looping back to try again jumps back to run main again.
- ![Alt text](assets/readme_images/restart3.png)

- ![Alt text](assets/readme_images/restart4.png)

</details><br>

[Back to top](#)






## Technologies used

[Python](https://www.python.org/)  -  The primary programming language for game development.

[Editor - VScode](https://code.visualstudio.com/)  -  All coding was conducted with this editor.

<br>

[Back to top](#)




### Dependencies
    
   requirements.txt file contains following libraries: 

- gspread
- oauth2client
- bcrypt==3.2.0


### Python Libraries Used

`Import os`
 Used for clearing the terminal screen.

`Import time` 
 Adds pauses or delays in a program.
 
`from random import randint`
 Generates random integers, for random number tasks. 



### Third party Libraries Used



`import gspread` 
 Store/retrieve/modify data in a google Sheet.


`from google.oauth2.service_account import Credentials`
 Permission to modify/access Google services.


`import bcrypt`
Securely hashes passwords, ensures password safety in storage.

`"I have to mention"` using google Sheets to store user data isn't best practice.
  It's due to my database setup limitations, it's utilized for this game.

<br>

## Installation (Cloning the Project)

1. Clone the repository.

2. Rename your repository, if desired.

3. Navigate to the project directory.

4. Run the command `pip install -r requirements.txt` in the terminal.


[Back to top](#)

<br><br>

## Deployment


full detail with screenshots!!!!!! 











[Back to top](#)

<br>


## Credits

<details><summary>Alot of good examples how to setup and use ***bccrypt*** in python</summary>  

* https://python.hotexamples.com/examples/bcrypt/-/hashpw/python-hashpw-function-examples.html
* https://stackabuse.com/hashing-passwords-in-python-with-bcrypt/
* https://www.youtube.com/watch?v=hNa05wr0DSA
* https://www.makeuseof.com/tag/encryption-terms/
* https://onebite.dev/snippet/python
* https://onebite.dev/how-to-make-bcrypt-checkpw-function-work/
* https://www.programcreek.com/python/example/81834/bcrypt.hashpw 


[Back to top](#)

</details><br>

<details><summary>Login / Registration prompt</summary>  
<br>

- After revisiting the "love sandwich" project, I searched the internet until I found something 
- that perfectly matched what I had in mind to enhance the project and make it complete.

<br>

* https://replit.com/talk/share/A-Simple-Login-System-using-Google-Sheets-API/20950
* https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_strip



[Back to top](#)

</details><br>


<details><summary>Password hashing</summary>  


https://pypi.org/project/argon2-cffi/

https://stackoverflow.com/questions/58431973/argon2-library-that-hashes-passwords-without-a-secret-and-with-a-random-salt-tha



[Back to top](#)

</details><br>


<details><summary>Restart the game</summary>  


- https://stackoverflow.com/questions/41718538/how-do-i-insert-a-restart-game-option

- https://stackoverflow.com/questions/63973777/cant-forbid-numbers-from-a-username-that-includes-alphabetical-characters
  

[Back to top](#)

</details><br>

<details><summary>To construct the board</summary>  
  

- https://www.programcreek.com/python/?CodeExample=print+board

- https://stackoverflow.com/questions/63318514/how-output-of-printprint-boardboard-is-printed-like-a-matrix-but-not-like-a


[Back to top](#)

</details><br>


<details><summary>The turns</summary>  


- https://trinket.io/python/051179b6d3

- https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605


[Back to top](#)

</details><br>


## Acknowledgments

I would like to acknowledge my mentor Mo Shami, for staring me in right direction.