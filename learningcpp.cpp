//EVERY CODE SEPERATED BY COMMENTS IS A CODE OF IT'S OWN I WROTE TO PRACTICE CONCEPTS AND QUESTIONS 

//student roll and marks
#include<iostream>
using namespace std;
//class(encapsulation)
class Student{
    //abstractions (public/private)
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
    //object
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

//constructors 
#include<iostream>
using namespace std;
class Student{
    
    private:
        int marks;
        int roll;
    
    public:
        
        Student(int m, int r){
            marks =m;
            roll = r;
        }
    
    void display(){
        cout << "Roll: " << roll << endl;
        cout << "Marks: "<< marks << endl;
        
    }
};

int main(){
    Student s1(50,98);
    
    s1.display();
    return 0;
}

// constructs circle
#include<iostream>
using namespace std;

class Circle{
    private:
        int radius;
    
    public:
        Circle(int r) : radius(r){}
        void display(){
            cout << "Area: " << (3.14)*radius*radius <<endl;
            
        }
        
};

int main(){
    
    Circle c1(5);
    
    c1.display();
    return 0; 
}

//constructs question:
#include<iostream>
using namespace std;

class Box{
    
    private:
        int length;
        int breadth;
        int height;
        
    public:
        
        Box(int l, int b,int h): length(l),breadth(b),height(h){}
        
        void display(){
            cout << "Volume: "<< length*breadth*height << endl;
            
        }
};

int main(){
    Box b1(10,5,4);
    b1.display();
    return 0;
}

//constructor overloading
#include<iostream>
using namespace std;
class Student{
    
    private:
        int roll;
        int marks;
    
    public:
        
        Student(){
            roll = 0;
            marks=0;
        }
        
        Student(int r, int m): roll(r),marks(m){}
        
        void display(){
            cout << "Roll: " << roll << endl;
            cout << "Marks: "<<marks << endl;
        }
        
};

int main(){
    Student s1;
    Student s2(101,90);
    s1.display();
    s2.display();
    return 0;
}

//function overloading
#include<iostream>
using namespace std;

class Add{
    
    public:
        int sum(int a,int b){
            return a+b;
        }
        float sum(float a,float b){
            return a+b;
        }
};

int main(){
    
    Add a1;
    
    cout << a1.sum(1,3) << endl;
    cout << a1.sum(2.5f,5.5f) << endl;
    return 0; 
}

//problem
#include<iostream>
using namespace std;

class Math{
    
    public:
        
        int add(int a,int b, int c){
            return a+b+c;
        }
        
        int add(int a,int b){
            return a+b;
        }
};

int main(){
    
    Math m;
    
    cout << "Sum of three numbers: "<<m.add(10,5,15)<<endl;
    cout << "Sum of two numbers: "<<m.add(10,5)<<
    endl;
    return 0;
    
}

//problem
#include<iostream>
using namespace std;

class Math{
    
    public:
        
        int add(int a,int b, int c){
            return a+b+c;
        }
        
        int add(int a,int b){
            return a+b;
        }
};

int main(){
    
    Math m;
    
    cout << "Sum of three numbers: "<<m.add(10,5,15)<<endl;
    cout << "Sum of two numbers: "<<m.add(10,5)<<
    endl;
    return 0;
    
}

//operator overloading
#include<iostream>
using namespace std;

class Complex{
    int real,imag;
    
    Complex(int r, int i): real(r),imag(i){}
    
    Complex operator+(Complex c){
        
        Complex temp(0,0);
        temp.real = real + c.real;
        temp.imag = imag + c.imag;
        return temp;
    }
    
    void display(){
        cout << real << "+"<<imag<<"i"<<endl;
        
    }
    
};

int main(){
    Complex c1(2,3);
    Complex c2(4,5);
    
    Complex c3 = c1 + c2;
    
    c3.display();
}


