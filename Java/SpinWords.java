public class SpinWords {

    public String spinWords(String sentence) {
      StringBuilder reversedStr = new StringBuilder();
      String[] words = sentence.split("\\s");
      for(String i: words){
        if (i.length() > 5) {
          StringBuilder reversedWord = new StringBuilder(i);
          reversedWord.reverse();
          reversedStr.append(reversedWord).append(" ");
          
        }
        else{
          reversedStr.append(i);
        }
      }
      return reversedStr.toString().trim();
    }
  }