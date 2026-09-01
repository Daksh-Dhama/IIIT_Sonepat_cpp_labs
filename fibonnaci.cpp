#include<iostream>
#include<math.h>
using namespace std;
int main()
{cout<<"enter required series lenght"<<endl;
    int first_number=0;
    int second_number=1;
    int i=3;
    int n;
    int digit;
    cin>>n;
        if(n==1){
            cout<<"0"<<endl;
            return 0;}
            if(n==2){
                cout<<"0  "<<"1"<<endl;
                return 0;}
                cout<<"0 "<<"1 ";
                while(i<=n){
digit=first_number+second_number;
first_number=second_number;
second_number=digit;
i++;
cout<<digit<<" ";}
    }





    



