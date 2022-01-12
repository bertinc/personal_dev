''' <summary>
''' AUTHOR: Robert W. Rallison
''' COPYRIGHT: 2011
''' 
''' This is the Speed Calculator.  This program was written to easily estimate the speed
''' required by the runner to finish a run within a certain time.  This program can
''' autocalculate time, speed, and distance based on user input.  It also has quick links
''' for standard distances such as a 5k or a marathon.
''' 
''' Select the value (time, speed, distance) that you would like to calculate and then modify
''' the other two values as needed.
''' 
''' This program currently only supports km and miles.  Speed is always assumed to be in MPH.
''' </summary>
Public Class SpeedCalc

  Private dmTime As Double
  Private dmDistance As Double
  Private dmSpeed As Double
  Private dmWeight As Double

  Private DefaultSpeed As Double
  Private DefaultDistance As Double

  Private noUpdate As Boolean = True
  Private optLock As New RadioList

  Private CalCalc As CalorieCalc


#Region "Private CONSTANTS"

  Private Const KMTOMILESCONV As Double = 0.6214
  Private Const MARATHON As Double = 26.2
  Private Const HALFMARATHON As Double = 13.1
  Private Const FIVEKILOMETERS As Double = 5
  Private Const TENKILOMETERS As Double = 10

#End Region


#Region "Unums: Lock Position, Units, etc..."

  ''' <summary>
  ''' Assumes the inputes come in this order:
  ''' 1) Time
  ''' 2) Distance
  ''' 3) Speed
  ''' </summary>
  Private Enum Lock
    Time = 0
    Distance = 1
    Speed = 2
  End Enum

  ''' <summary>
  ''' Assumes Order:
  ''' 1) miles
  ''' 2) kilometers
  ''' 3) to be decided...
  ''' </summary>
  Private Enum Unit
    miles = 0
    km = 1
  End Enum

#End Region


#Region "Private Properties"

  ''' <summary>
  ''' Gets or sets the distance.  When setting the distance, the property will first
  ''' run the value through the conversion helper method in case the entered value
  ''' was inteneded to be in km instead of miles
  ''' </summary>
  ''' <value>The distance.</value>
  Private Property Distance As Double
    Get
      Return dmDistance
    End Get
    Set(ByVal value As Double)
      dmDistance = ConvertKMtoMiles(value)
    End Set
  End Property

  ''' <summary>
  ''' Gets or sets the time.
  ''' </summary>
  ''' <value>The time.</value>
  Private Property Time As Double
    Get
      Return dmTime
    End Get
    Set(ByVal value As Double)
      dmTime = value
    End Set
  End Property

  ''' <summary>
  ''' Gets or sets the speed.
  ''' </summary>
  ''' <value>The speed.</value>
  Private Property Speed As Double
    Get
      Return dmSpeed
    End Get
    Set(ByVal value As Double)
      dmSpeed = value
    End Set
  End Property

  ''' <summary>
  ''' Gets or sets the weight.
  ''' </summary>
  ''' <value>The weight.</value>
  Private Property Weight As Double
    Get
      Return dmWeight
    End Get
    Set(ByVal value As Double)
      dmWeight = value
    End Set
  End Property

#End Region


#Region "Load/Close"

  Public Sub New()

    ' This call is required by the designer.
    InitializeComponent()

    ' Add any initialization after the InitializeComponent() call.

  End Sub

  Private Sub SpeedCalc_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    DefaultDistance = numDistance.Value
    DefaultSpeed = numSpeed.Value

    optLock = New RadioList
    optLock.AddRadio(radTime)
    optLock.AddRadio(radDistance)
    optLock.AddRadio(radSpeed)

    AddHandler radTime.CheckedChanged, AddressOf optLock_ValueChanged
    AddHandler radDistance.CheckedChanged, AddressOf optLock_ValueChanged
    AddHandler radSpeed.CheckedChanged, AddressOf optLock_ValueChanged

    Dim index As Integer = optLock.CheckedIndex

    cboUnit.SelectedIndex = Unit.miles

    ' initialize the noUpdate to false so it will allow for the time to be initialized
    noUpdate = False
    UpdateValues()

  End Sub

#End Region


