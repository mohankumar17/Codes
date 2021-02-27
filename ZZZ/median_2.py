import sys
def medianTwo(x,y):
    if len(x)>len(y):
        x,y=y,x

    start_x=0
    end_x=len(x)

    while start_x<=end_x:
        position_x=(start_x+end_x)//2
        position_y=(len(x)+len(y)+1)//2-position_x

        if position_x==0:
            max_left_x=-sys.maxsize
        else:
            max_left_x=x[position_x-1]

        if position_x==len(x):
            min_right_x=sys.maxsize
        else:
            min_right_x=x[position_x]

        if position_y==0:
            max_left_y=-sys.maxsize
        else:
            max_left_y=y[position_y-1]

        if position_y==len(y):
            min_right_y=sys.maxsize
        else:
            min_right_y=y[position_y]

        if max_left_x<=min_right_y and max_left_y<=min_right_x:
            if (len(x)+len(y))%2==0:
                return (max(max_left_x,max_left_y)+min(min_right_x,min_right_y))/2
            else:
                return max(max_left_x,max_left_y)

        elif max_left_x>min_right_y:
            end_x=position_x-1

        else:
            start_x=position_x+1


x=[1,2]
y=[3,4,6,7]
print(medianTwo(x,y))
