Attribute VB_Name = "模块3"
Sub createtoolbar()
    Dim newToolBars As CommandBar
    Dim button As CommandBarButton
    Dim buttonNames As Variant
    Dim buttonActions As Variant
    buttonNames = Array("1、添加数据源", "2、更新后台查询", "3、汇总材料")
    buttonActions = Array("data", "refresh", "mto")
    On Error Resume Next
    CommandBars("支架材料工具").delete
    Set newToolBars = CommandBars.Add(Name:="支架材料工具", Temporary:=True)
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