#Region "Calculate Values"

  ''' <summary>
  ''' Updates the values based on which radio is selected.  The selected radio is always
  ''' the one to be recalculated.
  ''' NOTE: Speed is always assumed to be MPH
  ''' </summary>
  Private Sub UpdateValues()

    Select Case optLock.CheckedIndex
      Case Lock.Time
        UpdateTime()
      Case Lock.Distance
        UpdateDistance()
      Case Lock.Speed
        UpdateSpeed()

    End Select

    Dim calories As Double
    If CalCalc Is Nothing Then
      CalCalc = New CalorieCalc(200, Speed, Time)
      calories = CalCalc.CaloriesBurned
    Else
      CalCalc.SetSpeed = Speed
      CalCalc.SetTime = Time
      CalCalc.SetWeight = Weight
      calories = CalCalc.CaloriesBurned
      txtCalories.Text = Math.Ceiling(calories).ToString
    End If

  End Sub

  ''' <summary>
  ''' Updates the time where time = 60*distance/speed
  ''' </summary>
  Private Sub UpdateTime()

    If noUpdate Then Return

    Speed = numSpeed.Value
    Distance = numDistance.Value
    Time = (60 * Distance) / Speed

    ' since time is in minutes, we have to convert it manually into hours, minutes, seconds
    Dim hours As Integer = 0
    Dim minutes As Integer = 0
    Dim seconds As Integer = 0

    hours = Math.Truncate(Time / 60)
    minutes = Math.Truncate(Time - (hours * 60))
    seconds = (Time - (minutes + (hours * 60))) * 60
    If seconds / 60 > 0 Then
      minutes += Int(seconds / 60)
      seconds = seconds Mod 60
    End If
    If minutes / 60 > 0 Then
      hours += Int(minutes / 60)
      minutes = minutes Mod 60
    End If

    noUpdate = True

    DisableTime(False)
    numHours.Value = hours
    numMins.Value = minutes
    numSecs.Value = seconds
    DisableTime(True)

    noUpdate = False

  End Sub

  ''' <summary>
  ''' Updates the speed where speed = 60/(time/distance)
  ''' </summary>
  Private Sub UpdateSpeed()

    If noUpdate Then Return

    Distance = numDistance.Value
    Time = (numHours.Value * 60) + numMins.Value + (numSecs.Value / 60)

    Speed = 60 / (Time / Distance)

    noUpdate = True

    DisableSpeed(False)
    numSpeed.Value = Speed
    DisableSpeed(True)

    noUpdate = False

  End Sub

  ''' <summary>
  ''' Updates the distance where distance = time*speed/60
  ''' </summary>
  Private Sub UpdateDistance()

    If noUpdate Then Return

    Speed = numSpeed.Value
    Time = (numHours.Value * 60) + numMins.Value + (numSecs.Value / 60)

    Distance = (Time * Speed) / 60

    noUpdate = True

    DisableDistance(False)
    numDistance.Value = Distance
    DisableDistance(True)

    noUpdate = False

  End Sub

#End Region


