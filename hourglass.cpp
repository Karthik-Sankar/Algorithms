//problem question link - https://www.hackerrank.com/challenges/2d-array/problem

#include <iostream>
using namespace std;
int main(){
    int main_arr[6][6];
    int sum_of_hg[16];
    int temp = 0;
    int a=0,b=0,c=0,d=0,e=0,f=0,g=0;
    int max=-999;
    for(int i=0;i<6;i++)
        for(int j=0;j<6;j++)
            cin>>main_arr[i][j];
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            a = main_arr[i][j];
            b = main_arr[i][j+1];
            c = main_arr[i][j+2];
            d = main_arr[i+1][j+1];
            e = main_arr[i+2][j];
            f = main_arr[i+2][j+1];
            g = main_arr[i+2][j+2];
            temp = a+b+c+d+e+f+g;
            if(max<temp)
                max=temp;
        }
    cout<<max;
    return 0;
}

