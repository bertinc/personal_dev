Public Class Main

  Private Sub btnGo_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnGo.Click
    Dim files As String() = Me.txtFilenames.Text.Split(",")
    Dim dir As String = Me.txtDir.Text

    For fileCnt As Integer = 0 To files.Length - 1
      Dim fileReader As New System.IO.StreamReader(dir & files(fileCnt))
      Dim lines As New System.Collections.ArrayList

      With fileReader
        While Not .EndOfStream
          lines.Add(.ReadLine())
        End While
      End With

      fileReader.Close()

      Dim fileWriter As New System.IO.StreamWriter(dir & files(fileCnt))

      For i As Integer = 0 To lines.Count - 1
        If lines.Item(i).ToString = Me.txtSearchLineAfter.Text Then
          fileWriter.WriteLine(lines.Item(i).ToString)
          fileWriter.WriteLine(Me.txtAddAfter.Text)
          i += 1
        End If
        If lines.Item(i).ToString = Me.txtSearchLineBefore.Text Then
          fileWriter.WriteLine(Me.txtAddBefore.Text)
        End If
        fileWriter.WriteLine(lines.Item(i).ToString)
      Next

      fileWriter.Flush()
      fileWriter.Close()
    Next

  End Sub

  Private Sub btnDir_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnDir.Click
    Me.ofdDirectory.ShowDialog()
    Dim fileName As String = Me.ofdDirectory.FileName
    Dim dirArray As String() = fileName.Split("\")
    fileName = String.Empty
    For i As Integer = 0 To dirArray.Length - 2
      fileName = fileName & dirArray(i) & "\"
    Next
    Me.txtDir.Text = fileName

    Dim files As String = String.Empty
    With Me.ofdDirectory
      For j As Integer = 0 To Me.ofdDirectory.FileNames.Length - 1
        Dim tempArray As String() = .FileNames(j).Split("\")
        files = files & tempArray(tempArray.Length - 1) & ","
      Next
    End With

    Me.txtFilenames.Text = files.Remove(files.Length - 1, 1)
    
  End Sub
End Class
