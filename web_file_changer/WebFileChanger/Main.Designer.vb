<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Main
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
    Me.btnGo = New System.Windows.Forms.Button
    Me.txtAddAfter = New System.Windows.Forms.TextBox
    Me.ofdDirectory = New System.Windows.Forms.OpenFileDialog
    Me.btnDir = New System.Windows.Forms.Button
    Me.txtDir = New System.Windows.Forms.TextBox
    Me.txtSearchLineAfter = New System.Windows.Forms.TextBox
    Me.Label1 = New System.Windows.Forms.Label
    Me.txtFilenames = New System.Windows.Forms.TextBox
    Me.Label2 = New System.Windows.Forms.Label
    Me.Label4 = New System.Windows.Forms.Label
    Me.Label5 = New System.Windows.Forms.Label
    Me.txtSearchLineBefore = New System.Windows.Forms.TextBox
    Me.txtAddBefore = New System.Windows.Forms.TextBox
    Me.SuspendLayout()
    '
    'btnGo
    '
    Me.btnGo.Location = New System.Drawing.Point(288, 437)
    Me.btnGo.Name = "btnGo"
    Me.btnGo.Size = New System.Drawing.Size(177, 60)
    Me.btnGo.TabIndex = 0
    Me.btnGo.Text = "Change Files"
    Me.btnGo.UseVisualStyleBackColor = True
    '
    'txtAddAfter
    '
    Me.txtAddAfter.Location = New System.Drawing.Point(12, 291)
    Me.txtAddAfter.Name = "txtAddAfter"
    Me.txtAddAfter.Size = New System.Drawing.Size(748, 20)
    Me.txtAddAfter.TabIndex = 3
    '
    'ofdDirectory
    '
    Me.ofdDirectory.Multiselect = True
    '
    'btnDir
    '
    Me.btnDir.Location = New System.Drawing.Point(12, 12)
    Me.btnDir.Name = "btnDir"
    Me.btnDir.Size = New System.Drawing.Size(128, 23)
    Me.btnDir.TabIndex = 4
    Me.btnDir.Text = "Select Files  -->"
    Me.btnDir.UseVisualStyleBackColor = True
    '
    'txtDir
    '
    Me.txtDir.Location = New System.Drawing.Point(146, 15)
    Me.txtDir.Name = "txtDir"
    Me.txtDir.Size = New System.Drawing.Size(614, 20)
    Me.txtDir.TabIndex = 5
    '
    'txtSearchLineAfter
    '
    Me.txtSearchLineAfter.Location = New System.Drawing.Point(12, 252)
    Me.txtSearchLineAfter.Name = "txtSearchLineAfter"
    Me.txtSearchLineAfter.Size = New System.Drawing.Size(748, 20)
    Me.txtSearchLineAfter.TabIndex = 6
    '
    'Label1
    '
    Me.Label1.AutoSize = True
    Me.Label1.Location = New System.Drawing.Point(12, 275)
    Me.Label1.Name = "Label1"
    Me.Label1.Size = New System.Drawing.Size(75, 13)
    Me.Label1.TabIndex = 7
    Me.Label1.Text = "Add This Line:"
    '
    'txtFilenames
    '
    Me.txtFilenames.Location = New System.Drawing.Point(12, 41)
    Me.txtFilenames.Multiline = True
    Me.txtFilenames.Name = "txtFilenames"
    Me.txtFilenames.Size = New System.Drawing.Size(748, 180)
    Me.txtFilenames.TabIndex = 8
    '
    'Label2
    '
    Me.Label2.AutoSize = True
    Me.Label2.Location = New System.Drawing.Point(12, 236)
    Me.Label2.Name = "Label2"
    Me.Label2.Size = New System.Drawing.Size(76, 13)
    Me.Label2.TabIndex = 9
    Me.Label2.Text = "Add Line after:"
    '
    'Label4
    '
    Me.Label4.AutoSize = True
    Me.Label4.Location = New System.Drawing.Point(12, 327)
    Me.Label4.Name = "Label4"
    Me.Label4.Size = New System.Drawing.Size(85, 13)
    Me.Label4.TabIndex = 14
    Me.Label4.Text = "Add Line before:"
    '
    'Label5
    '
    Me.Label5.AutoSize = True
    Me.Label5.Location = New System.Drawing.Point(12, 366)
    Me.Label5.Name = "Label5"
    Me.Label5.Size = New System.Drawing.Size(75, 13)
    Me.Label5.TabIndex = 13
    Me.Label5.Text = "Add This Line:"
    '
    'txtSearchLineBefore
    '
    Me.txtSearchLineBefore.Location = New System.Drawing.Point(12, 343)
    Me.txtSearchLineBefore.Name = "txtSearchLineBefore"
    Me.txtSearchLineBefore.Size = New System.Drawing.Size(748, 20)
    Me.txtSearchLineBefore.TabIndex = 12
    '
    'txtAddBefore
    '
    Me.txtAddBefore.Location = New System.Drawing.Point(12, 382)
    Me.txtAddBefore.Name = "txtAddBefore"
    Me.txtAddBefore.Size = New System.Drawing.Size(748, 20)
    Me.txtAddBefore.TabIndex = 11
    '
    'Main
    '
    Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
    Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
    Me.ClientSize = New System.Drawing.Size(772, 509)
    Me.Controls.Add(Me.Label4)
    Me.Controls.Add(Me.Label5)
    Me.Controls.Add(Me.txtSearchLineBefore)
    Me.Controls.Add(Me.txtAddBefore)
    Me.Controls.Add(Me.Label2)
    Me.Controls.Add(Me.txtFilenames)
    Me.Controls.Add(Me.Label1)
    Me.Controls.Add(Me.txtSearchLineAfter)
    Me.Controls.Add(Me.txtDir)
    Me.Controls.Add(Me.btnDir)
    Me.Controls.Add(Me.txtAddAfter)
    Me.Controls.Add(Me.btnGo)
    Me.Name = "Main"
    Me.Text = "Web File Changer"
    Me.ResumeLayout(False)
    Me.PerformLayout()

  End Sub
  Friend WithEvents btnGo As System.Windows.Forms.Button
  Friend WithEvents txtAddAfter As System.Windows.Forms.TextBox
  Friend WithEvents ofdDirectory As System.Windows.Forms.OpenFileDialog
  Friend WithEvents btnDir As System.Windows.Forms.Button
  Friend WithEvents txtDir As System.Windows.Forms.TextBox
  Friend WithEvents txtSearchLineAfter As System.Windows.Forms.TextBox
  Friend WithEvents Label1 As System.Windows.Forms.Label
  Friend WithEvents txtFilenames As System.Windows.Forms.TextBox
  Friend WithEvents Label2 As System.Windows.Forms.Label
  Friend WithEvents Label4 As System.Windows.Forms.Label
  Friend WithEvents Label5 As System.Windows.Forms.Label
  Friend WithEvents txtSearchLineBefore As System.Windows.Forms.TextBox
  Friend WithEvents txtAddBefore As System.Windows.Forms.TextBox

End Class
