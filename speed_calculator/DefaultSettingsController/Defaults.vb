Imports System.Data
Imports System.IO

''' <summary>
''' AUTHOR: Robert W. Rallison
''' COPYRIGHT: 2011
''' 
''' This class handles all the XML management for saved default settings.  The data is
''' exported and imported using the built in XML features of System.Data.DataTable
''' </summary>
Public Class Defaults
  Private DT_DEFAULTS As DataTable
  Private Const TABLENAME As String = "dt_defaults"
  Private Const DEFAULTSFILENAME As String = "default_settings.xml"
  Private DefaultsFolder As String
  Private Const XSDFILENAME As String = "defaults_settings.xsd"
  Private XSDFolderName As String
  Private XSDFILE As String
  Private SettingsRow As DataRow


#Region "Public CONST Column Keys"

  Public Const COL_HOURS As String = "hours"
  Public Const COL_MINUTES As String = "minutes"
  Public Const COL_SECONDS As String = "seconds"
  Public Const COL_DISTANCE As String = "distance"
  Public Const COL_DIST_UNIT As String = "distance_unit"
  Public Const COL_SPEED As String = "speed"
  Public Const COL_LOCK As String = "option_lock"
  Public Const COL_WEIGHT As String = "weight"

#End Region


#Region "Constructors/Destructors"

  ''' <summary>
  ''' Initializes a new instance of the <see cref="Defaults" /> class.
  ''' Initializes the datatable
  ''' Sets the SettingsRow to nothing
  ''' </summary>
  Public Sub New()

    XSDFolderName = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData) & "\SpeedCalc"
    If Not System.IO.Directory.Exists(XSDFolderName) Then
      Directory.CreateDirectory(XSDFolderName)
    End If

    XSDFILE = Path.Combine(XSDFolderName, XSDFILENAME)

    DefaultsFolder = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments) & "\SpeedCalcDefaults"
    If Not System.IO.Directory.Exists(DefaultsFolder) Then
      Directory.CreateDirectory(DefaultsFolder)
    End If

    InitializeDataTable()
    SettingsRow = Nothing

  End Sub

#End Region


#Region "Initialization Methods"

  ''' <summary>
  ''' Initializes the data table object.  The XSD file is used to initialize the schema if it
  ''' exists.  If it doesn't exist then the schema id difined manually.  After the schema is
  ''' manually difined, the XSD file will be created.
  ''' </summary>
  Private Sub InitializeDataTable()

    DT_DEFAULTS = New DataTable(TABLENAME)

    If File.Exists(XSDFILE) Then
      DT_DEFAULTS.ReadXmlSchema(XSDFILE)
    Else
      DT_DEFAULTS.Columns.Add(COL_HOURS, Type.GetType("System.Int32"))
      DT_DEFAULTS.Columns.Add(COL_MINUTES, Type.GetType("System.Int32"))
      DT_DEFAULTS.Columns.Add(COL_SECONDS, Type.GetType("System.Int32"))
      DT_DEFAULTS.Columns.Add(COL_DISTANCE, Type.GetType("System.Double"))
      DT_DEFAULTS.Columns.Add(COL_DIST_UNIT, Type.GetType("System.Int32"))
      DT_DEFAULTS.Columns.Add(COL_SPEED, Type.GetType("System.Double"))
      DT_DEFAULTS.Columns.Add(COL_LOCK, Type.GetType("System.Int32"))
      DT_DEFAULTS.Columns.Add(COL_WEIGHT, Type.GetType("System.Double"))
      DT_DEFAULTS.WriteXmlSchema(XSDFILE)
    End If

  End Sub

#End Region


#Region "Save To XML Defaults File"

  ''' <summary>
  ''' Creates a datatable using the user input values and saves to the default.xml file.  If it doesn't
  ''' already exist, the datatable will be designed from scratch and the file will be created on writing
  ''' the table to xml.
  ''' </summary>
  ''' <param name="hours">The hours.</param>
  ''' <param name="minutes">The minutes.</param>
  ''' <param name="seconds">The seconds.</param>
  ''' <param name="distance">The distance.</param>
  ''' <param name="distance_unit">The distance_unit.</param>
  ''' <param name="speed">The speed.</param>
  Public Sub SaveDefaults(ByVal hours As Integer, ByVal minutes As Integer, ByVal seconds As Integer, ByVal distance As Double, ByVal distance_unit As Integer, ByVal speed As Double, ByVal lock As Integer, ByVal weight As Double)

    Dim FILENAME As String = Path.Combine(DefaultsFolder, DEFAULTSFILENAME)
    If File.Exists(FILENAME) Then
      DT_DEFAULTS.ReadXml(FILENAME)
      If DT_DEFAULTS.Rows.Count > 0 Then
        SettingsRow = DT_DEFAULTS.Rows(0)
      Else
        SettingsRow = DT_DEFAULTS.NewRow()
        DT_DEFAULTS.Rows.Add(SettingsRow)
      End If
    Else
      SettingsRow = DT_DEFAULTS.NewRow()
      DT_DEFAULTS.Rows.Add(SettingsRow)
    End If

    SettingsRow(COL_HOURS) = hours
    SettingsRow(COL_MINUTES) = minutes
    SettingsRow(COL_SECONDS) = seconds
    SettingsRow(COL_DISTANCE) = distance
    SettingsRow(COL_DIST_UNIT) = distance_unit
    SettingsRow(COL_SPEED) = speed
    SettingsRow(COL_LOCK) = lock
    SettingsRow(COL_WEIGHT) = weight

    DT_DEFAULTS.WriteXml(FILENAME)
  End Sub

#End Region


#Region "Load Frome XML Defaults File"

  ''' <summary>
  ''' Gets the default values from the XML file.  If the files doesn't exist then it returns nothing.
  ''' </summary>
  ''' <value>The defaults row</value>
  Public ReadOnly Property GetDefaults As DataRow
    Get
      Return LoadDefaults()
    End Get
  End Property

  ''' <summary>
  ''' Loads the settings fro the default.xml file if it exists.
  ''' </summary>
  ''' <returns>If the files exists, this will return a data row from the settings file.  Otherwise, it returns nothing.</returns>
  Private Function LoadDefaults() As System.Data.DataRow

    Dim FILENAME As String = Path.Combine(DefaultsFolder, DEFAULTSFILENAME)
    If File.Exists(FILENAME) Then
      DT_DEFAULTS.ReadXml(FILENAME)
      If DT_DEFAULTS.Rows.Count > 0 Then
        SettingsRow = DT_DEFAULTS.Rows(0)
      End If
    End If

    Return SettingsRow
  End Function

#End Region


End Class
