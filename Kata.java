

public class Kata
{

  public static String reverseWords(final String original)
  {
    if (original.isEmpty()) {
      return original;  
  }
      StringBuilder reversedStr = new StringBuilder();
      String[] words = original.split("\\s");
      for (String i : words){
        StringBuilder reversedWord = new StringBuilder(i);
        reversedWord.reverse();
        reversedStr.append(reversedWord).append(" ");
      }
      return reversedStr.toString().trim();
  }
  
}
