# string.strip([chars]) 可以去除字符串首位字符 lstrip 可以去除左边字符  rstrip可以去除右边字符
print('stringstring'.rstrip('ing'))
print('stringstring'.strip('str'))
print('stringstring'.rstrip('ing'))
# copy字符串
print('string'[0:])
# 在字符串中查找字符串 find 和 index 是都会返回索引值 但是 找不到的时候index 会报异常
print('string'.find('k'))
print('string'.rfind('g'))
#比较字符串
print('str'=='strr')
#字符串长度
print(len('str'))
#大小写转换
print('Str'.lower())
print('Str'.upper())
print('stsST'.swapcase())
print('str'.capitalize())
#翻转字符串
print('string'[::-1])
#分割字符串
print('string'.split('i'))
#字符出现次数
print('stringstringstrng'.count('i'))
#替换字符串
print('stringi'.replace('i','g',2))
#字符串的判断测试
print('  '.isspace())
print('T  '.istitle())
print('T  '.islower())
print('Td'.isupper())
print('211321'.isdigit())
print('str0'.isalpha())
print('str'.startswith('s'))
print('strsdd'.endswith('dd'))

