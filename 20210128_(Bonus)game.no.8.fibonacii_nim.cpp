#include<iostream>
#include<string>
#include<cmath>
using namespace std;
unsigned long long int factorial(int m)

{
int c=m;
unsigned long long int factorial=1;
while (c>=1)
{
factorial*=c;
c--;
}
return factorial;

}


long double value (long double sum ,double y ,int m, long double  l)
{
 l=factorial(m);
  long double newFactorial =2;
  unsigned long long int power=0;
  unsigned long long int newPower=1;
 //unsigned long long int l=factorial(m); Testing github
 while (m<=100 && l<=newFactorial && newPower>=power)

{
  power=pow(y,m);
  cout<< "power is: "<<power<<'\n'<<factorial(m)<<'\n';
  l=factorial(m);
  sum=sum+(power/(l));
  cout<<'\n'<<"sum is: "<<sum<<'\n';
  m++;
  newFactorial  =factorial(m);
  newPower= pow(y,m);

}
return sum;
}


void show(int m,double y)

{

//int m=1;

  string display="1";
  while (m<=100)

{
     string x=to_string(y) ;
     string n=to_string(m);
     display+="+("+x+'^'+n+")/"+n;
     m++;


     if((m-1)%10 ==0)
     {

   display+='\n';
  }
}

   cout<<display;

}


int main()

 {

  //unsigned long long int l=factorial(m);
  long double sum=1;
  cout<<"exp: "<<exp(9);
  int m=1;
  long double l=factorial(m);
  //unsigned long long int power=0;
  //unsigned long long int newPower=1;
  double y;
  cout<<"enter a number:";
  cin>>y;
 // show(m,y);
  //cout<<m;r
  cout<<"/nI love you";
  cout<<'='<<value(sum,y,m,l);

     return 0;

}
