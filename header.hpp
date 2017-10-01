class MyClass
{
public:
  int field;
  virtual void method() const = 0;

  static const int static_field;
  static int static_method();
  void print ()
    {
      cout << field << endl;
    }
};

int main (int a)
{
MyClass b;
return a;
}

struct type {
  int a;
  int b;
  int c;
};

int a[10] = {1, 2,3,
    4, 5};
