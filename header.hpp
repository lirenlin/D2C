class MyClass
{
public:
  int field;
  virtual void method() const = 0;

  static const int static_field;
  static int static_method();
};

int main (int a)
{
MyClass b;
return a;
}
