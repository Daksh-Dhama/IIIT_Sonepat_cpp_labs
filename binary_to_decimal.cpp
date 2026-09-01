#include<iostream>
using namespace std;
int main()
{
    cout<<"enter your number"<<endl;
    int n;
    int decimal=0;
    int power_2=1;
    cin>>n;
    while( n>0)
    {int remainder=n%10;
        if(remainder!=0 && remainder!=1)
        {cout<<"invalid digit entered "<<remainder<<endl;
        return 0; }
    decimal+=(remainder*power_2);
power_2*=2;
n=n/10;}
cout<<"decimal is " <<decimal<<endl;
}