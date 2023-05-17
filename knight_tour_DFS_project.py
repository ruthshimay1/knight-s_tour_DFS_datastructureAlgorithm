
"""A program that address the classic Knight's tour problem by implementing a graph,
utilizing a depth first search algorithm and optimized by observing heuristics -
the Warnsdorf’s algorithm.  .

"""
print("A knight's Tour around a chessboard, \nshowing the path using vertices:\n")

import sys

class KnightsTour:
    """A class to create the chessboard of size wxh """
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.board = []
        self.generate_board()

    def generate_board(self):
        """
        Creates a nested list to represent the game board. It is an
        array equal to the number of vertices and all coordinates
        would be initiated to zero (empty) before visted.
        (i.e, the board will be filled with all zeros at first.
        """
        for i in range(self.h):
            self.board.append([0]*self.w)

    def print_board(self):
        '''Printing the the chessboard with all the moves in an easy to follow format.'''
        
        print( '\n' )
        print( "A Knight's tour around a chessboard \
\nstarting at 1 and it's subsiquent moves:  ")
        print( "------------------------------------" )
        for elem in self.board:
            print( ' \n',    elem, '\n' )
        print( "-------------------------------------" )       

    def generate_legal_moves(self, cur_pos):
        """
        Generates a list of legal moves the knight cam make 
        from the current position at position (i,j).
        
        """
        possible_pos = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]  #the eight possible movements for a knight

        for move in move_offsets:
            new_i = cur_pos[0] + move[0]
            new_j = cur_pos[1] + move[1]  
            
            #note that a knight cannot go out of the chessboard 
            if (new_i >= self.h) or (new_i < 0) or \
                (new_j >= self.w) or (new_j < 0):     #checks coordinates are within the chessboard
                continue

            else:
                possible_pos.append((new_i, new_j))

        return possible_pos

    def sort_lonely_neighbors(self, to_visit):
        """
        It is more efficient to visit the lonely neighbors first, 
        since these are at the edges of the chessboard and cannot 
        be reached easily if done later in the traversal.
        """
        neighbor_list = self.generate_legal_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            np_value = self.board[neighbor[0]][neighbor[1]]
            if np_value == 0:       #checking if that adjacent vertex is not visited
                empty_neighbours.append(neighbor)

        scores = []       #a list of positions and the number of moves possible
        for empty in empty_neighbours:
            score = [empty, 0]        #coordinate, with it's max number of possobile move from that coordinate
            moves = self.generate_legal_moves(empty)  # Generate legal moves using the coordinates empty as cur_pos
            for m in moves:
                if self.board[m[0]][m[1]] == 0: #if you find unvisted(empty) coordinate, increment score(finding nun of edges from a vertes)
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key = lambda s: s[1]) #sort coordinates by their number of connections(moves)
        sorted_neighbours = [s[0] for s in scores_sort]    #store the sorted coordinate in sorted_neighbours and return result
        return sorted_neighbours

    def tour(self, n, path, to_visit):
        """
        Recursive definition of knights tour. where:
        n = current depth of search tree
        path = current path taken
        to_visit = node to visit
        """
       
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit) #append the newest vertex to the current point
        
        print( to_visit,'->', end = ' ' )
        

        if n == self.w * self.h: #if every coordinate(vertex) is visited then print boart and exit
            self.print_board()
            sys.exit(0)

        else:                   #knight should tour recursively with the updated n
            sorted_neighbours = self.sort_lonely_neighbors(to_visit)
            for neighbor in sorted_neighbours:
                self.tour(n+1, path, neighbor)

            #If we exit the loop bofore we reach our goal because of a dead end then we backtrack
            self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
                print( "Going back to: ", path[-1] ) #implicitly using stack since it's recursive
            except IndexError:
                print( "No path found" )
                sys.exit(0)
                
#Testing the program
if __name__ == '__main__':
    #Instantiating an object to create an 8x8 chessboard.
    K_tour = KnightsTour(8, 8)
    K_tour.tour(1, [], (0,0))
    K_tour.print_board()