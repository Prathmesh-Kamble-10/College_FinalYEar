#include <iostream>
#include <vector>
using namespace std;
int notes[] = { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 };
int n = sizeof(notes) / sizeof(notes[0]);
void minchange(int sum)
{
   vector<int> coins;
   for (int i = n - 1; i >= 0; i--)
   {
      while (sum >= notes[i]) 
      {
         sum -= notes[i];
         coins.push_back(notes[i]);
      }
   }
   for (int i = 0; i < coins.size(); i++)
      cout << coins[i] << "\t";
}
int main(){
   int n = 8540;
   cout << "The minimum number of coins/notes that sum up " << n << " is \t ";
   minchange(n);
   return 0;
}
