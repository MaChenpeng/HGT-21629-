Attribute VB_Name = "模块1"
Sub CopyDataA1()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngA1 As Range
    Dim rngA1Z As Range
    Dim wsSS As Worksheet
    Dim wsA1 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsA1 = ThisWorkbook.Sheets("A1")
    Set rngA1Z = wsA1.Range("A2:D100")
    rngA1Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "A1" Then
    For j = 1 To 4
    wsA1.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataA2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngA2 As Range
    Dim rngA2Z As Range
    Dim wsSS As Worksheet
    Dim wsA2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsA2 = ThisWorkbook.Sheets("A2")
    Set rngA2Z = wsA2.Range("A2:D100")
    rngA2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "A2" Then
    For j = 1 To 4
    wsA2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataA3()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngA3 As Range
    Dim rngA3Z As Range
    Dim wsSS As Worksheet
    Dim wsA3 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsA3 = ThisWorkbook.Sheets("A3")
    Set rngA3Z = wsA3.Range("A2:D100")
    rngA3Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "A3" Then
    For j = 1 To 4
    wsA3.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataA4()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngA4 As Range
    Dim rngA4Z As Range
    Dim wsSS As Worksheet
    Dim wsA4 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsA4 = ThisWorkbook.Sheets("A4")
    Set rngA4Z = wsA4.Range("A2:D100")
    rngA4Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "A4" Then
    For j = 1 To 4
    wsA4.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataA5()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngA5 As Range
    Dim rngA5Z As Range
    Dim wsSS As Worksheet
    Dim wsA5 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsA5 = ThisWorkbook.Sheets("A5")
    Set rngA5Z = wsA5.Range("A2:D100")
    rngA5Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "A5" Then
    For j = 1 To 4
    wsA5.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD2 As Range
    Dim rngD2Z As Range
    Dim wsSS As Worksheet
    Dim wsD2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD2 = ThisWorkbook.Sheets("D2")
    Set rngD2Z = wsD2.Range("A2:D100")
    rngD2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D2" Then
    For j = 1 To 4
    wsD2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD3()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD3 As Range
    Dim rngD3Z As Range
    Dim wsSS As Worksheet
    Dim wsD3 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD3 = ThisWorkbook.Sheets("D3")
    Set rngD3Z = wsD3.Range("A2:D100")
    rngD3Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D3" Then
    For j = 1 To 4
    wsD3.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD4()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD4 As Range
    Dim rngD4Z As Range
    Dim wsSS As Worksheet
    Dim wsD4 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD4 = ThisWorkbook.Sheets("D4")
    Set rngD4Z = wsD4.Range("A2:D100")
    rngD4Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D4" Then
    For j = 1 To 4
    wsD4.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD5()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD5 As Range
    Dim rngD5Z As Range
    Dim wsSS As Worksheet
    Dim wsD5 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD5 = ThisWorkbook.Sheets("D5")
    Set rngD5Z = wsD5.Range("A2:D100")
    rngD5Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D5" Then
    For j = 1 To 4
    wsD5.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD6()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD6 As Range
    Dim rngD6Z As Range
    Dim wsSS As Worksheet
    Dim wsD6 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD6 = ThisWorkbook.Sheets("D6")
    Set rngD6Z = wsD6.Range("A2:D100")
    rngD6Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D6" Then
    For j = 1 To 4
    wsD6.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD7()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD7 As Range
    Dim rngD7Z As Range
    Dim wsSS As Worksheet
    Dim wsD7 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD7 = ThisWorkbook.Sheets("D7")
    Set rngD7Z = wsD7.Range("A2:D100")
    rngD7Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D7" Then
    For j = 1 To 4
    wsD7.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD8()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD8 As Range
    Dim rngD8Z As Range
    Dim wsSS As Worksheet
    Dim wsD8 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD8 = ThisWorkbook.Sheets("D8")
    Set rngD8Z = wsD8.Range("A2:D100")
    rngD8Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D8" Then
    For j = 1 To 4
    wsD8.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD9()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD9 As Range
    Dim rngD9Z As Range
    Dim wsSS As Worksheet
    Dim wsD9 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD9 = ThisWorkbook.Sheets("D9")
    Set rngD9Z = wsD9.Range("A2:D100")
    rngD9Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D9" Then
    For j = 1 To 4
    wsD9.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD10()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD10 As Range
    Dim rngD10Z As Range
    Dim wsSS As Worksheet
    Dim wsD10 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD10 = ThisWorkbook.Sheets("D10")
    Set rngD10Z = wsD10.Range("A2:D100")
    rngD10Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D10" Then
    For j = 1 To 4
    wsD10.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD11()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD11 As Range
    Dim rngD11Z As Range
    Dim wsSS As Worksheet
    Dim wsD11 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD11 = ThisWorkbook.Sheets("D11")
    Set rngD11Z = wsD11.Range("A2:D100")
    rngD11Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D11" Then
    For j = 1 To 4
    wsD11.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD12()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD12 As Range
    Dim rngD12Z As Range
    Dim wsSS As Worksheet
    Dim wsD12 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD12 = ThisWorkbook.Sheets("D12")
    Set rngD12Z = wsD12.Range("A2:D100")
    rngD12Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D12" Then
    For j = 1 To 4
    wsD12.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD13()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD13 As Range
    Dim rngD13Z As Range
    Dim wsSS As Worksheet
    Dim wsD13 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD13 = ThisWorkbook.Sheets("D13")
    Set rngD13Z = wsD13.Range("A2:D100")
    rngD13Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D13" Then
    For j = 1 To 4
    wsD13.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD14()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD14 As Range
    Dim rngD14Z As Range
    Dim wsSS As Worksheet
    Dim wsD14 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD14 = ThisWorkbook.Sheets("D14")
    Set rngD14Z = wsD14.Range("A2:D100")
    rngD14Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D14" Then
    For j = 1 To 4
    wsD14.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD15()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD15 As Range
    Dim rngD15Z As Range
    Dim wsSS As Worksheet
    Dim wsD15 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD15 = ThisWorkbook.Sheets("D15")
    Set rngD15Z = wsD15.Range("A2:D100")
    rngD15Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D15" Then
    For j = 1 To 4
    wsD15.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD16()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD16 As Range
    Dim rngD16Z As Range
    Dim wsSS As Worksheet
    Dim wsD16 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD16 = ThisWorkbook.Sheets("D16")
    Set rngD16Z = wsD16.Range("A2:D100")
    rngD16Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D16" Then
    For j = 1 To 4
    wsD16.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD17()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD17 As Range
    Dim rngD17Z As Range
    Dim wsSS As Worksheet
    Dim wsD17 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD17 = ThisWorkbook.Sheets("D17")
    Set rngD17Z = wsD17.Range("A2:D100")
    rngD17Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D17" Then
    For j = 1 To 4
    wsD17.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD18()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD18 As Range
    Dim rngD18Z As Range
    Dim wsSS As Worksheet
    Dim wsD18 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD18 = ThisWorkbook.Sheets("D18")
    Set rngD18Z = wsD18.Range("A2:D100")
    rngD18Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D18" Then
    For j = 1 To 4
    wsD18.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD19()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD19 As Range
    Dim rngD19Z As Range
    Dim wsSS As Worksheet
    Dim wsD19 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD19 = ThisWorkbook.Sheets("D19")
    Set rngD19Z = wsD19.Range("A2:D100")
    rngD19Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D19" Then
    For j = 1 To 4
    wsD19.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataD20()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngD20 As Range
    Dim rngD20Z As Range
    Dim wsSS As Worksheet
    Dim wsD20 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsD20 = ThisWorkbook.Sheets("D20")
    Set rngD20Z = wsD20.Range("A2:D100")
    rngD20Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "D20" Then
    For j = 1 To 4
    wsD20.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE1()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE1 As Range
    Dim rngE1Z As Range
    Dim wsSS As Worksheet
    Dim wsE1 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE1 = ThisWorkbook.Sheets("E1")
    Set rngE1Z = wsE1.Range("A2:D100")
    rngE1Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E1" Then
    For j = 1 To 4
    wsE1.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE2 As Range
    Dim rngE2Z As Range
    Dim wsSS As Worksheet
    Dim wsE2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE2 = ThisWorkbook.Sheets("E2")
    Set rngE2Z = wsE2.Range("A2:D100")
    rngE2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E2" Then
    For j = 1 To 4
    wsE2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE3()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE3 As Range
    Dim rngE3Z As Range
    Dim wsSS As Worksheet
    Dim wsE3 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE3 = ThisWorkbook.Sheets("E3")
    Set rngE3Z = wsE3.Range("A2:D100")
    rngE3Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E3" Then
    For j = 1 To 4
    wsE3.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE4()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE4 As Range
    Dim rngE4Z As Range
    Dim wsSS As Worksheet
    Dim wsE4 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE4 = ThisWorkbook.Sheets("E4")
    Set rngE4Z = wsE4.Range("A2:D100")
    rngE4Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E4" Then
    For j = 1 To 4
    wsE4.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE5()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE5 As Range
    Dim rngE5Z As Range
    Dim wsSS As Worksheet
    Dim wsE5 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE5 = ThisWorkbook.Sheets("E5")
    Set rngE5Z = wsE5.Range("A2:D100")
    rngE5Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E5" Then
    For j = 1 To 4
    wsE5.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE6()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE6 As Range
    Dim rngE6Z As Range
    Dim wsSS As Worksheet
    Dim wsE6 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE6 = ThisWorkbook.Sheets("E6")
    Set rngE6Z = wsE6.Range("A2:D100")
    rngE6Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E6" Then
    For j = 1 To 4
    wsE6.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE7()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE7 As Range
    Dim rngE7Z As Range
    Dim wsSS As Worksheet
    Dim wsE7 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE7 = ThisWorkbook.Sheets("E7")
    Set rngE7Z = wsE7.Range("A2:D100")
    rngE7Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E7" Then
    For j = 1 To 4
    wsE7.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE8()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE8 As Range
    Dim rngE8Z As Range
    Dim wsSS As Worksheet
    Dim wsE8 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE8 = ThisWorkbook.Sheets("E8")
    Set rngE8Z = wsE8.Range("A2:D100")
    rngE8Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E8" Then
    For j = 1 To 4
    wsE8.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE9()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE9 As Range
    Dim rngE9Z As Range
    Dim wsSS As Worksheet
    Dim wsE9 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE9 = ThisWorkbook.Sheets("E9")
    Set rngE9Z = wsE9.Range("A2:D100")
    rngE9Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E9" Then
    For j = 1 To 4
    wsE9.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataE10()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngE10 As Range
    Dim rngE10Z As Range
    Dim wsSS As Worksheet
    Dim wsE10 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsE10 = ThisWorkbook.Sheets("E10")
    Set rngE10Z = wsE10.Range("A2:D100")
    rngE10Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "E10" Then
    For j = 1 To 4
    wsE10.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF2 As Range
    Dim rngF2Z As Range
    Dim wsSS As Worksheet
    Dim wsF2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF2 = ThisWorkbook.Sheets("F2")
    Set rngF2Z = wsF2.Range("A2:D100")
    rngF2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F2" Then
    For j = 1 To 4
    wsF2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF3()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF3 As Range
    Dim rngF3Z As Range
    Dim wsSS As Worksheet
    Dim wsF3 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF3 = ThisWorkbook.Sheets("F3")
    Set rngF3Z = wsF3.Range("A2:D100")
    rngF3Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F3" Then
    For j = 1 To 4
    wsF3.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF4()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF4 As Range
    Dim rngF4Z As Range
    Dim wsSS As Worksheet
    Dim wsF4 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF4 = ThisWorkbook.Sheets("F4")
    Set rngF4Z = wsF4.Range("A2:D100")
    rngF4Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F4" Then
    For j = 1 To 4
    wsF4.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF5()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF5 As Range
    Dim rngF5Z As Range
    Dim wsSS As Worksheet
    Dim wsF5 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF5 = ThisWorkbook.Sheets("F5")
    Set rngF5Z = wsF5.Range("A2:D100")
    rngF5Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F5" Then
    For j = 1 To 4
    wsF5.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF6()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF6 As Range
    Dim rngF6Z As Range
    Dim wsSS As Worksheet
    Dim wsF6 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF6 = ThisWorkbook.Sheets("F6")
    Set rngF6Z = wsF6.Range("A2:D100")
    rngF6Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F6" Then
    For j = 1 To 4
    wsF6.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF7()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF7 As Range
    Dim rngF7Z As Range
    Dim wsSS As Worksheet
    Dim wsF7 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF7 = ThisWorkbook.Sheets("F7")
    Set rngF7Z = wsF7.Range("A2:D100")
    rngF7Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F7" Then
    For j = 1 To 4
    wsF7.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF8()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF8 As Range
    Dim rngF8Z As Range
    Dim wsSS As Worksheet
    Dim wsF8 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF8 = ThisWorkbook.Sheets("F8")
    Set rngF8Z = wsF8.Range("A2:D100")
    rngF8Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F8" Then
    For j = 1 To 4
    wsF8.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF9()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF9 As Range
    Dim rngF9Z As Range
    Dim wsSS As Worksheet
    Dim wsF9 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF9 = ThisWorkbook.Sheets("F9")
    Set rngF9Z = wsF9.Range("A2:D100")
    rngF9Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F9" Then
    For j = 1 To 4
    wsF9.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF10()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF10 As Range
    Dim rngF10Z As Range
    Dim wsSS As Worksheet
    Dim wsF10 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF10 = ThisWorkbook.Sheets("F10")
    Set rngF10Z = wsF10.Range("A2:D100")
    rngF10Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F10" Then
    For j = 1 To 4
    wsF10.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF11()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF11 As Range
    Dim rngF11Z As Range
    Dim wsSS As Worksheet
    Dim wsF11 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF11 = ThisWorkbook.Sheets("F11")
    Set rngF11Z = wsF11.Range("A2:D100")
    rngF11Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F11" Then
    For j = 1 To 4
    wsF11.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF12()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF12 As Range
    Dim rngF12Z As Range
    Dim wsSS As Worksheet
    Dim wsF12 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF12 = ThisWorkbook.Sheets("F12")
    Set rngF12Z = wsF12.Range("A2:D100")
    rngF12Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F12" Then
    For j = 1 To 4
    wsF12.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF13()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF13 As Range
    Dim rngF13Z As Range
    Dim wsSS As Worksheet
    Dim wsF13 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF13 = ThisWorkbook.Sheets("F13")
    Set rngF13Z = wsF13.Range("A2:D100")
    rngF13Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F13" Then
    For j = 1 To 4
    wsF13.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataF14()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngF14 As Range
    Dim rngF14Z As Range
    Dim wsSS As Worksheet
    Dim wsF14 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsF14 = ThisWorkbook.Sheets("F14")
    Set rngF14Z = wsF14.Range("A2:D100")
    rngF14Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "F14" Then
    For j = 1 To 4
    wsF14.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG1()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG1 As Range
    Dim rngG1Z As Range
    Dim wsSS As Worksheet
    Dim wsG1 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG1 = ThisWorkbook.Sheets("G1")
    Set rngG1Z = wsG1.Range("A2:D100")
    rngG1Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G1" Then
    For j = 1 To 4
    wsG1.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG2 As Range
    Dim rngG2Z As Range
    Dim wsSS As Worksheet
    Dim wsG2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG2 = ThisWorkbook.Sheets("G2")
    Set rngG2Z = wsG2.Range("A2:D100")
    rngG2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G2" Then
    For j = 1 To 4
    wsG2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG3()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG3 As Range
    Dim rngG3Z As Range
    Dim wsSS As Worksheet
    Dim wsG3 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG3 = ThisWorkbook.Sheets("G3")
    Set rngG3Z = wsG3.Range("A2:D100")
    rngG3Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G3" Then
    For j = 1 To 4
    wsG3.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG4()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG4 As Range
    Dim rngG4Z As Range
    Dim wsSS As Worksheet
    Dim wsG4 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG4 = ThisWorkbook.Sheets("G4")
    Set rngG4Z = wsG4.Range("A2:D100")
    rngG4Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G4" Then
    For j = 1 To 4
    wsG4.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG5()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG5 As Range
    Dim rngG5Z As Range
    Dim wsSS As Worksheet
    Dim wsG5 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG5 = ThisWorkbook.Sheets("G5")
    Set rngG5Z = wsG5.Range("A2:D100")
    rngG5Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G5" Then
    For j = 1 To 4
    wsG5.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG6()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG6 As Range
    Dim rngG6Z As Range
    Dim wsSS As Worksheet
    Dim wsG6 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG6 = ThisWorkbook.Sheets("G6")
    Set rngG6Z = wsG6.Range("A2:D100")
    rngG6Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G6" Then
    For j = 1 To 4
    wsG6.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG11()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG11 As Range
    Dim rngG11Z As Range
    Dim wsSS As Worksheet
    Dim wsG11 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG11 = ThisWorkbook.Sheets("G11")
    Set rngG11Z = wsG11.Range("A2:D100")
    rngG11Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G11" Then
    For j = 1 To 4
    wsG11.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG12()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG12 As Range
    Dim rngG12Z As Range
    Dim wsSS As Worksheet
    Dim wsG12 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG12 = ThisWorkbook.Sheets("G12")
    Set rngG12Z = wsG12.Range("A2:D100")
    rngG12Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G12" Then
    For j = 1 To 4
    wsG12.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG13()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG13 As Range
    Dim rngG13Z As Range
    Dim wsSS As Worksheet
    Dim wsG13 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG13 = ThisWorkbook.Sheets("G13")
    Set rngG13Z = wsG13.Range("A2:D100")
    rngG13Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G13" Then
    For j = 1 To 4
    wsG13.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG14()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG14 As Range
    Dim rngG14Z As Range
    Dim wsSS As Worksheet
    Dim wsG14 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG14 = ThisWorkbook.Sheets("G14")
    Set rngG14Z = wsG14.Range("A2:D100")
    rngG14Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G14" Then
    For j = 1 To 4
    wsG14.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG15()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG15 As Range
    Dim rngG15Z As Range
    Dim wsSS As Worksheet
    Dim wsG15 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG15 = ThisWorkbook.Sheets("G15")
    Set rngG15Z = wsG15.Range("A2:D100")
    rngG15Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G15" Then
    For j = 1 To 4
    wsG15.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG16()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG16 As Range
    Dim rngG16Z As Range
    Dim wsSS As Worksheet
    Dim wsG16 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG16 = ThisWorkbook.Sheets("G16")
    Set rngG16Z = wsG16.Range("A2:D100")
    rngG16Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G16" Then
    For j = 1 To 4
    wsG16.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataG17()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngG17 As Range
    Dim rngG17Z As Range
    Dim wsSS As Worksheet
    Dim wsG17 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsG17 = ThisWorkbook.Sheets("G17")
    Set rngG17Z = wsG17.Range("A2:D100")
    rngG17Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "G17" Then
    For j = 1 To 4
    wsG17.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataH1()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngH1 As Range
    Dim rngH1Z As Range
    Dim wsSS As Worksheet
    Dim wsH1 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsH1 = ThisWorkbook.Sheets("H1")
    Set rngH1Z = wsH1.Range("A2:D100")
    rngH1Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "H1" Then
    For j = 1 To 4
    wsH1.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataH2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngH2 As Range
    Dim rngH2Z As Range
    Dim wsSS As Worksheet
    Dim wsH2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsH2 = ThisWorkbook.Sheets("H2")
    Set rngH2Z = wsH2.Range("A2:D100")
    rngH2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "H2" Then
    For j = 1 To 4
    wsH2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataJ1()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngJ1 As Range
    Dim rngJ1Z As Range
    Dim wsSS As Worksheet
    Dim wsJ1 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsJ1 = ThisWorkbook.Sheets("J1")
    Set rngJ1Z = wsJ1.Range("A2:D100")
    rngJ1Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "J1" Then
    For j = 1 To 4
    wsJ1.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataJ2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngJ2 As Range
    Dim rngJ2Z As Range
    Dim wsSS As Worksheet
    Dim wsJ2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsJ2 = ThisWorkbook.Sheets("J2")
    Set rngJ2Z = wsJ2.Range("A2:D100")
    rngJ2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "J2" Then
    For j = 1 To 4
    wsJ2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataJ13()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngJ13 As Range
    Dim rngJ13Z As Range
    Dim wsSS As Worksheet
    Dim wsJ13 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsJ13 = ThisWorkbook.Sheets("J13")
    Set rngJ13Z = wsJ13.Range("A2:D100")
    rngJ13Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "J13" Then
    For j = 1 To 4
    wsJ13.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataK1()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngK1 As Range
    Dim rngK1Z As Range
    Dim wsSS As Worksheet
    Dim wsK1 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsK1 = ThisWorkbook.Sheets("K1")
    Set rngK1Z = wsK1.Range("A2:D100")
    rngK1Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "K1" Then
    For j = 1 To 4
    wsK1.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataK2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngK2 As Range
    Dim rngK2Z As Range
    Dim wsSS As Worksheet
    Dim wsK2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsK2 = ThisWorkbook.Sheets("K2")
    Set rngK2Z = wsK2.Range("A2:D100")
    rngK2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "K2" Then
    For j = 1 To 4
    wsK2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataQ1()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngQ1 As Range
    Dim rngQ1Z As Range
    Dim wsSS As Worksheet
    Dim wsQ1 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsQ1 = ThisWorkbook.Sheets("Q1")
    Set rngQ1Z = wsQ1.Range("A2:D100")
    rngQ1Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Q1" Then
    For j = 1 To 4
    wsQ1.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataQ2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngQ2 As Range
    Dim rngQ2Z As Range
    Dim wsSS As Worksheet
    Dim wsQ2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsQ2 = ThisWorkbook.Sheets("Q2")
    Set rngQ2Z = wsQ2.Range("A2:D100")
    rngQ2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Q2" Then
    For j = 1 To 4
    wsQ2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataQ3()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngQ3 As Range
    Dim rngQ3Z As Range
    Dim wsSS As Worksheet
    Dim wsQ3 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsQ3 = ThisWorkbook.Sheets("Q3")
    Set rngQ3Z = wsQ3.Range("A2:D100")
    rngQ3Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Q3" Then
    For j = 1 To 4
    wsQ3.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataQ4()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngQ4 As Range
    Dim rngQ4Z As Range
    Dim wsSS As Worksheet
    Dim wsQ4 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsQ4 = ThisWorkbook.Sheets("Q4")
    Set rngQ4Z = wsQ4.Range("A2:D100")
    rngQ4Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Q4" Then
    For j = 1 To 4
    wsQ4.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataQ5()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngQ5 As Range
    Dim rngQ5Z As Range
    Dim wsSS As Worksheet
    Dim wsQ5 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsQ5 = ThisWorkbook.Sheets("Q5")
    Set rngQ5Z = wsQ5.Range("A2:D100")
    rngQ5Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Q5" Then
    For j = 1 To 4
    wsQ5.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataQ6()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngQ6 As Range
    Dim rngQ6Z As Range
    Dim wsSS As Worksheet
    Dim wsQ6 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsQ6 = ThisWorkbook.Sheets("Q6")
    Set rngQ6Z = wsQ6.Range("A2:D100")
    rngQ6Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Q6" Then
    For j = 1 To 4
    wsQ6.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataQ7()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngQ7 As Range
    Dim rngQ7Z As Range
    Dim wsSS As Worksheet
    Dim wsQ7 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsQ7 = ThisWorkbook.Sheets("Q7")
    Set rngQ7Z = wsQ7.Range("A2:D100")
    rngQ7Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Q7" Then
    For j = 1 To 4
    wsQ7.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataU1()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngU1 As Range
    Dim rngU1Z As Range
    Dim wsSS As Worksheet
    Dim wsU1 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsU1 = ThisWorkbook.Sheets("U1")
    Set rngU1Z = wsU1.Range("A2:D100")
    rngU1Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "U1" Then
    For j = 1 To 4
    wsU1.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataU2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngU2 As Range
    Dim rngU2Z As Range
    Dim wsSS As Worksheet
    Dim wsU2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsU2 = ThisWorkbook.Sheets("U2")
    Set rngU2Z = wsU2.Range("A2:D100")
    rngU2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "U2" Then
    For j = 1 To 4
    wsU2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataU3()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngU3 As Range
    Dim rngU3Z As Range
    Dim wsSS As Worksheet
    Dim wsU3 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsU3 = ThisWorkbook.Sheets("U3")
    Set rngU3Z = wsU3.Range("A2:D100")
    rngU3Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "U3" Then
    For j = 1 To 4
    wsU3.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataU4()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngU4 As Range
    Dim rngU4Z As Range
    Dim wsSS As Worksheet
    Dim wsU4 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsU4 = ThisWorkbook.Sheets("U4")
    Set rngU4Z = wsU4.Range("A2:D100")
    rngU4Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "U4" Then
    For j = 1 To 4
    wsU4.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataU5()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngU5 As Range
    Dim rngU5Z As Range
    Dim wsSS As Worksheet
    Dim wsU5 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsU5 = ThisWorkbook.Sheets("U5")
    Set rngU5Z = wsU5.Range("A2:D100")
    rngU5Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "U5" Then
    For j = 1 To 4
    wsU5.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataU6()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngU6 As Range
    Dim rngU6Z As Range
    Dim wsSS As Worksheet
    Dim wsU6 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsU6 = ThisWorkbook.Sheets("U6")
    Set rngU6Z = wsU6.Range("A2:D100")
    rngU6Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "U6" Then
    For j = 1 To 4
    wsU6.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataY1()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngY1 As Range
    Dim rngY1Z As Range
    Dim wsSS As Worksheet
    Dim wsY1 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsY1 = ThisWorkbook.Sheets("Y1")
    Set rngY1Z = wsY1.Range("A2:D100")
    rngY1Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Y1" Then
    For j = 1 To 4
    wsY1.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataY2()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngY2 As Range
    Dim rngY2Z As Range
    Dim wsSS As Worksheet
    Dim wsY2 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsY2 = ThisWorkbook.Sheets("Y2")
    Set rngY2Z = wsY2.Range("A2:D100")
    rngY2Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Y2" Then
    For j = 1 To 4
    wsY2.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub
Sub CopyDataY4()
    Dim arr As Variant
    Dim i As Long
    Dim j As Long
    Dim rngSS As Range
    Dim rngY4 As Range
    Dim rngY4Z As Range
    Dim wsSS As Worksheet
    Dim wsY4 As Worksheet
    Dim row As Long
    row = 2
    Set wsSS = ThisWorkbook.Sheets("管架编号及数量输入")
    Set wsY4 = ThisWorkbook.Sheets("Y4")
    Set rngY4Z = wsY4.Range("A2:D100")
    rngY4Z.ClearContents
    arr = wsSS.Range("A1").CurrentRegion.Value
    For i = LBound(arr, 1) To UBound(arr, 1)
    If arr(i, 4) = "Y4" Then
    For j = 1 To 4
    wsY4.Cells(row, j).Value = arr(i, j)
    Next j
    row = row + 1
    End If
    Next i
End Sub



