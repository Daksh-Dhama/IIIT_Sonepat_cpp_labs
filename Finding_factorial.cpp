#include<iostream>
using namespace std;
int main()
{cout<<"Enter a number to find its factorial:"<<endl;
int n;
cin>>n;
int j=1;
for(int i=1;i<=n;i++)
{
 j=j*i;}
cout<<"Factorial of "<<n<<" is "<<j<<endl;
}