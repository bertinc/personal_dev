Public Class CalorieCalc

  Private Const POUNDSTOKG As Double = 0.45359237
  Private kcals As Double = 0
  Private dmWeight As Double
  Private dmSpeed As Double
  Private dmMinutes As Double

  Private Const TABLENAME As String = "dt_met"
  Private DT_MET As DataTable

  Private Const XSDFILENAME As String = "met.xsd"
  Private XSDFolderName As String
  Private XSDFILE As String
  Private Const METFILENAME As String = "met.xml"
  Private METFolderName As String
  Private METFILE As String

  Private Const COL_TYPE As String = "type"
  Private Const COL_SPEED As String = "speed"
  Private Const COL_MET As String = "met"

  Private StringType As Type = Type.GetType("System.String")
  Private DoubleType As Type = Type.GetType("System.Double")


#Region "Constructors/Destructors"

  Public Sub New(ByVal weightPounds As Double, ByVal speedMPH As Double, ByVal timeMinutes As Double)
    dmWeight = weightPounds * POUNDSTOKG
    dmSpeed = speedMPH
    dmMinutes = timeMinutes

    XSDFolderName = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData) & "\SpeedCalc"
    If Not System.IO.Directory.Exists(XSDFolderName) Then
      System.IO.Directory.CreateDirectory(XSDFolderName)
    End If

    XSDFILE = System.IO.Path.Combine(XSDFolderName, XSDFILENAME)

    METFolderName = AppDomain.CurrentDomain.BaseDirectory
    METFILE = System.IO.Path.Combine(METFolderName, METFILENAME)

    InitializeMETData()

    CalculateCalories()
  End Sub


#End Region


#Region "Initialization"

  Private Sub InitializeMETData()

    DT_MET = New DataTable(TABLENAME)
    If System.IO.File.Exists(XSDFILE) Then
      DT_MET.ReadXmlSchema(XSDFILE)
    Else
      DT_MET.Columns.Add(COL_TYPE, StringType)
      DT_MET.Columns.Add(COL_SPEED, DoubleType)
      DT_MET.Columns.Add(COL_MET, DoubleType)
      DT_MET.WriteXmlSchema(XSDFILE)
    End If

    DT_MET.ReadXml(METFILE)

  End Sub

#End Region


#Region "Public Properties"

  ''' <summary>
  ''' Sets the weight.
  ''' </summary>
  ''' <value>The weight.</value>
  Public WriteOnly Property SetWeight As Double
    Set(ByVal value As Double)
      dmWeight = value * POUNDSTOKG
      CalculateCalories()
    End Set
  End Property

  ''' <summary>
  ''' Sets the speed.
  ''' </summary>
  ''' <value>The speed.</value>
  Public WriteOnly Property SetSpeed As Double
    Set(ByVal value As Double)
      dmSpeed = value
      CalculateCalories()
    End Set
  End Property

  ''' <summary>
  ''' Sets the time.
  ''' </summary>
  ''' <value>The time.</value>
  Public WriteOnly Property SetTime As Double
    Set(ByVal value As Double)
      dmMinutes = value
      CalculateCalories()
    End Set
  End Property

  ''' <summary>
  ''' Gets the calories burned.
  ''' </summary>
  ''' <value>The calories burned.</value>
  Public ReadOnly Property CaloriesBurned As Double
    Get
      Return kcals
    End Get
  End Property


#End Region


#Region "Caloried Calculation Methods"

  ''' <summary>
  ''' Searches the MET table by speed and returns the MET value.
  ''' </summary>
  ''' <param name="speed">The speed.</param>
  ''' <returns>The MET value</returns>
  Private Function GetMET(ByVal speed As Double) As Double
    Dim MET As Double = 0

    If Not DT_MET Is Nothing Then
      Dim qry As String = String.Format("{0} = '{1}'", COL_SPEED, speed)
      Dim rows As DataRow() = DT_MET.Select(qry)
      If rows.Count > 0 Then
        MET = rows(0)(COL_MET)
      End If
    End If

    Return MET
  End Function

  ''' <summary>
  ''' Calculates the calories using (MET * Weight / 60) * Minutes
  ''' </summary>
  Private Sub CalculateCalories()

    Dim MET As Double = GetMET(dmSpeed)
    Dim caloriesPerMin As Double = 0

    caloriesPerMin = MET * dmWeight / 60

    kcals = caloriesPerMin * dmMinutes

  End Sub

#End Region


  End Class
