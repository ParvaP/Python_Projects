def eraseTable (tab):
   '''
   (list) -> None
   This function prepares the game table (array) 
   by putting '-' in all the elements.
   It does not create a new array
   Preconditions: tab is a reference to an nxn array matrice n x n that contains '-', 'X' or 'O'
   '''
   
    # to complete
   for row in range(len(tab)):
       for col in range(len(tab[row])):
          tab[row][col]='-'

    # returns nothing

def verifyWin(tab):
    '''(list) ->  bool
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    * Verify if there is a winner.
    * Look for 3 X's and O's in a row, column, and diagonal.
    * If we find one, we display the winner (the message "Player X has won"
    * or "Player O has won!") and returns True.
    * If there is a draw (verify it with the function testdraw),
    * display "It is a draw" and returns True.
    * If the game is not over, returns False.
    * The function call the functions testrows, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Those functions returns the winner 'X' or 'O', or '-' if there is no winner.
    '''
    if testRows(tab) == 'X' or testRows(tab) ==  'O':
       print("Player",testRows(tab),"has won!")
       return True
    if testCols(tab) == 'X' or testCols(tab) == 'O':
       print("Player", testCols(tab), "has won!")
       return True
    if testDiags(tab) == 'X' or testDiags(tab) == 'O':
       print("Player", testDiags(tab), "has won!")
       return True
    # to complete
    if testDraw(tab)==True:
       print("Draw")
       return True

    return False  # to change

 
def testRows(tab):
   ''' (list) ->  str
   * verify if there is a winning row.
   * Look for three 'X' or three 'O' in a row.  
   * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   for row in range(len(tab)):
      if tab[row][0] == 'X' and tab[row][1] == 'X' and tab[row][2] == 'X':
         return 'X'
      elif tab[row][0] == 'O' and tab[row][1] == 'O' and tab[row][2] == 'O':
         return 'O'
   # to complete
  
   return '-' # to be modified so that it returns the winner, or '-' if there is no winner 


  
def testCols(tab):
   ''' (list) ->  str
   * verify a winning column.
   * look for three 'X' or three 'O' in a column.  
   * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   for col in range(len(tab[0])):
         if tab[0][col] == 'X' and tab[1][col] == 'X' and tab[2][col] == 'X':
            return'X'
         elif tab[0][col] == 'O' and tab[1][col] == 'O' and tab[2][col] == 'O':
            return 'O'
   # to complete
  
   return '-'   #to be modified so that it returns the winner, or '-' if there is no winner

   
def testDiags(tab):
   ''' (list) ->  str
   * Look for three 'X' or three 'O' in a diagonal.  
   * If it is the case, the character 'X' or 'O' is returned
   * otherwise '-' is returned.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   if tab[0][0] == 'X' and tab[1][1] == 'X' and tab[2][2] == 'X':
      return 'X'
   elif tab[2][0] == 'X' and tab[1][1] == 'X' and tab[0][2] == 'X':
      return 'X'
   elif tab[0][0] == 'O' and tab[1][1] == 'O' and tab[2][2] == 'O':
      return 'O'
   elif tab[2][0] == 'O' and tab[1][1] == 'O' and tab[0][2] == 'O':
      return 'O'


   # to complete
    
   return '-'   # #to be modified so that it returns the winner, or '-' if there is no winner

  
  
def testDraw(tab):
   ''' (list) ->  bool
   * verify if there is a draw
   * check if all the array elements have X or O, not '-'.  
   * If we do not find find any '-' in the array, return True. 
   * If there is any '-', return false.
   * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
   '''
   for row in range(len(tab)):
      for col in range(len(tab[row])):
         if tab[row][col] == '-':
            return False
   # to complete
  
   return True  # to BE modiffied

