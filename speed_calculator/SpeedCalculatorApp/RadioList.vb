''' <summary>
''' AUTHOR: Robert W. Rallison
''' COPYRIGHT: 2011
''' 
''' This class is basically a radio button group to make it easy to check which
''' one is checked at any time and to check a radio by index
''' </summary>
Public Class RadioList

  Private buttonList As Dictionary(Of RadioButton, Integer)
  Private noCheckedEvent As Boolean = False


#Region "Constructors/Destructors"

  Public Sub New()
    buttonList = New Dictionary(Of RadioButton, Integer)()
  End Sub

#End Region

  
#Region "Public Methods"

  ''' <summary>
  ''' Adds the radio button to the dictionary
  ''' </summary>
  ''' <param name="rad">The radio button object</param>
  Public Sub AddRadio(ByVal rad As RadioButton)
    buttonList.Add(rad, buttonList.Count)
  End Sub

  ''' <summary>
  ''' Gets or sets which radio button is checked
  ''' </summary>
  ''' <value>The index of the radio button to make checked</value>
  Public Property CheckedIndex As Integer
    Get
      Dim index As Integer = -1

      For Each radio As RadioButton In buttonList.Keys
        If radio.Checked Then
          index = buttonList(radio)
          Exit For
        End If
      Next

      Return index
    End Get

    Set(ByVal value As Integer)
      Dim updateRad As New RadioButton
      For Each radio As RadioButton In buttonList.Keys
        If buttonList(radio) = value Then
          updateRad = radio
          Exit For
        End If
      Next
      updateRad.Checked = True
    End Set
  End Property

#End Region
  

End Class