#Region "Helper Functions"

  ''' <summary>
  ''' Converts kilometers to miles using a constant of 0.6214 for a conversion factor.
  ''' </summary>
  ''' <param name="value">The value.</param>
  ''' <returns>If the unit is miles then the value is passed back untouched, otherwise a conversion is applied</returns>
  Private Function ConvertKMtoMiles(ByVal value As Double)

    If cboUnit.SelectedIndex = Unit.miles Then Return value

    Dim miles As Double = 0
    Dim km As Double = value

    miles = km * KMTOMILESCONV

    Return miles

  End Function

#End Region


#Region "Enable/Disable Input Tools"

  ''' <summary>
  ''' Sets the time inputs to readonly since that is the value that will be autocalculated
  ''' </summary>
  ''' <param name="val">if true then the time inputs will be readonly</param>
  Private Sub DisableTime(ByVal val As Boolean)
    numHours.ReadOnly = val
    numMins.ReadOnly = val
    numSecs.ReadOnly = val
  End Sub

  ''' <summary>
  ''' Sets the distance input to readonly since that is the value that will be autocalculated
  ''' </summary>
  ''' <param name="val">if true then the distance input will be readonly</param>
  Private Sub DisableDistance(ByVal val As Boolean)
    numDistance.ReadOnly = val
    cboUnit.Enabled = Not val
  End Sub

  ''' <summary>
  ''' Sets the speed input to readonly since that is the value that will be autocalculated
  ''' </summary>
  ''' <param name="val">if true then the speed input will be readonly</param>
  Private Sub DisableSpeed(ByVal val As Boolean)
    numSpeed.ReadOnly = val
  End Sub

#End Region


#Region "Input Change Events"

  ''' <summary>
  ''' When the user selects the radio button, the inputs on that line will be locked to
  ''' user input.  The selection is meant to make sure only one element (time, speed, distance)
  ''' is autocalcualted at a time.
  ''' </summary>
  ''' <param name="sender">The source of the event.</param>
  ''' <param name="e">The <see cref="System.EventArgs" /> instance containing the event data.</param>
  Private Sub optLock_ValueChanged(ByVal sender As System.Object, ByVal e As System.EventArgs)
    Select Case optLock.CheckedIndex
      Case Lock.Time
        DisableTime(True)
        DisableDistance(False)
        DisableSpeed(False)
      Case Lock.Distance
        DisableTime(False)
        DisableDistance(True)
        DisableSpeed(False)
      Case Lock.Speed
        DisableTime(False)
        DisableDistance(False)
        DisableSpeed(True)
    End Select
  End Sub

  Private Sub numHours_ValueChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles numHours.ValueChanged
    UpdateValues()
  End Sub

  Private Sub numMins_ValueChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles numMins.ValueChanged
    UpdateValues()
  End Sub

  Private Sub numSecs_ValueChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles numSecs.ValueChanged
    UpdateValues()
  End Sub

  Private Sub numDistance_ValueChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles numDistance.ValueChanged
    UpdateValues()
  End Sub

  Private Sub numSpeed_ValueChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles numSpeed.ValueChanged
    UpdateValues()
  End Sub

  ''' <summary>
  ''' When the distance unit is changed the locked value needs to be recalculated.
  ''' </summary>
  ''' <param name="sender">The source of the event.</param>
  ''' <param name="e">The <see cref="System.EventArgs" /> instance containing the event data.</param>
  Private Sub cboUnit_ValueChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cboUnit.SelectedIndexChanged
    UpdateValues()
  End Sub

  Private Sub numWeight_ValueChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles numWeight.ValueChanged
    Weight = numWeight.Value
    UpdateValues()
  End Sub

#End Region


#Region "Save/Load Defaults"

  Private Sub btnSaveDefaults_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnSaveDefaults.Click
    Dim defaultSettings As New Defaults()
    defaultSettings.SaveDefaults(numHours.Value, numMins.Value, numSecs.Value, numDistance.Value, cboUnit.SelectedIndex, numSpeed.Value, optLock.CheckedIndex, numWeight.Value)
  End Sub

  Private Sub btnLoadDefaults_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnLoadDefaults.Click
    Dim defaultSettings As New Defaults()
    Dim defaultRow As System.Data.DataRow = defaultSettings.GetDefaults

    If defaultRow Is Nothing Then
      System.Windows.Forms.MessageBox.Show("No default settings found.")
      Return
    End If

    ' first set the locked option so we know what has to be set manually and what has to be calculated
    optLock.CheckedIndex = defaultRow(Defaults.COL_LOCK)

    Select Case optLock.CheckedIndex
      Case Lock.Time ' time is being calculated
        numDistance.Value = defaultRow(Defaults.COL_DISTANCE)
        cboUnit.SelectedIndex = defaultRow(Defaults.COL_DIST_UNIT)
        numSpeed.Value = defaultRow(Defaults.COL_SPEED)

      Case Lock.Distance ' distance is being calculated
        numHours.Value = defaultRow(Defaults.COL_HOURS)
        numMins.Value = defaultRow(Defaults.COL_MINUTES)
        numSecs.Value = defaultRow(Defaults.COL_SECONDS)
        numSpeed.Value = defaultRow(Defaults.COL_SPEED)

        ' need to enable the units drop down list temporarily so we can set the
        ' units based on the saved default
        DisableDistance(False)
        cboUnit.SelectedIndex = defaultRow(Defaults.COL_DIST_UNIT)
        DisableDistance(True)

      Case Lock.Speed ' speed is being calculated
        numHours.Value = defaultRow(Defaults.COL_HOURS)
        numMins.Value = defaultRow(Defaults.COL_MINUTES)
        numSecs.Value = defaultRow(Defaults.COL_SECONDS)
        cboUnit.SelectedIndex = defaultRow(Defaults.COL_DIST_UNIT)
        numDistance.Value = defaultRow(Defaults.COL_DISTANCE)

    End Select

    numWeight.Value = defaultRow(Defaults.COL_WEIGHT)

  End Sub

#End Region


#Region "Distance Quick Links"

  Private Sub link5k_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles link5k.Click
    optLock.CheckedIndex = Lock.Time
    cboUnit.SelectedIndex = Unit.km
    numDistance.Value = FIVEKILOMETERS
  End Sub

  Private Sub link10k_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles link10k.Click
    optLock.CheckedIndex = Lock.Time
    cboUnit.SelectedIndex = Unit.km
    numDistance.Value = TENKILOMETERS
  End Sub

  Private Sub linkHalfMarathon_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles linkHalfMarathon.Click
    optLock.CheckedIndex = Lock.Time
    cboUnit.SelectedIndex = Unit.miles
    numDistance.Value = HALFMARATHON
  End Sub

  Private Sub linkFullMarathon_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles linkFullMarathon.Click
    optLock.CheckedIndex = Lock.Time
    cboUnit.SelectedIndex = Unit.miles
    numDistance.Value = MARATHON
  End Sub

  Private Sub linkReset_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles linkReset.Click
    optLock.CheckedIndex = Lock.Time
    cboUnit.SelectedIndex = Unit.miles
    numDistance.Value = DefaultDistance
    numSpeed.Value = DefaultSpeed
  End Sub

#End Region

  
End Class