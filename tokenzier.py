text = "Life is a complex and unpredictable journey, often filled with moments of joy, sorrow, confusion, and clarity, all intricately woven together to form the tapestry of our experiences. As we navigate through its winding paths, we are constantly learning, adapting, and evolving—not just from our successes, but more importantly, from our failures and setbacks. Each day offers new opportunities to reflect, grow, and challenge ourselves, even when the odds seem overwhelming or when motivation is hard to find. The people we meet, the choices we make, and the environments we immerse ourselves in all shape who we become, influencing our character, values, and worldview. In a world where everything moves rapidly, it's easy to lose sight of the simple, quiet moments that often carry the most meaning—like a late-night conversation with a close friend, the peaceful stillness of early morning, or the bittersweet feeling of remembering something beautiful from the past. Ultimately, the journey is not about reaching some final destination, but about learning to be present in the moment, finding purpose in the small things, and striving to become a better version of ourselves—one thought, one step, and one day at a time."
tokens = text.encode('utf-8')
print('-------------------')
print(text)
print("length :", len(text))
print('-------------------')
tokens = list(map(int, tokens))
print(tokens)
print("length :", len(tokens))

def get_stats(ids):
    counts = {}
    for i in range(len(ids) - 1):
        pair = (ids[i], ids[i + 1])
        counts[pair] = counts.get(pair, 0) + 1
    return counts

stats = get_stats(tokens)
print(stats)

def get_max(dic):
    if not dic:
        return None
    return max(dic, key=dic.get)

max_pair = get_max(stats)
print(max_pair)

def merge (tokens,max_pair,id):
    newtokens=[]
    i=0
    while i<len(tokens):
        if i<len(tokens)-1 and max_pair[0]==tokens[i] and max_pair[1] == tokens [i+1]:
            newtokens.append(id)
            i+=2
        else:
            newtokens.append(tokens[i])        
            i+=1
    return newtokens

newtokenlist =merge(tokens,max_pair,len(tokens) )
print(newtokenlist)

