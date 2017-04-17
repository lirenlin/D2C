#include <iostream>
#include <clang-c/Index.h>  // This is libclang.
using namespace std;

int main()
{
  CXIndex index = clang_createIndex(0, 0);
  CXTranslationUnit unit = clang_parseTranslationUnit(
    index, "header.hpp", 0, 0, 0, 0, CXTranslationUnit_None);

  if (unit == 0)
  {
    cerr << "Unable to parse translation unit. Quitting." << endl;
    return -1;
  }

  CXFile file = clang_getFile (unit, "header.hpp");
  CXSourceLocation loc = clang_getLocation (unit, file, 8, 1);
  CXCursor cursor = clang_getCursor (unit, loc);
  CXCursor parent = clang_getCursorLexicalParent(cursor);

  //if (clang_getCursorKind (cursor) == CXCursor_CompoundStmt)
  {
    cout << clang_getCString (clang_getCursorKindSpelling (clang_getCursorKind(cursor))) << endl;
    cout << clang_getCString (clang_getCursorKindSpelling (clang_getCursorKind(parent))) << endl;
  }
  cout << "hello";

  clang_disposeTranslationUnit(unit);
  clang_disposeIndex(index);
}
