OpenAPI 데이터정리 코드로 데이터_파일별_필드 CSV 생성. 

그 후 CSV 데이터와 마찬가지로 Excel 매크로를 사용해 필드명 나열 파일 1개와 단순 복사 붙여넣기로 파일명 나열 파일 1개 작성.

Sub TableToColumn()
    Dim Rng As Range, LR As Long, i As Long
    LR = Range("B" & Rows.Count).End(xlUp).Row # B = 시작 열
    For i = 2 To LR
        Set Rng = Range("B" & i, "E" & i)  # B / E 대신 <- 시작/종료열 
        Range("A" & Rows.Count).End(xlUp)(2).Resize(Rng.Count) = Application.WorksheetFunction.Transpose(Rng) # A <- 작성열
    Next i
End Sub