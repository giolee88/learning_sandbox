Sub CheckerBoard()

  ' Create an array to hold the two color options
  Dim color_options(2) As Integer

  ' Setup a counter to track cell number
  Dim cellnumber as Integer
  cellnumber = 1

  ' Loop through each row of the board
  For i = 1 to 8

    ' Loop through each column of the board
    For j = 1 to 8

      ' If we are on a cell that is divisible by 2 then color it red
      If (cellnumber mod 2 = 0) then

        Cells(i, j).Interior.ColorIndex = 1

      ' Otherwise color it black
      Else

        Cells(i, j).Interior.ColorIndex = 3

      End if

      ' Add one to our cell number each time
      cellnumber = cellnumber + 1

    Next j

    ' Whenever we start on a new row, we also add one to the cell number (to create the alternation)
    cellnumber = cellnumber + 1

  Next i

End Sub
