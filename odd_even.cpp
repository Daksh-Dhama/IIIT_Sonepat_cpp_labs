#include<iostream>
using namespace std;
int main(){
    int a;
    cout<<"enter a number"<<endl;
    cin>>a;
    if(a==0)
    {cout<<"neither even nor odd"<<endl;
    return 0;}
    if(a%2==0)
    {
        cout<<a<<" is even"<<endl;
    }
    else{
        cout<<a<<" is odd"<<endl;
    }
}
    