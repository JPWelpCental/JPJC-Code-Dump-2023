def Partition(Scores, First, Last):
    PivotValue = Scores[First]
    LeftMark = First + 1
    RightMark = Last
    Done = False
    while not Done:
        while LeftMark <= RightMark and Scores[LeftMark] <= PivotValue:
            LeftMark += 1
        while Scores[RightMark] >= PivotValue and RightMark >= LeftMark:
            RightMark -= 1
        if RightMark < LeftMark:
            Done = True
        else:
            Scores[LeftMark], Scores[RightMark] = Scores[RightMark], Scores[LeftMark]
    Scores[First], Scores[RightMark] = Scores[RightMark], Scores[First]
    return RightMark

def QuickSortHelper(Scores, First, Last):
    if First < Last:
        SplitPoint = Partition(Scores, First, Last)
        QuickSortHelper(Scores, First, SplitPoint - 1)
        QuickSortHelper(Scores, SplitPoint + 1, Last)
    return Scores

def QuickSort(Scores):
    QuickSortHelper(Scores, 0, len(Scores) - 1)
    return Scores
