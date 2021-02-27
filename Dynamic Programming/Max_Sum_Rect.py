import sys
def kadens(ar):
    meh=0
    msf=-sys.maxsize
    for i in ar:
        meh=meh+i
        if meh<i:
            meh=i
        if meh>msf:
            msf=meh
    return msf

def maxSum(ar):
    m=0
    for L in range(0,len(ar[0])):
        t=[0]*len(ar)
        for R in range(L,len(ar[0])):
            for i in range(0,len(ar)):
                t[i]=t[i]+ar[i][R]
            res=kadens(t)
            if res>m:
                m=res

    return m

ar=[[2,1,-3,-4,5],
    [0,6,3,4,1],
    [2,-2,-1,4,-5],
    [-3,3,1,0,3]]

print(maxSum(ar))



'''
public class SubRectangularMatrixWithMaximumSum {

    class Result{
        int maxSum;
        int leftBound;
        int rightBound;
        int upBound;
        int lowBound;
        @Override
        public String toString() {
            return "Result [maxSum=" + maxSum + ", leftBound=" + leftBound
                    + ", rightBound=" + rightBound + ", upBound=" + upBound
                    + ", lowBound=" + lowBound + "]";
        }

    }

    public Result maxSum(int input[][]){
        int rows = input.length;
        int cols = input[0].length;
        int temp[] = new int[rows];
        Result result = new Result();
        for(int left = 0; left < cols ; left++){
            for(int i=0; i < rows; i++){
                temp[i] = 0;
            }
            for(int right = left; right < cols; right++){
                for(int i=0; i < rows; i++){
                    temp[i] += input[i][right];
                }
                KadaneResult kadaneResult = kadane(temp);
                if(kadaneResult.maxSum > result.maxSum){
                    result.maxSum = kadaneResult.maxSum;
                    result.leftBound = left;
                    result.rightBound = right;
                    result.upBound = kadaneResult.start;
                    result.lowBound = kadaneResult.end;
                }
            }
        }
        return result;
    }

    class KadaneResult{
        int maxSum;
        int start;
        int end;
        public KadaneResult(int maxSum, int start, int end) {
            this.maxSum = maxSum;
            this.start = start;
            this.end = end;
        }
    }

    private KadaneResult kadane(int arr[]){
        int max = 0;
        int maxStart = -1;
        int maxEnd = -1;
        int currentStart = 0;
        int maxSoFar = 0;
        for(int i=0; i < arr.length; i++){
            maxSoFar += arr[i];
            if(maxSoFar < 0){
                maxSoFar = 0;
                currentStart = i+1;
            }
            if(max < maxSoFar){
                maxStart = currentStart;
                maxEnd = i;
                max = maxSoFar;
            }
        }
        return new KadaneResult(max, maxStart, maxEnd);
    }


    public static void main(String args[]){
        int input[][] = {{ 2,  1, -3, -4,  5},
                         { 0,  6,  3,  4,  1},
                         { 2, -2, -1,  4, -5},
                         {-3,  3,  1,  0,  3}};
        SubRectangularMatrixWithMaximumSum saw = new SubRectangularMatrixWithMaximumSum();
        System.out.println(saw.maxSum(input));
    }
}

'''
