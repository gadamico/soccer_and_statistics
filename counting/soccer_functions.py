def standings(results):
    """This function will return a DataFrame of the rankings
    of Teams a, b, c, and d given an input string of the
    outcomes of the six games, where those games are arranged
    in the following order: a vs. b, a vs. c, a vs. d, b vs. c,
    b vs. d, c vs. d."""
    import numpy as np
    import pandas as pd
    
    # Initialize the point totals at 0
    a = 0
    b = 0
    c = 0
    d = 0
    
    # Identify the ties in the outcome string
    ties = [j for j in range(6) if results[j] == 't']
    
    # Assign the ties' points accordingly
    if 0 in ties:
        a += 1
        b += 1
    if 1 in ties:
        a += 1
        c += 1
    if 2 in ties:
        a += 1
        d += 1
    if 3 in ties:
        b += 1
        c += 1
    if 4 in ties:
        b += 1
        d += 1
    if 5 in ties:
        c += 1
        d += 1
    
    # Assign the wins' points accordingly
    a += 3*results.count('a')
    b += 3*results.count('b')
    c += 3*results.count('c')
    d += 3*results.count('d')
    
    return pd.DataFrame(np.array([a, b, c, d]),
                     index=['a', 'b', 'c', 'd'],
                       columns=['points']).sort_values(by='points', ascending=False)

def standings_n_teams(results, n=4, verbose=1):
    
    """This function will return the standings as an array for a
    given outcome string. The results should be arranged in
    'alphabetical' order so that all of Team A's games come first,
    followed by the remaining games of Team B, etc."""
    
    import numpy as np
    import pandas as pd
    import string
    
    # We'll calculate the number of games and possibilities.
    if verbose == 1:
        games = n*(n-1)//2
        print(f"For {n} teams there will be {games} games and so {3**games} possibilities.")
    
    # Initialize the point totals at 0
    points = np.zeros(n).astype(int)
    
    # Calculating points
    for num in range(len(results)):
        
        # For any letter other than 't', we'll simply add 3
        # points to the relevant place in the points array.
        pos = string.ascii_lowercase.index(results[num])
        if pos != 19:
            points[pos] += 3
        
        # Otherwise, we'll need to figure out which two teams
        # have tied.
        else:
            
            # Since Team A's games are listed first, we'll see
            # if the position of the 't' is small enough to be
            # in that range. If not, then we'll check to see if
            # it's small enough to be in the list of Team B's
            # games. Etc.
            first_team = 1
            test = n - 1
            if num + 1 > test:
                while num + 1 > test:
                    first_team += 1
                    
                    # This `temp` variable will keep track of the
                    # the "distance" between the two teams.
                    temp = test
                    test += n - first_team
            else:
                temp = 0
            second_team = first_team + (num + 1 - temp)
            points[first_team - 1] += 1
            points[second_team - 1] += 1
    
    return np.array(sorted(points)[::-1])

def sequences(arr):
    """
    We assume that we want to build a sequence of characters
    of a given length where we have a set of choices for each
    position in the sequence. This function generates all possible
    such sequences. The function assumes that all choice sets have
    the same length.
    
    Example
    --------
    
    sequences(['ab', 'cd']) = ['ac', 'ad', 'bc', 'bd']
    
    """
    
    import itertools as it
    import numpy as np
    
    out = []
    j = len(arr)
    k = len(arr[0])
    
    # Initialize an empty array
    seqs = np.char.array([np.zeros(j) for _ in range(k**j)])
    
    for num, elem in enumerate(arr):
        seq = []
        
        while len(seq) != k**j:
            for opt in range(k):
                seq.extend(list(it.repeat(elem[opt], k**(j-num-1))))

        seqs[:, num] = np.char.array(seq)
    
    return [''.join(seq) for seq in seqs.astype(str)]