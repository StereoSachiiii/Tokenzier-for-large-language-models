text = "Life is a complex and unpredictable journey, often filled with moments of joy, sorrow, confusion, and clarity, all intricately woven together to form the tapestry of our experiences. As we navigate through its winding paths, we are constantly learning, adapting, and evolving—not just from our successes, but more importantly, from our failures and setbacks. Each day offers new opportunities to reflect, grow, and challenge ourselves, even when the odds seem overwhelming or when motivation is hard to find. The people we meet, the choices we make, and the environments we immerse ourselves in all shape who we become, influencing our character, values, and worldview. In a world where everything moves rapidly, it's easy to lose sight of the simple, quiet moments that often carry the most meaning—like a late-night conversation with a close friend, the peaceful stillness of early morning, or the bittersweet feeling of remembering something beautiful from the past. Ultimately, the journey is not about reaching some final destination, but about learning to be present in the moment, finding purpose in the small things, and striving to become a better version of ourselves—one thought, one step, and one day at a time."

tokens = text.encode('utf-8')
tokens = list(map(int, tokens))

def get_stats(ids):
    counts = {}
    for i in range(len(ids) - 1):
        a = ids[i]
        b = ids[i + 1]
        pair = (a, b)
        if pair in counts:
            counts[pair] += 1
        else:
            counts[pair] = 1
    return counts

def get_max(stats):
    max_pair = None
    max_count = -1
    for pair in stats:
        if stats[pair] > max_count:
            max_count = stats[pair]
            max_pair = pair
    return max_pair

def merge(tokens, max_pair, new_id):
    new_tokens = []
    i = 0
    while i < len(tokens):
        if i < len(tokens) - 1 and tokens[i] == max_pair[0] and tokens[i + 1] == max_pair[1]:
            new_tokens.append(new_id)
            i += 2
        else:
            new_tokens.append(tokens[i])
            i += 1
    return new_tokens

tokens2 = list(tokens)
merges = {}
i = 0

while True:
    stats = get_stats(tokens2)

    repeat_pairs = {}
    for pair in stats:
        if stats[pair] > 1:
            repeat_pairs[pair] = stats[pair]

    has_repeats = False
    for _ in repeat_pairs:
        has_repeats = True
        break

    if not has_repeats:
        break

    max_pair = get_max(repeat_pairs)
    new_token = 256 + i
    print("Merging", max_pair, "into new token", new_token)
    tokens2 = merge(tokens2, max_pair, new_token)
    merges[max_pair] = new_token
    i += 1

print("\nFinal token list:", tokens2)
print("Number of tokens:", len(tokens2))
print("Old token length:", len(tokens))
print(i, "vocabulary tokens added. Final vocab size:", 256 + i)
