//student roll and marks
#include<iostream>
using namespace std;
class Student{
    public:
        int roll,marks;
        
        void input(){
            cout << "Enter roll: ";
            cin >> roll;
            cout << "Enter marks: ";
            cin >> marks;
        }
        void display(){
            cout << roll<<endl;
            
            cout << marks<<endl;
        }
};

int main(){
    Student s1;
    s1.input();
    s1.display();
    return 0;
}

//rectangle
#include<iostream>
using namespace std;

class Rectangle{
    private:
        int length;
        int breadth;
        
    public:
        int area;
        void setData(int l,int b){
            length = l;
            breadth = b;
            area = length*breadth;
        }
        void display(){
            cout << "Area: "<< area <<endl;
            
        }
};   
int main(){
    Rectangle r1;
    r1.setData(10,5);
    r1.display();
    return 0;
}

