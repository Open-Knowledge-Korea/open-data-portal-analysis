OpenAPI ���������� �ڵ�� ������_���Ϻ�_�ʵ� CSV ����. 

�� �� CSV �����Ϳ� ���������� Excel ��ũ�θ� ����� �ʵ�� ���� ���� 1���� �ܼ� ���� �ٿ��ֱ�� ���ϸ� ���� ���� 1�� �ۼ�.

Sub TableToColumn()
    Dim Rng As Range, LR As Long, i As Long
    LR = Range("B" & Rows.Count).End(xlUp).Row # B = ���� ��
    For i = 2 To LR
        Set Rng = Range("B" & i, "E" & i)  # B / E ��� <- ����/���῭ 
        Range("A" & Rows.Count).End(xlUp)(2).Resize(Rng.Count) = Application.WorksheetFunction.Transpose(Rng) # A <- �ۼ���
    Next i
End Sub