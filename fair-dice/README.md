# Fair Dice

### Challenge

Are you willing to throw dices and try your luck at DCTF?

Flag format: DCTF{sha256}

### My solution

Via netcat, we find ourselves in front of :

```
Welcome to a fair dice game.
 - We are going to play some fair rounds. Let's say 101.
 - We both throw one dice. The biggest numbered showed on the dice, wins!
 - The person who wins more rounds from 101, wins that game.
 - If you win too many games in the same session, I am going to alter the game rules to make it fairer for me.
 - If you are going to win four games, I will give you a special code.
 - Note that I am getting bored very fast and I will close this game soon.
Should we start?
Let me show you first 3 dices we are going to play:

Here is the blue dice:

       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  3  xx  6  xx  3  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
Ok?

Here is the yellow dice:

       xxxxxxx
       x     x
       x  5  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  5  xx  5  xx  2  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  2  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  2  x
       x     x
       xxxxxxx
Ok?

Here is the red dice:

       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  4  xx  1  xx  4  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
Ok?
I am chosing the red dice!
What are you choosing? blue / yellow / red:
```

My first reflex is to comute the expected value (scaled by 6) of each dice :
* 3x5 + 6 = 21 for the blue dice
* 2x3 + 5x3 = 21 for the yellow dice
* 5x4 + 1 = 21 for the red dice

To be faiiiiir, I messed up my calculation while doing the challenge lol (I had 15 for the yellow dice for an unknown reason). Also, I know I should have calculated the probability of victory for each challenge, that is : P(B>Y), P(B>R), P(Y>R). With these probabilities, I could have done the perfect solution. Buuuuuuuuut, I was lazy and I had found and OBVIOUSLY worse dice (lol), so throwing only the blue and red dice should win me the game.

About 50% of times, I defeated step 1. Then it was time for step 2, which is as follows :

```
You won with 52 rounds!

Time for second game!

You are two lucky, altering rules!
 - We are playing with the same dices.
 - Each one of us selects 1 color of the playing dice.
 - Each one of us throws 2 times the playing dice and add the numbers together.
 - The biggest number wins.
I am chosing the yellow dice!
What are you choosing? blue / yellow / red:
```

Same strategy as before, onto round 3 :

```
You won with 57 rounds!

Time for third game!

OMG! Again you? You are two lucky, altering rules!
 - We are playing 4 new dices.
 - Same rules as 1st game...
 - You shall not pass!
Let me show you the 4 dices we are going to play:

Here is the blue dice:

       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  3  xx  3  xx  3  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  3  x
       x     x
       xxxxxxx
Ok?

Here is the yellow dice:

       xxxxxxx
       x     x
       x  6  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  6  xx  2  xx  2  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  2  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  2  x
       x     x
       xxxxxxx
Ok?

Here is the red dice:

       xxxxxxx
       x     x
       x  5  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  5  xx  5  xx  1  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  1  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  1  x
       x     x
       xxxxxxx
Ok?

Here is the green dice:

       xxxxxxx
       x     x
       x  0  x
       x     x
       xxxxxxx
xxxxxxxxxxxxxxxxxxxxx
x     xx     xx     x
x  0  xx  4  xx  4  x
x     xx     xx     x
xxxxxxxxxxxxxxxxxxxxx
       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
       xxxxxxx
       x     x
       x  4  x
       x     x
       xxxxxxx
Ok?
```

Expected values (scaled by 6) :
* Blue : 6x3 = 18
* Yellow : 2x6 + 4x2 = 20
* Red : 3x5 + 3x1 = 18
* Green : 4x4 = 16

Here we have a clear leader, and we can expect to win by throwing the yellow dice as often as possible, and throw the blue dice for instance when the program choses the yellow dice. **Please keep in mind that these are not the right calculations to do in order to have the BEST chances to win each round, but this is sufficient for this challenge** if you are willing to restart the script a couple of times (not that many, I promise)

Then round 4 :

```
You won with 52 rounds!

Time for fourth game!

... No words ...  You are two lucky, altering rules!
 - We are playing 4 new dices.
 - Same rules as 2nd game...
 - If you beat me one more time, I am going to give you my flag!
I am chosing the green dice!
What are you choosing? blue / yellow / red / green:
```

Same strategy, and we get the flag.

```
You won with 55 rounds!
DCTF{...}
Good luck.
```
