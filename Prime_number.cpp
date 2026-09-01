#include<iostream>
using namespace std;
int main () {
    int a;
    int n=2;
    cout<<"Enter a number"<<endl;
    cin>>a;
    if(a<=1)
    {cout<<"not prime"<<endl;
        return 0;}
    while(n<a)
    {if (a%n==0)
    {cout<<"not prime"<<endl;
    return 0;}
n=n+1;}
cout<<"prime"<<endl;
}