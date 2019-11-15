#include <stdio.h>
#include <string.h>

int IsPasswordOkay(void)
{
  char Password[12];
  gets(Password);

  if (!strcmp(Password, "goodpass"))
    return 1;

  return 0;
}

int main(void)
{
  int PwStatus;

  puts("Enter password:");
  PwStatus = IsPasswordOkay();
  if (PwStatus == 0) {
    puts("Access denied");
    return -1;
  }
  puts("Access granted");
  return 0;
} 