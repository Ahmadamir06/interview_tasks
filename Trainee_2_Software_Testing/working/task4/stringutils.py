

class StringUtils:
  def is_palindrome(self, text):
      text = text.lower().replace(" ", "")
      return text == text[::-1]

  def count_vowels(self, text):
      return sum(1 for char in text.lower() if char in 'aeiou')

  def reverse_words(self, sentence):
      return ' '.join(word[::-1] for word in sentence.split())