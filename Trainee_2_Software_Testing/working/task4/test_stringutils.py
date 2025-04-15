from stringutils import StringUtils


class TestStringUtils:
  
  def test_is_palindrome(self):
    obj = StringUtils()

    assert obj.is_palindrome('') == True 
    assert obj.is_palindrome(' ') == True 
    assert obj.is_palindrome('a') == True
    assert obj.is_palindrome(' a ') == True
    assert obj.is_palindrome('aa') == True
    assert obj.is_palindrome('aba') == True
    assert obj.is_palindrome('abBa') == True
    assert obj.is_palindrome('baaab') == True
    assert obj.is_palindrome('bAaab') == True

    assert obj.is_palindrome('ab') == False
    assert obj.is_palindrome('ab') == False
    assert obj.is_palindrome('abb') == False
    assert obj.is_palindrome('+10+') == False
    
  def test_count_vowels(self):
    obj = StringUtils()

    assert obj.count_vowels('') == 0
    assert obj.count_vowels('l1n3') == 0
    assert obj.count_vowels('A new line') == 4
    assert obj.count_vowels('A \tnew\nline') == 4
    assert obj.count_vowels('I=0;j=0;E=01') == 2
    assert obj.count_vowels('AEIOU') == 5
    assert obj.count_vowels('aeiou') == 5
    assert obj.count_vowels('aEiUo') == 5

  def test_reverse_words(self):
    obj = StringUtils()

    assert obj.reverse_words('') == ''
    assert obj.reverse_words('a') == 'a'
    assert obj.reverse_words('A new word') == 'A wen drow'
    assert obj.reverse_words('123 321') == '321 123'
    assert obj.reverse_words('a  b') == 'a b'