<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class SpeedCalc
  Inherits System.Windows.Forms.Form

  'Form overrides dispose to clean up the component list.
  <System.Diagnostics.DebuggerNonUserCode()> _
  Protected Overrides Sub Dispose(ByVal disposing As Boolean)
    Try
      If disposing AndAlso components IsNot Nothing Then
        components.Dispose()
      End If
    Finally
      MyBase.Dispose(disposing)
    End Try
  End Sub

  'Required by the Windows Form Designer
  Private components As System.ComponentModel.IContainer

  'NOTE: The following procedure is required by the Windows Form Designer
  'It can be modified using the Windows Form Designer.  
  'Do not modify it using the code editor.
  <System.Diagnostics.DebuggerStepThrough()> _
  Private Sub InitializeComponent()
    Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(SpeedCalc))
    Me.numSecs = New System.Windows.Forms.NumericUpDown()
    Me.numMins = New System.Windows.Forms.NumericUpDown()
    Me.numHours = New System.Windows.Forms.NumericUpDown()
    Me.numDistance = New System.Windows.Forms.NumericUpDown()
    Me.numSpeed = New System.Windows.Forms.NumericUpDown()
    Me.Label1 = New System.Windows.Forms.Label()
    Me.Label2 = New System.Windows.Forms.Label()
    Me.Label3 = New System.Windows.Forms.Label()
    Me.Label4 = New System.Windows.Forms.Label()
    Me.link5k = New System.Windows.Forms.Label()
    Me.linkHalfMarathon = New System.Windows.Forms.Label()
    Me.link10k = New System.Windows.Forms.Label()
    Me.linkFullMarathon = New System.Windows.Forms.Label()
    Me.linkReset = New System.Windows.Forms.Label()
    Me.btnSaveDefaults = New System.Windows.Forms.Button()
    Me.btnLoadDefaults = New System.Windows.Forms.Button()
    Me.picRunner = New System.Windows.Forms.PictureBox()
    Me.cboUnit = New System.Windows.Forms.ComboBox()
    Me.radTime = New System.Windows.Forms.RadioButton()
    Me.radDistance = New System.Windows.Forms.RadioButton()
    Me.radSpeed = New System.Windows.Forms.RadioButton()
    Me.numWeight = New System.Windows.Forms.NumericUpDown()
    Me.txtCalories = New System.Windows.Forms.TextBox()
    Me.Label5 = New System.Windows.Forms.Label()
    Me.Label6 = New System.Windows.Forms.Label()
    CType(Me.numSecs, System.ComponentModel.ISupportInitialize).BeginInit()
    CType(Me.numMins, System.ComponentModel.ISupportInitialize).BeginInit()
    CType(Me.numHours, System.ComponentModel.ISupportInitialize).BeginInit()
    CType(Me.numDistance, System.ComponentModel.ISupportInitialize).BeginInit()
    CType(Me.numSpeed, System.ComponentModel.ISupportInitialize).BeginInit()
    CType(Me.picRunner, System.ComponentModel.ISupportInitialize).BeginInit()
    CType(Me.numWeight, System.ComponentModel.ISupportInitialize).BeginInit()
    Me.SuspendLayout()
    '
    'numSecs
    '
    Me.numSecs.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.numSecs.Location = New System.Drawing.Point(332, 16)
    Me.numSecs.Maximum = New Decimal(New Integer() {59, 0, 0, 0})
    Me.numSecs.Name = "numSecs"
    Me.numSecs.Size = New System.Drawing.Size(65, 44)
    Me.numSecs.TabIndex = 21
    Me.numSecs.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
    '
    'numMins
    '
    Me.numMins.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.numMins.Location = New System.Drawing.Point(235, 16)
    Me.numMins.Maximum = New Decimal(New Integer() {59, 0, 0, 0})
    Me.numMins.Name = "numMins"
    Me.numMins.Size = New System.Drawing.Size(65, 44)
    Me.numMins.TabIndex = 22
    Me.numMins.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
    '
    'numHours
    '
    Me.numHours.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.numHours.Location = New System.Drawing.Point(138, 16)
    Me.numHours.Maximum = New Decimal(New Integer() {99, 0, 0, 0})
    Me.numHours.Name = "numHours"
    Me.numHours.Size = New System.Drawing.Size(65, 44)
    Me.numHours.TabIndex = 23
    Me.numHours.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
    '
    'numDistance
    '
    Me.numDistance.DecimalPlaces = 1
    Me.numDistance.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.numDistance.Increment = New Decimal(New Integer() {1, 0, 0, 65536})
    Me.numDistance.Location = New System.Drawing.Point(279, 66)
    Me.numDistance.Maximum = New Decimal(New Integer() {99999, 0, 0, 65536})
    Me.numDistance.Minimum = New Decimal(New Integer() {1, 0, 0, 65536})
    Me.numDistance.Name = "numDistance"
    Me.numDistance.Size = New System.Drawing.Size(118, 44)
    Me.numDistance.TabIndex = 24
    Me.numDistance.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
    Me.numDistance.Value = New Decimal(New Integer() {3, 0, 0, 0})
    '
    'numSpeed
    '
    Me.numSpeed.DecimalPlaces = 1
    Me.numSpeed.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.numSpeed.Increment = New Decimal(New Integer() {1, 0, 0, 65536})
    Me.numSpeed.Location = New System.Drawing.Point(264, 116)
    Me.numSpeed.Maximum = New Decimal(New Integer() {9999, 0, 0, 65536})
    Me.numSpeed.Minimum = New Decimal(New Integer() {1, 0, 0, 65536})
    Me.numSpeed.Name = "numSpeed"
    Me.numSpeed.Size = New System.Drawing.Size(133, 44)
    Me.numSpeed.TabIndex = 25
    Me.numSpeed.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
    Me.numSpeed.Value = New Decimal(New Integer() {6, 0, 0, 0})
    '
    'Label1
    '
    Me.Label1.AutoSize = True
    Me.Label1.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.Label1.Location = New System.Drawing.Point(38, 18)
    Me.Label1.Name = "Label1"
    Me.Label1.Size = New System.Drawing.Size(97, 37)
    Me.Label1.TabIndex = 26
    Me.Label1.Text = "Time:"
    '
    'Label2
    '
    Me.Label2.AutoSize = True
    Me.Label2.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.Label2.Location = New System.Drawing.Point(38, 68)
    Me.Label2.Name = "Label2"
    Me.Label2.Size = New System.Drawing.Size(150, 37)
    Me.Label2.TabIndex = 27
    Me.Label2.Text = "Distance:"
    '
    'Label3
    '
    Me.Label3.AutoSize = True
    Me.Label3.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.Label3.Location = New System.Drawing.Point(38, 118)
    Me.Label3.Name = "Label3"
    Me.Label3.Size = New System.Drawing.Size(218, 37)
    Me.Label3.TabIndex = 28
    Me.Label3.Text = "Speed (MPH):"
    '
    'Label4
    '
    Me.Label4.AutoSize = True
    Me.Label4.Font = New System.Drawing.Font("Microsoft Sans Serif", 18.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.Label4.Location = New System.Drawing.Point(40, 173)
    Me.Label4.Name = "Label4"
    Me.Label4.Size = New System.Drawing.Size(236, 29)
    Me.Label4.TabIndex = 29
    Me.Label4.Text = "Distance Quick Links"
    '
    'link5k
    '
    Me.link5k.AutoSize = True
    Me.link5k.Font = New System.Drawing.Font("Microsoft Sans Serif", 18.0!, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.link5k.ForeColor = System.Drawing.Color.Blue
    Me.link5k.Location = New System.Drawing.Point(40, 208)
    Me.link5k.Name = "link5k"
    Me.link5k.Size = New System.Drawing.Size(38, 29)
    Me.link5k.TabIndex = 30
    Me.link5k.Text = "5k"
    '
    'linkHalfMarathon
    '
    Me.linkHalfMarathon.AutoSize = True
    Me.linkHalfMarathon.Font = New System.Drawing.Font("Microsoft Sans Serif", 18.0!, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.linkHalfMarathon.ForeColor = System.Drawing.Color.Blue
    Me.linkHalfMarathon.Location = New System.Drawing.Point(40, 266)
    Me.linkHalfMarathon.Name = "linkHalfMarathon"
    Me.linkHalfMarathon.Size = New System.Drawing.Size(161, 29)
    Me.linkHalfMarathon.TabIndex = 31
    Me.linkHalfMarathon.Text = "Half Marathon"
    '
    'link10k
    '
    Me.link10k.AutoSize = True
    Me.link10k.Font = New System.Drawing.Font("Microsoft Sans Serif", 18.0!, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.link10k.ForeColor = System.Drawing.Color.Blue
    Me.link10k.Location = New System.Drawing.Point(40, 237)
    Me.link10k.Name = "link10k"
    Me.link10k.Size = New System.Drawing.Size(51, 29)
    Me.link10k.TabIndex = 32
    Me.link10k.Text = "10k"
    '
    'linkFullMarathon
    '
    Me.linkFullMarathon.AutoSize = True
    Me.linkFullMarathon.Font = New System.Drawing.Font("Microsoft Sans Serif", 18.0!, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.linkFullMarathon.ForeColor = System.Drawing.Color.Blue
    Me.linkFullMarathon.Location = New System.Drawing.Point(40, 295)
    Me.linkFullMarathon.Name = "linkFullMarathon"
    Me.linkFullMarathon.Size = New System.Drawing.Size(113, 29)
    Me.linkFullMarathon.TabIndex = 33
    Me.linkFullMarathon.Text = "Marathon"
    '
    'linkReset
    '
    Me.linkReset.AutoSize = True
    Me.linkReset.Font = New System.Drawing.Font("Microsoft Sans Serif", 18.0!, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.linkReset.ForeColor = System.Drawing.Color.Blue
    Me.linkReset.Location = New System.Drawing.Point(40, 324)
    Me.linkReset.Name = "linkReset"
    Me.linkReset.Size = New System.Drawing.Size(94, 29)
    Me.linkReset.TabIndex = 34
    Me.linkReset.Text = "Reset..."
    '
    'btnSaveDefaults
    '
    Me.btnSaveDefaults.AutoSize = True
    Me.btnSaveDefaults.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.btnSaveDefaults.Location = New System.Drawing.Point(130, 511)
    Me.btnSaveDefaults.Name = "btnSaveDefaults"
    Me.btnSaveDefaults.Size = New System.Drawing.Size(142, 30)
    Me.btnSaveDefaults.TabIndex = 35
    Me.btnSaveDefaults.Text = "Save As Defaults"
    Me.btnSaveDefaults.UseVisualStyleBackColor = True
    '
    'btnLoadDefaults
    '
    Me.btnLoadDefaults.AutoSize = True
    Me.btnLoadDefaults.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.btnLoadDefaults.Location = New System.Drawing.Point(278, 511)
    Me.btnLoadDefaults.Name = "btnLoadDefaults"
    Me.btnLoadDefaults.Size = New System.Drawing.Size(119, 30)
    Me.btnLoadDefaults.TabIndex = 36
    Me.btnLoadDefaults.Text = "Load Defaults"
    Me.btnLoadDefaults.UseVisualStyleBackColor = True
    '
    'picRunner
    '
    Me.picRunner.Image = Global.SpeedCalculator.My.Resources.Resources.new_runner_trans
    Me.picRunner.Location = New System.Drawing.Point(235, 208)
    Me.picRunner.Name = "picRunner"
    Me.picRunner.Size = New System.Drawing.Size(162, 179)
    Me.picRunner.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
    Me.picRunner.TabIndex = 37
    Me.picRunner.TabStop = False
    '
    'cboUnit
    '
    Me.cboUnit.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
    Me.cboUnit.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.cboUnit.FormattingEnabled = True
    Me.cboUnit.Items.AddRange(New Object() {"Mi", "km"})
    Me.cboUnit.Location = New System.Drawing.Point(191, 65)
    Me.cboUnit.Name = "cboUnit"
    Me.cboUnit.Size = New System.Drawing.Size(82, 45)
    Me.cboUnit.TabIndex = 38
    '
    'radTime
    '
    Me.radTime.AutoSize = True
    Me.radTime.Checked = True
    Me.radTime.Location = New System.Drawing.Point(18, 36)
    Me.radTime.Name = "radTime"
    Me.radTime.Size = New System.Drawing.Size(14, 13)
    Me.radTime.TabIndex = 39
    Me.radTime.TabStop = True
    Me.radTime.UseVisualStyleBackColor = True
    '
    'radDistance
    '
    Me.radDistance.AutoSize = True
    Me.radDistance.Location = New System.Drawing.Point(18, 86)
    Me.radDistance.Name = "radDistance"
    Me.radDistance.Size = New System.Drawing.Size(14, 13)
    Me.radDistance.TabIndex = 40
    Me.radDistance.UseVisualStyleBackColor = True
    '
    'radSpeed
    '
    Me.radSpeed.AutoSize = True
    Me.radSpeed.Location = New System.Drawing.Point(18, 136)
    Me.radSpeed.Name = "radSpeed"
    Me.radSpeed.Size = New System.Drawing.Size(14, 13)
    Me.radSpeed.TabIndex = 41
    Me.radSpeed.UseVisualStyleBackColor = True
    '
    'numWeight
    '
    Me.numWeight.DecimalPlaces = 1
    Me.numWeight.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.numWeight.Location = New System.Drawing.Point(242, 393)
    Me.numWeight.Maximum = New Decimal(New Integer() {9999, 0, 0, 65536})
    Me.numWeight.Minimum = New Decimal(New Integer() {1, 0, 0, 65536})
    Me.numWeight.Name = "numWeight"
    Me.numWeight.Size = New System.Drawing.Size(155, 44)
    Me.numWeight.TabIndex = 42
    Me.numWeight.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
    Me.numWeight.Value = New Decimal(New Integer() {160, 0, 0, 0})
    '
    'txtCalories
    '
    Me.txtCalories.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.txtCalories.Location = New System.Drawing.Point(275, 443)
    Me.txtCalories.Name = "txtCalories"
    Me.txtCalories.ReadOnly = True
    Me.txtCalories.Size = New System.Drawing.Size(122, 44)
    Me.txtCalories.TabIndex = 43
    '
    'Label5
    '
    Me.Label5.AutoSize = True
    Me.Label5.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.Label5.Location = New System.Drawing.Point(38, 395)
    Me.Label5.Name = "Label5"
    Me.Label5.Size = New System.Drawing.Size(198, 37)
    Me.Label5.TabIndex = 44
    Me.Label5.Text = "Weight (lbs):"
    '
    'Label6
    '
    Me.Label6.AutoSize = True
    Me.Label6.Font = New System.Drawing.Font("Microsoft Sans Serif", 24.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
    Me.Label6.Location = New System.Drawing.Point(38, 446)
    Me.Label6.Name = "Label6"
    Me.Label6.Size = New System.Drawing.Size(231, 37)
    Me.Label6.TabIndex = 45
    Me.Label6.Text = "Calories (kcal):"
    '
    'SpeedCalc
    '
    Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
    Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
    Me.BackColor = System.Drawing.Color.PaleGoldenrod
    Me.ClientSize = New System.Drawing.Size(411, 553)
    Me.Controls.Add(Me.Label6)
    Me.Controls.Add(Me.Label5)
    Me.Controls.Add(Me.txtCalories)
    Me.Controls.Add(Me.numWeight)
    Me.Controls.Add(Me.radSpeed)
    Me.Controls.Add(Me.radDistance)
    Me.Controls.Add(Me.radTime)
    Me.Controls.Add(Me.cboUnit)
    Me.Controls.Add(Me.picRunner)
    Me.Controls.Add(Me.btnLoadDefaults)
    Me.Controls.Add(Me.btnSaveDefaults)
    Me.Controls.Add(Me.linkReset)
    Me.Controls.Add(Me.linkFullMarathon)
    Me.Controls.Add(Me.link10k)
    Me.Controls.Add(Me.linkHalfMarathon)
    Me.Controls.Add(Me.link5k)
    Me.Controls.Add(Me.Label4)
    Me.Controls.Add(Me.Label3)
    Me.Controls.Add(Me.Label2)
    Me.Controls.Add(Me.Label1)
    Me.Controls.Add(Me.numSpeed)
    Me.Controls.Add(Me.numDistance)
    Me.Controls.Add(Me.numHours)
    Me.Controls.Add(Me.numMins)
    Me.Controls.Add(Me.numSecs)
    Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
    Me.MaximizeBox = False
    Me.MinimizeBox = False
    Me.MinimumSize = New System.Drawing.Size(427, 591)
    Me.Name = "SpeedCalc"
    Me.Text = "Speed Calculator"
    CType(Me.numSecs, System.ComponentModel.ISupportInitialize).EndInit()
    CType(Me.numMins, System.ComponentModel.ISupportInitialize).EndInit()
    CType(Me.numHours, System.ComponentModel.ISupportInitialize).EndInit()
    CType(Me.numDistance, System.ComponentModel.ISupportInitialize).EndInit()
    CType(Me.numSpeed, System.ComponentModel.ISupportInitialize).EndInit()
    CType(Me.picRunner, System.ComponentModel.ISupportInitialize).EndInit()
    CType(Me.numWeight, System.ComponentModel.ISupportInitialize).EndInit()
    Me.ResumeLayout(False)
    Me.PerformLayout()

  End Sub
  Friend WithEvents numSecs As System.Windows.Forms.NumericUpDown
  Friend WithEvents numMins As System.Windows.Forms.NumericUpDown
  Friend WithEvents numHours As System.Windows.Forms.NumericUpDown
  Friend WithEvents numDistance As System.Windows.Forms.NumericUpDown
  Friend WithEvents numSpeed As System.Windows.Forms.NumericUpDown
  Friend WithEvents Label1 As System.Windows.Forms.Label
  Friend WithEvents Label2 As System.Windows.Forms.Label
  Friend WithEvents Label3 As System.Windows.Forms.Label
  Friend WithEvents Label4 As System.Windows.Forms.Label
  Friend WithEvents link5k As System.Windows.Forms.Label
  Friend WithEvents linkHalfMarathon As System.Windows.Forms.Label
  Friend WithEvents link10k As System.Windows.Forms.Label
  Friend WithEvents linkFullMarathon As System.Windows.Forms.Label
  Friend WithEvents linkReset As System.Windows.Forms.Label
  Friend WithEvents btnSaveDefaults As System.Windows.Forms.Button
  Friend WithEvents btnLoadDefaults As System.Windows.Forms.Button
  Friend WithEvents picRunner As System.Windows.Forms.PictureBox
  Friend WithEvents cboUnit As System.Windows.Forms.ComboBox
  Friend WithEvents radTime As System.Windows.Forms.RadioButton
  Friend WithEvents radDistance As System.Windows.Forms.RadioButton
  Friend WithEvents radSpeed As System.Windows.Forms.RadioButton
  Friend WithEvents numWeight As System.Windows.Forms.NumericUpDown
  Friend WithEvents txtCalories As System.Windows.Forms.TextBox
  Friend WithEvents Label5 As System.Windows.Forms.Label
  Friend WithEvents Label6 As System.Windows.Forms.Label

End Class
