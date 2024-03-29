'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_member_following=social_graph[from_member]["following"] 
    to_member_following=social_graph[to_member]["following"] 
    if from_member in to_member_following and to_member in from_member_following:
        return "friends"
    elif from_member in to_member_following:
        return "followed by"
    elif to_member in from_member_following:
        return "follower"
    else: return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for rows in board:
        if len(board)>len(rows):
            break
        if len(set(rows))==1:
            return (rows[0])
        break
    
    column_matrix=[[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    for columns in column_matrix:
        if len(board)>len(columns):
            break
        if len(set(columns))==1:
            return (columns[0])
        break
    
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return (board[0][0])
    elif len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return (board[0][len(board)-1])
    else: return("NO WINNER")

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    circle_route = []
    route_time = []
    time_sum = 0
    running = False
 
    if first_stop == second_stop:
        return time_sum
    for key, value in route_map.items():
        circle_route.append(key)
        route_time.append(value['travel_time_mins'])
    routes = list(zip(circle_route, route_time))
    for route in routes:
        if first_stop == route[0][0]:
            running = True
        if running:
            time_sum += route[1]
        if second_stop == route[0][1]:
            break
    return time_sum