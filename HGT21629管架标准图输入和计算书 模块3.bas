Attribute VB_Name = "模块3"
Sub CreateToolBar()
    Dim newToolBars As CommandBar
    Dim button As CommandBarButton
    
    Dim buttonNames As Variant
    Dim buttonActions As Variant
    
    
    buttonNames = Array("指派管架编号和数量至分表")
    buttonActions = Array("button1")

    On Error Resume Next
    CommandBars("工 具").Delete
    
    Set newToolBars = CommandBars.Add(Name:="工 具", Temporary:=True)
    With newToolBars
        .Visible = True
        .Position = msoBarTop
        
        For i = 0 To UBound(buttonNames)
            Set button = .Controls.Add
            With button
                .Caption = buttonNames(i)
                .Style = msoButtonCaption
                .OnAction = buttonActions(i)
                
                .BeginGroup = (i > 0)
            End With
        Next
    End With
    
End Sub

