# soccer_and_statistics

This repository explores statistical questions that arise in the context of soccer competition.

In the first part of a soccer tournament (like the World Cup) teams are often divided into groups, and every team in that group will play every other team in that group. The results of this "round-robin" play will determine the teams to advance to the single-elimination tournament (or "knockout round"). A team will earn three points for a win and one point for a tie.

Very often a group will comprise four teams. For a four-team group, how many different game outcomes are possible? How many different sets of final standings are possible? **How many different sets of final standings are possible if we abstract away from the team identities?**

This last question is what I want to pursue here. As we shall see, the complexity of this problem grows quickly as we increase the number of teams in our group.

The notebook begins by exploring a simple case of a two-team group and then works up to the more typical cases in international soccer of four- and five-team groups. For a group of $n$ teams, there will be $\binom{n}{2}$ games and, since each game has three possible outcomes (win, lose, or draw), there will therefore be $3^{\bin{n}{2}}$ possible results. But this number counts certain possible final standings multiple times. Most obviously, this number doesn't abstract away from the identities of the teams themselves.

In the course of our calculations, I develop a function that will count the possible results of a string of games, where each game is represented as a string of possible outcomes (one character per outcome). This function, called "sequences", may be of use whenever we want to construct a list of all possible sequences, where each position in the sequence has a finite number of options.

For a four-team group (as found in the World Cup), the answer to our original question turns out to be 40. There are 40 different possible standings of a four-team group where winning teams earn 3 points and tying teams earn 1.

## Navigation

The soccer_and_statistics.ipynb notebook file walks through our problem. It makes use of a few homegrown functions that are stored in the soccer_functions.py Python file inside the counting folder.
