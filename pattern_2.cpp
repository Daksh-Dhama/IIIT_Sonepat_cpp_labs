#include<iostream>
using namespace std;
int main() {
 cout<<"Please enter a number"<<endl;
 int a;
 cin>>a;
 int i=1;
 while(i<=a)
 {
    int j=1;
    while(j<=a)
    {cout<<i;
    j=j+1;}
    cout<<endl;
    i=i+1;}
}