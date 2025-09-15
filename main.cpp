/*
    긍정

    DP
        - Identifying and solving subproblems
        - Using subproblems together to solve larger problem

        LIS
            focus on the length of the LIS
            find an appropriate subproblem
                ex) all IS have a start & end
                    LIS[4] = 1 + max {LIS[0], LIS[1], LIS[3]}
            find relationships among subproblems
            generalize the relationship
            implement by solving subproblems in **appropriate** order
                def lis(A):
                    L = [1] * len(A)
                    for i in range(1,len(L)):
                        subproblems = 
                        L[i] = 1 + max(subproblems,0)

 */