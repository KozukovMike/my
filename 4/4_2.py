user_text = input()
our_dict = {i: user_text.count(i) for i in user_text}
result = sorted(our_dict.items(), key=lambda x: x[1], reverse=True)
print(dict(result))
