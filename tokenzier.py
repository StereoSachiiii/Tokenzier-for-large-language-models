text='Life is a complex and unpredictable journey, often filled with moments of joy, sorrow, confusion, and clarity, all intricately woven together to form the tapestry of our experiences. As we navigate through its winding paths, we are constantly learning, adapting, and evolving—not just from our successes, but more importantly, from our failures and setbacks. Each day offers new opportunities to reflect, grow, and challenge ourselves, even when the odds seem overwhelming or when motivation is hard to find. The people we meet, the choices we make, and the environments we immerse ourselves in all shape who we become, influencing our character, values, and worldview. In a world where everything moves rapidly, it’s easy to lose sight of the simple, quiet moments that often carry the most meaning—like a late-night conversation with a close friend, the peaceful stillness of early morning, or the bittersweet feeling of remembering something beautiful from the past. Ultimately, the journey is not about reaching some final destination, but about learning to be present in the moment, finding purpose in the small things, and striving to become a better version of ourselves—one thought, one step, and one day at a time.'
tokens=text.encode('utf-8')

print('-------------------')
print(text)
print("length :",len(text))
print('-------------------')
tokens= list(map(int,tokens))
print(tokens)
print("length :",len(tokens))



def get_stats(ids):
    pairs = {}
    for i in range(0, len(ids) - 1, 2):
        pairs[i]=((ids[i], ids[i + 1]))

        if len(text) % 2 != 0:
            pairs[len(ids)-1]=((ids[-1],))
    return pairs
stats=get_stats(tokens)
print(stats)