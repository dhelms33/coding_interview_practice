public String front3(String str) {
  int digit = 3;
  if (str.length() < 3 ) {
    digit = str.length();
  }
  String frontThree = str.substring(0, digit);
  return (frontThree +frontThree + frontThree);
}