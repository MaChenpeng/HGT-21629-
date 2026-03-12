Attribute VB_Name = "模块2"

Sub ml()

    Dim wsht As Worksheet, k%, wshtname$

    Columns(1).ClearContents

    Range("a1") = "HG/T21629管架标准图目录和索引"
    k = 1

    For Each wsht In Worksheets

        wshtname = wsht.Name

        If wshtname <> ActiveSheet.Name Then

          k = k + 1

          ActiveSheet.Hyperlinks.Add anchor:=Cells(k, 1), Address:="", SubAddress:="'" & wshtname & "'!a1", TextToDisplay:=wshtname

        End If

    Next

End Sub
