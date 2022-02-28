
# CPE 101: Fundamentals of Computer Science

## Project 2: Lunar Lander Simulator

- Practice writing loops in Python
- Practice writing and calling functions that you have written
- Practice testing your code

You are part of a team writing a program that simulates landing the Lunar Module (LM) from the Apollo space program on the moon. The simulation picks up when the retrorockets cut off and the pilot/astronaut takes over control of the LM. The user of the simulator specifies the initial amount of fuel and initial altitude. The LM starts at a user-specified altitude with an initial velocity of zero meters per second and has a user-specified amount of fuel on board.

The manual thrusters are off and the LM is in free-fall -- meaning that lunar gravity is causing the LM to accelerate toward the surface according to the gravitational constant for the moon. The pilot can control the rate of descent using the thrusters of the LM. The thrusters are controlled by entering integer values from 0 to 9 which represent the rate of fuel flow. A value of 5 maintains the current velocity, 0 means free-fall, 9 means maximum thrust -- all other values are a variation of those possibilities and can be calculated with an equation that is provided below.

To make things interesting (and to reflect reality) the LM has a limited amount of fuel -- if you run out of fuel before touching down you have lost control of the LM and it freefalls to the surface.

The goal is to land the LM on the surface with a velocity between 0 and -1 meters per second, inclusive, using the least amount of fuel possible. A landing velocity between -1 meters per second and -10 meters per second (exclusive) means you survive but the LM is damaged and will not be able to leave the surface of the moon -- you will be able to enjoy the surface of the moon as long as your oxygen lasts but you will not leave the moon alive. Velocities faster than (less than) or equal to -10 meters per second mean the LM sustains severe damage and you die immediately.


## Project 3: Calcudoku

- Write a program requiring use of loops and lists

For this program, you will be writing a solver for 5x5 Calcudoku puzzles. A Calcudoku puzzle is an NxN grid where the solution satisfies the following:
each row can only have the numbers 1 through N with no duplicates
• each column can only have the numbers 1 through N with no duplicates
• the sum of the numbers in a “cage” (areas with a bold border) should equal the
number shown in the upper left portion of the cage

## Project 4: Word Search

- practice working with strings
- understand conditional logic, loops, lists, functions

n this project, you will implement a program which locates words in common word search 
puzzles (all puzzles are 10x10).

Words can appear in the puzzle running up, down, forward, backward, or diagonal 
(down/right only). You do not need to check other diagonal directions (up/right, up/left, 
down/left).

Your program will begin by reading in the puzzle and words to search for.  You will not prompt 
the user for the input, simply assume they will type it.  You may assume all input will be valid 
input.

Puzzle - Your program should read in a 100 character long string from user via standard 
keyboard input.

## Project 5: 

- practice on a 2D python list
- practice sorting algorithms
- practice reading from a file
- practice writing to a file

In commercial data processing, it’s common to have several files in each system. In an 
accounts receivable system, for example, there is generally a master file containing detailed 
information about each customer such as the customer’s name, address, telephone number, 
outstanding balance, credit limit, discount terms, contract arrangements and possibly a 
condensed history of recent purchases and cash payments. In this program we only stored the 
customers’ account number, customers’ first and last name, customer’s balance, customers’ 
phone number, and customers’ city. 

As transactions occur (i.e., sales are made and cash payments arrive in the mail), they’re 
entered into a file. At the end of each business period (i.e., a month for some companies, a week 
for others and a day in some cases) the file of transactions (called "transaction.dat") is applied to 
the master file (called "oldMaster.dat"), thus updating each account's record of purchases and 
payments. After each of these updates, the master file is rewritten as a new file 
("newMaster.dat"), which is then used at the end of the next business period to begin the 
updating process again.

File-matching programs must deal with certain problems that do not exist in single-file 
programs. For example, a match does not always occur. A customer on the master file might not 
have made any purchases or cash payments in the current business period, and therefore no 
record for this customer will appear on the transaction file. Similarly, a customer who did make 
some purchases or cash payments might have just moved to this community and the company 
may not have had a chance to create a master record for this customer. 

Use the account number on each file as the record key for matching purposes. The 
oldMaster.dat is not ordered. You need to read the file and generate a sequential file which is 
sorted in increasing account number order. This sequential file will be sorted_oldMaster.dat. 
The transaction.dat file is a sequential file with records stored in increasing account number 
order. 

When a match occurs (i.e., records with the same account number appear on both the master file 
and the transaction file), add the dollar amount on the transaction file to the current balance on 
the master file and write the "newMaster.dat" record. (Assume that purchases are indicated by 
positive amounts on the transaction file, and that payments are indicated by negative amounts.) 
When there is a master record for a particular account but no corresponding transaction record, 
merely write the master record to "newMaster.dat". When there is a transaction record but no 
corresponding master record, print the message "Unmatched transaction record for account 
number ..." (fill in the account number from the transaction record) 


